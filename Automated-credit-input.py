from PIL import Image
from PIL import ImageDraw
import tkinter
from tkinter import filedialog

fle = tkinter.filedialog.askopenfilenames(filetypes=[('', '*')],initialdir = "{PWD}")

for i in fle:
  opendimage = Image.open(str(i))
  output_image = ImageDraw.Draw(opendimage)
  output_image.text((28, 36), "hello world", fill=(255, 0, 0))
  opendimage.save("test.png")

