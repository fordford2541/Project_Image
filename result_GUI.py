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
L00.grid(row = 0, column = 0)

L10 = ttk.Label(GUI)
L10.grid(row = 1, column = 0)

L20 = ttk.Label(GUI)
L20.grid(row = 2, column = 0)

L30 = ttk.Label(GUI)
L30.grid(row = 3, column = 0)

L40 = ttk.Label(GUI)
L40.grid(row = 4, column = 0)

Label(L00, text = 'Datasheet').grid(row = 0, column = 0)

Label(L10, text = '  1 Floor  ').grid(row = 0, column = 0)
Button(L10, text = ' ', width = '15').grid(row = 0, column = 1)
Button(L10, text = ' ', width = '15').grid(row = 0, column = 2)
Button(L10, text = ' ', width = '15').grid(row = 0, column = 3)
Button(L10, text = ' ', width = '15').grid(row = 0, column = 4)
Button(L10, text = ' ', width = '15').grid(row = 0, column = 5)
Button(L10, text = ' ', width = '15').grid(row = 0, column = 6)
Label(L10, text = '  12  ').grid(row = 0, column = 7)

Label(L20, text = '  2 Floor  ').grid(row = 1, column = 0)
Button(L20, text = ' ', width = '15').grid(row = 1, column = 1)
Button(L20, text = ' ', width = '15').grid(row = 1, column = 2)
Button(L20, text = ' ', width = '15').grid(row = 1, column = 3)
Button(L20, text = ' ', width = '15').grid(row = 1, column = 4)
Button(L20, text = ' ', width = '15').grid(row = 1, column = 5)
Button(L20, text = ' ', width = '15').grid(row = 1, column = 6)
Label(L20, text = '  11  ').grid(row = 1, column = 7)

Label(L30, text = '  3 Floor  ').grid(row = 2, column = 0)
Button(L30, text = ' ', width = '15').grid(row = 2, column = 1)
Button(L30, text = ' ', width = '15').grid(row = 2, column = 2)
Button(L30, text = ' ', width = '15').grid(row = 2, column = 3)
Button(L30, text = ' ', width = '15').grid(row = 2, column = 4)
Button(L30, text = ' ', width = '15').grid(row = 2, column = 5)
Button(L30, text = ' ', width = '15').grid(row = 2, column = 6)
Label(L30, text = '  15  ').grid(row = 2, column = 7)

Label(L40, text = 'Result 38').pack(fill = X)



GUI.mainloop()

