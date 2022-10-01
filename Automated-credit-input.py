from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import tkinter
from tkinter import filedialog
import os

fle = tkinter.filedialog.askopenfilenames(filetypes=[('', '*')],initialdir = "{PWD}") 

for i in fle:
  input_image = Image.open(str(i))
  output_image = ImageDraw.Draw(input_image)
  output_image.text((50, 50),"Satellite Imagery © Maxar Technologies Provided by European Space Imaging", fill=(0, 0, 0),)
  input_image.save("new_" + os.path.basename(i) )