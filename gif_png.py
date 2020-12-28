from PIL import Image
import os
import os.path

filepath = input(r'读取文件路径, 用这个/，比如 C:/Users/hn/Desktop/印章图集（教育部）/印章图集（教育部）/高河城区幼儿园，：')
#rootdir = r'C:\用户目录\我的图片\From Yun\背景图\背景图'  # 指明被遍历的文件夹
rootdir = filepath #原图片目录
outputdir = input(r'输出图片路径，用这个/，比如 C:/Users/hn/Desktop/PNG，：')

def gif_png(rootdir, outputdir):
    for parent, dirnames, filenames in os.walk(rootdir):#遍历每一张图片
        for filename in filenames:
            print('parent is :' + parent)
            print('filename is :' + filename)
            currentPath = os.path.join(parent, filename)
            print('the fulll name of the file is :' + currentPath)
    
            im = Image.open(currentPath)#打开gif格式的图片
            def iter_frames(im):
                try:
                    i= 0
                    while 1:
                        im.seek(i)
                        imframe = im.copy()
                        if i == 0:
                            palette = imframe.getpalette()
                        else:
                            imframe.putpalette(palette)
                        yield imframe
                        i += 1
                except EOFError:
                    pass   
            for i, frame in enumerate(iter_frames(im)):
                print('frame信息：==>')
                print(frame.info)
                filename = filename[0:-4]
                frame.save(outputdir + r'/' + filename +'.png',
                'png')
                
                new = Image.open(outputdir + r'/' + filename +'.png')
                new = new.resize((992,992),Image.NEAREST)
                new.save(outputdir + r'/' + filename +'.png','png', dpi = (600.0,600.0))
                # //frame.save(r"/Users/mamabang/Downloads/new_emoticon/"+filename +'.png',**frame.info)

# Transform the gifs to png
gif_png(rootdir,outputdir)

