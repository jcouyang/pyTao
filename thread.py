import threading,time
import cocoaGui

def threda():
    cocoaGui.main()
def thredb():
    time.sleep(3)
    print 'thread b'
background2 = threading.Thread(target=threda)

background2.start()
print 'The main program continues to run in foreground.'

#background.join()    # Wait for the background task to finish
print 'Main program waited until background was done.'