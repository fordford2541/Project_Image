from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


GUI = Tk()
GUI.title('License Detection')
GUI.option_add("*Font", "consolas 20")

# Variable
unit = StringVar()
result0 = StringVar()
result1 = StringVar()
result2 = StringVar()
result3 = StringVar()
result4 = StringVar()
result5 = StringVar()
result6 = StringVar()
result_sum = StringVar()
service = StringVar()
result_sum2 = StringVar()
ft = StringVar()
vat = StringVar()
result_total = StringVar()

f1p1 = Image.open("test photo/1080p/IMG_1 (20).jpg")
photo = ImageTk.PhotoImage(f1p1)

# Beam Textbox
L00 = ttk.Label(GUI)
L00.grid(row = 0, column = 0)

L10 = ttk.Label(GUI)
L10.grid(row = 1, column = 0)



L40 = ttk.Label(GUI)
L40.grid(row = 2, column = 0)

Label(L00, text = 'Datasheet').grid(row = 0, column = 0)

Label(L10, text = '  3 Floor  ').grid(row = 0, column = 0, rowspan = 2)

Button(L10, text = ' ', width = '15').grid(row = 0, column = 1)
Button(L10, text = ' ', width = '15').grid(row = 0, column = 2)
Button(L10, text = ' ', width = '15').grid(row = 0, column = 3)
Button(L10, text = ' ', width = '15').grid(row = 1, column = 1)
Button(L10, text = ' ', width = '15').grid(row = 1, column = 2)
Button(L10, text = ' ', width = '15').grid(row = 1, column = 3)
Label(L10, text = ' Result ').grid(row = 0, column = 4)
Label(L10, text = ' 14 ').grid(row = 1, column = 4)
#Label(L10, text = '  12  ').grid(row = 0, column = 7)






GUI.mainloop()

