from zxing import *

zxing_location = "./zxing/"
testimage = "sample.png"

zx = BarCodeReader(zxing_location) 
barcode = zx.decode(testimage)
print barcode.data