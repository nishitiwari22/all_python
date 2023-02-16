# 11) Write a Python GUI program to create a textbox and two buttons exit and hello using
# tkinter module. Display message on the click of hello button

import tkinter as tk   

def write_text():
    print("Tkinter is easy to create GUI!")

parent = tk.Tk()
frame = tk.Frame(parent)
frame.pack()

text_disp= tk.Button(frame, 
                   text="Hello", 
                   command=write_text
                   )

text_disp.pack(side=tk.LEFT)

exit_button = tk.Button(frame,
                   text="Exit",
                   fg="green",
                   command=quit)
exit_button.pack(side=tk.RIGHT)

parent.mainloop()