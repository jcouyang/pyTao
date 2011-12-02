#!/usr/bin/python

from taobaoapi2 import *
from Tkinter import *
import ttk
from zxing import *
import urllib,urllib2
import webbrowser
import cocoaGui
import time
from multiprocessing import Pool
import threading
zxing_location = "./zxing/"
testimage = "sample.png"
containerUrl = 'http://container.api.tbsandbox.com/container?appkey='
root = Tk()
sessionKey = '610172754c735a0137e5936b66b058121c315c72670da62180020093'
root.title ='taobao helper'
soldItems = []
import os
# Initialize our country "databases":
#  - the list of country codes (a subset anyway)
#  - a parallel list of country names, in the same order as the country codes
#  - a hash table mapping country code to population<
countrycodes = ('ar', 'au', 'be', 'br', 'ca', 'cn', 'dk', 'fi', 'fr', 'gr', 'in', 'it', 'jp', 'mx', 'nl', 'no', 'es', 'se', 'ch')
##countrynames = ('Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada', 'China', 'Denmark', \
##        'Finland', 'France', 'Greece', 'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Norway', 'Spain', \
##        'Sweden', 'Switzerland')
#cnames = StringVar(value=countrynames)
countrynames=[]
populations = {'ar':41000000, 'au':21179211, 'be':10584534, 'br':185971537, \
        'ca':33148682, 'cn':1323128240, 'dk':5457415, 'fi':5302000, 'fr':64102140, 'gr':11147000, \
        'in':1131043000, 'it':59206382, 'jp':127718000, 'mx':106535000, 'nl':16402414, \
        'no':4738085, 'es':45116894, 'se':9174082, 'ch':7508700}

# Names of the gifts we can send
gifts = { 'card':'Greeting card', 'flowers':'Flowers', 'nastygram':'Nastygram'}

# State variables
gift = StringVar()
sentmsg = StringVar()
statusmsg = StringVar()
companies = []

class AsyncGui(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        cocoaGui.main()


def getSoldItem(*args):
    # Taobao bussinuss
    itemSold = TradesSoldGet()
    itemSold.setParams(session=sessionKey.get(),status='WAIT_SELLER_SEND_GOODS')
    itemSold.fetch()
    return itemSold.datas

def getCompany(*args):
    deliveryCompany = CompaniesGet()
    deliveryCompany.fetch()
    
    return deliveryCompany.datas
    
#print deliveryCompany.datas


# Show item detail
def showDetail(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        print idx
        print soldItems
        for order in soldItems:
            detailText.insert('1.0',order['title']+'\n')

def readCode():
    print 'read started'
# scan barcode
def test1():
    
    print 'scan done'
def test2():
    print 'process1'
def scanBarcode(*args):
    idxs = lbox.curselection()
    print 'scan'
    tr1 = threading.Thread(target=test1)
    tr1.start()
    cocoaGui.main()
    return

# Create and grid the outer content frame
c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=1, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

sercetCode = StringVar()
sercetCode.set('sandbox6881dbe428ca0c26422cf2487')
api_key =  StringVar()
api_key.set('12408725')


# auth_url = 'http://container.api.tbsandbox.com/container?appkey=%s' % api_key
# taobao_url ='http://gw.api.tbsandbox.com/router/rest'
# sign = 'slFDafsWNuIC5UyIw03hkA%3D%3D'

scEntry = ttk.Entry(c,width=20, textvariable=sercetCode)
scEntry.grid(column=0,row=0, sticky=W)
ttk.Entry(c,width=20, textvariable=api_key).grid(column=1,row=0)

sessionKey = StringVar()
sessionKey.set('610172754c735a0137e5936b66b058121c315c72670da62180020093')
ttk.Entry(c,width=20, textvariable=sessionKey).grid(column=2,row=0)

def setApi(*args):
    base.sercetCode = sercetCode.get()
    base.api_key=api_key.get()
    #urlopen = urllib2.urlopen()
    webbrowser.open_new_tab(containerUrl+api_key.get())
   
    #setList()
    
Button(c, text="login", command=setApi).grid(column=3, row=0)



lbox = Listbox(c, height=5)
def setList(*args):
    lbox.delete(0, END)
    base.sercetCode = sercetCode.get()
    base.api_key=api_key.get()
    
    deliveryComp = StringVar()
    compVar = [x['name'] for x in getCompany()]
    deliveryComp.set(compVar[0])
    
    compCB = apply(OptionMenu, (c, deliveryComp) + tuple(compVar))
    compCB.grid(column='1',row='1')
    global soldItems 
    soldItems = getSoldItem()
    print soldItems
    for item in soldItems:
        i = item['orders']['order'][0]
        lbox.insert(END, i['title']+'\t|'+item['buyer_nick'])
        countrynames.append(i['title'])
        
        
ttk.Button(c,text='get sold items',command=setList).grid(column=3,row=1)

ttk.Button(c,text='Scan bar code',command=scanBarcode).grid(column=2,row=1)


    
lbl = ttk.Label(c, text="Send to country's leader:")
g1 = ttk.Radiobutton(c, text=gifts['card'], variable=gift, value='card');
g2 = ttk.Radiobutton(c, text=gifts['flowers'], variable=gift, value='flowers');
g3 = ttk.Radiobutton(c, text=gifts['nastygram'], variable=gift, value='nastygram');
send = ttk.Button(c, text='Send Gift', command=scanBarcode, default='active')
sentlbl = ttk.Label(c, textvariable=sentmsg, anchor='center');
status = ttk.Label(c, textvariable=statusmsg, anchor=W);
detailText = Text(c)
detailText.grid(column=1,row=9)
detailText.insert('1.0','sdf')
# Grid all the widgets
lbox.grid(column=0, row=1, rowspan=6, sticky=(N,S,E,W))
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(5, weight=1)

# Set event bindings for when the selection in the listbox changes,
# when the user double clicks the list, and when they hit the Return key
lbox.bind('<<ListboxSelect>>', showDetail)
#lbox.bind('<Double-1>', sendGift)
#root.bind('<Return>', sendGift)	

# Colorize alternating lines of the listbox
#for i in range(0,len(countrynames),2):
#    lbox.itemconfigure(i, background='#f0f0ff')

# Set the starting state of the interface, including selecting the
# default gift to send, and clearing the messages.  Select the first
# country in the list; because the <<ListboxSelect>> event is only
# generated when the user makes a change, we explicitly call showPopulation.
gift.set('card')
sentmsg.set('')
statusmsg.set('')
lbox.selection_set(0)
#showPopulation()

root.mainloop()
