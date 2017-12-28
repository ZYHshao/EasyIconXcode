# --coding:utf-8--
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
def startWork(filePath,dirPaht):
    imgSize = [(1024,1024),(167,167),(80,80),(40,40),(152,152),(76,76),(20,20),(40,40),(29,29),(58,58),(120,120),(180,180),(87,87),(60,60)]
    for size in imgSize:
        outfile = dirPaht+"/"
        oriIm = open(filePath)
        indata = oriIm.read()
        oriIm.close()
        outdata = open(outfile + str(size[0])+".png", "w")
        outdata.write(indata)
        newImage = Image.open(outfile + str(size[0])+".png")
        out = newImage.resize(size, Image.ANTIALIAS)
        out.save(outfile + str(size[0])+".png")
        outdata.close()
        newImage.close()











