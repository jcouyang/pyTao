from math import sin, cos, pi
from Foundation import *
from AppKit import *
from QTKit import*
import objc
from PyObjCTools import AppHelper
import threading

import time

imageBufferToRelease = None
mCurrentImageBuffer = None
imageBufferToRelease = None
class AppDelegate(NSObject):
    lock = threading.Lock()
    
    def captureOutput_didOutputVideoFrame_withSampleBuffer_fromConnection_(self,captureOutput,videoFrame,sampleBuffer,connection):
        print 'caputure out put'
        CVBufferRetain(videoFrame);

        self.lock.acquire()
        global  mCurrentImageBuffer
        global imageBufferToRelease
        try:   
            print 'videoFrame:',videoFrame
            imageBufferToRelease = mCurrentImageBuffer;

            mCurrentImageBuffer = videoFrame;
        finally:
            self.lock.release()
        CVBufferRelease(imageBufferToRelease);
        print 'capture done'
    def windowWillClose_(self, notification):
        app.terminate_(self)
    def snap(self):
        
        imageBuffer = None
        self.lock.acquire()
        try:
            print 'unlock'
            imageBuffer = CVBufferRetain(mCurrentImageBuffer);
        finally:
            self.lock.release()

            
        print imageBuffer
        if (imageBuffer) :

            ciimage = CIImage.imageWithCVImageBuffer_(imageBuffer)
            imageRep = NSCIImageRep.imageRepWithCIImage_(ciimage);

            bitrep = NSBitmapImageRep.alloc().initWithCIImage_(ciimage)
            bitdata = bitrep.representationUsingType_properties_(NSBMPFileType, objc.NULL)

            # Save image to disk using Cocoa
            bitdata.writeToFile_atomically_("tmp.bmp", False)
        
        print 'save'
        #AppHelper.stopEventLoop()
        

def main( ):
    global app
    loopPool=NSAutoreleasePool.alloc().init();
    app = NSApplication.sharedApplication( )
    graphicsRect = NSMakeRect(100, 100, 640, 530)
    myWindow = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
    graphicsRect, 
    NSTitledWindowMask 
    | NSClosableWindowMask 
    | NSResizableWindowMask
    | NSMiniaturizableWindowMask,
    NSBackingStoreBuffered,
    False).autorelease()
    myWindow.setTitle_('webcam')
    #    myView = DemoView.alloc( ).initWithFrame_(graphicsRect)
    #    myWindow.setContentView_(myView)
    #    myDelegate = AppDelegate.alloc( ).init( )
    #    myWindow.setDelegate_(myDelegate)
    
    iSight = QTCaptureDevice.defaultInputDeviceWithMediaType_(QTMediaTypeVideo)
    iSight.open_(None)
    myInput = QTCaptureDeviceInput.deviceInputWithDevice_(iSight)
    print iSight
    session =  QTCaptureSession.alloc().init().autorelease()
    print session
    session.addInput_error_(myInput,None)
    outputView = QTCaptureView.alloc().init().autorelease()
    
    outputView.setCaptureSession_(session)
    
    myDelegate = AppDelegate.alloc().init().autorelease()
    
    captureOutput = QTCaptureDecompressedVideoOutput.alloc().init().autorelease()
    captureOutput.setDelegate_(myDelegate)
    session.addOutput_error_(captureOutput, None)
    print session
    button = NSButton.alloc().initWithFrame_(NSMakeRect(300, 10, 60, 30)).autorelease()
    button.setBezelStyle_(NSRoundedBezelStyle)
    button.setTitle_('Click')
    button.setAction_('snap');
    
    outputView.setFrame_(NSMakeRect(0,50,640,480))
    print outputView
    myWindow.contentView().addSubview_(outputView)
    myWindow.contentView().addSubview_(button)
           
    myWindow.setDelegate_(myDelegate)
           
    session.startRunning()        
    # myWindow.setContentView_(myview)
    myWindow.display( )
    myWindow.orderFrontRegardless( )
    print myWindow
    AppHelper.runEventLoop()
    #app.run( )
    loopPool.drain()
    
    print 'Done'
    
def test():
    time.sleep(2)
    print 'test pool'
if __name__ == '__main__':
    main()