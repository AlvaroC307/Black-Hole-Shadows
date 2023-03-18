from wand.image import Image as WandImage #Hay que instalar esto en el ordenador

#para intalar: pip install wand 
#Si hay que instalar pip: python -m ensurepip --default-pip
#You can download Ghostscript from the official website: https://www.ghostscript.com/download/gsdnld.html


# open the EPS file using Wand
eps_path = "./Graphics/Black_Hole_Image.eps"
with WandImage(filename=eps_path) as image:
    # convert the EPS file to a JPEG file
    jpg_path = "./Graphics/Black_Hole_Image.jpg"
    with image.convert('jpeg') as converted:
        converted.save(filename=jpg_path)