# from tkinter import *


# import tkinter as Tk
# nishi_root = Tk()
# The above creates a basic UI the base which is essential in every GUI

# frm = ttk.Frame(nishi_root, padding=10)
# frm.grid()

# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=nishi_root.destroy).grid(column=1, row=0)


# nishi_root.mainloop()
# Remembering the GUI logic which the user used.

# import tkinter
# print("the imported file is", tkinter.__file__)


# from tkinter import tk

# from tkinter import ttk


# # ⛔️ NameError: name 'tk' is not defined. Did you mean: 'ttk'?
# root = tk.Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()

# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# root.mainloop()


# import tkinter as tk
# from tkinter import *
# from tkinter import ttk

# class karl( Frame ):
#     def __init__( self ):
#         tk.Frame.__init__(self)
#         self.pack()
#         self.master.title("Karlos")
#         self.button1 = Button( self, text = "CLICK HERE", width = 25,
#                                command = self.new_window )
#         self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )
#     def new_window(self):
#         self.newWindow = karl2()
# class karl2(Frame):     
#     def __init__(self):
#         new =tk.Frame.__init__(self)
#         new = Toplevel(self)
#         new.title("karlos More Window")
#         new.button = tk.Button(  text = "PRESS TO CLOSE", width = 25,
#                                  command = self.close_window )
#         new.button.pack()
#     def close_window(self):
#         self.destroy()
# def main(): 
#     karl().mainloop()
# if __name__ == '__main__':
#     main()

# # import mysql.connector
# import re

# txt = "The rain in Spain"
# # x = re.search("^The.*Spain$", txt)

# x = re.findall("Portugal", txt)
# print(x)

# if x:
#     print("Woo-ohh!")
# else:
#     print("LOL")



# import tkinter as Tk
# # m = tkinter.TK() # w=Button(master, option=value)

# r = tk.Tk()  

# Widgets are added here
# r.title('Counting Seconds')
# button = tk.Button(r, text= 'Stop', width=25, command=r.destroy)
# button.pack()

# w = Canvas(master, option=value)
# master is the parameter used to represent the parent window.

from tkinter import *
master = Tk()
# w = Canvas(master, width=40, height = 60)
# w.pack()
# canvas_height=20
# canvas_width=200
# y = int(canvas_height / 2)
# w.create_line(0, y, canvas_width, y)


# Checkbox

# var1 = IntVar()
# Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
# var2 = IntVar()
# Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)


# Entry

Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column = 1)
e2.grid(row=1, column=1)

mainloop()
# r.mainloop()





# https://www.codewithharry.com/videos/python-gui-tkinter-hindi-3/