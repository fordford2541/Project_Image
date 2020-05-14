from tkinter import *
from tkinter import ttk


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

# Beam Textbox
L00 = ttk.Label(GUI)
L00.grid(row = 0, column = 0, rowspan = 2)

L10 = ttk.Label(GUI)
L10.grid(row = 0, column = 1, rowspan = 2)

L20 = ttk.Label(GUI)
L20.grid(row = 0, column = 2, rowspan = 2)

Label(L00, text = 'Select floor').grid(row = 0, column = 0)
Button(L00, text = '1 Floor', width = '12').grid(row = 1, column = 0)
Button(L00, text = '2 Floor', width = '12').grid(row = 2, column = 0)
Button(L00, text = '3 Floor', width = '12').grid(row = 3, column = 0)
Label(L00, text = ' ').grid(row = 4, column = 0)
Label(L00, text = ' ').grid(row = 5, column = 0)
Label(L00, text = ' ').grid(row = 6, column = 0)
Label(L00, text = ' ').grid(row = 7, column = 0)
Label(L00, text = ' ').grid(row = 8, column = 0)
Label(L00, text = ' ').grid(row = 9, column = 0)
Label(L00, text = ' ').grid(row = 10, column = 0)
Label(L00, text = ' ').grid(row = 11, column = 0)
Label(L00, text = ' ').grid(row = 12, column = 0)

Button(L10, text = '1', height = '8', width = '30').grid(row = 0, column = 0)
Button(L10, text = '1', height = '8', width = '30').grid(row = 0, column = 1)
Button(L10, text = '1', height = '8', width = '30').grid(row = 0, column = 2)
Button(L10, text = '1', height = '8', width = '30').grid(row = 1, column = 0)
Button(L10, text = '1', height = '8', width = '30').grid(row = 1, column = 1)
Button(L10, text = '1', height = '8', width = '30').grid(row = 1, column = 2)

Button(L20, text = 'Count Car', width = '15').grid(row = 0, column = 0)
Button(L20, text = 'Count License', width = '15').grid(row = 1, column = 0)


Label(L20, text = 'Detecting').grid(row = 3, column = 0)
Label(L20, text = '11').grid(row = 4, column = 0)
Label(L20, text = 'Car').grid(row = 5, column = 0)
Label(L20, text = ' ').grid(row = 6, column = 0)
Label(L20, text = 'Detecting').grid(row = 7, column = 0)
Label(L20, text = '12').grid(row = 8, column = 0)
Label(L20, text = 'License').grid(row = 9, column = 0)
Label(L20, text = ' ').grid(row = 10, column = 0)
Label(L20, text = 'Result').grid(row = 11, column = 0)
Label(L20, text = '11').grid(row = 12, column = 0)
Label(L20, text = 'Car').grid(row = 13, column = 0)


GUI.mainloop()

