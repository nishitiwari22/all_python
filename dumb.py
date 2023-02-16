from tkinter import *
from PIL import Image, ImageTk


# pip install pillow (for images in python)
first_root = Tk()

# Width x Height
first_root.geometry("644x434")
# photo = PhotoImage(file="women.jpg")

# For JPG Images
image = Image.open("women.jpg")
photo = ImageTK.PhotoImage(image)

nishi_label = Label(image=photo)
# width, height
# first_root.minsize(300,100)

# width, height
# first_root.maxsize(1200, 988)

# nishi = Label(text="Nishi is a good girl and this is her GUI")
nishi_label.pack()


first_root.mainloop()

