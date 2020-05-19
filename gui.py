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

f1p1 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_1.jpg"))
f1p2 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_2.jpg"))
f1p3 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_3.jpg"))
f1p4 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_4.jpg"))
f1p5 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_5.jpg"))
f1p6 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_6.jpg"))
f2p1 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_7.jpg"))
f2p2 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_8.jpg"))
f2p3 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_9.jpg"))
f2p4 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_10.jpg"))
f2p5 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_11.jpg"))
f2p6 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_12.jpg"))
f3p1 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_13.jpg"))
f3p2 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_14.jpg"))
f3p3 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_15.jpg"))
f3p4 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_16.jpg"))
f3p5 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_17.jpg"))
f3p6 = ImageTk.PhotoImage(Image.open("test photo/1080p/GUI/IMG_18.jpg"))

rrr = ImageTk.PhotoImage(Image.open("GUI/rrr.jpg"))
grr = ImageTk.PhotoImage(Image.open("GUI/grr.jpg"))
rgr = ImageTk.PhotoImage(Image.open("GUI/rgr.jpg"))
rrg = ImageTk.PhotoImage(Image.open("GUI/rrg.jpg"))
ggr = ImageTk.PhotoImage(Image.open("GUI/ggr.jpg"))

# Beam Textbox
L00 = ttk.Label(GUI)
L00.grid(row = 0, column = 0)

L01 = ttk.Label(GUI)
L01.grid(row = 0, column = 1)

L10 = ttk.Label(GUI)
L10.grid(row = 1, column = 0, columnspan = 2)

L10 = ttk.Label(GUI)
L10.grid(row = 2, column = 0, columnspan = 2)

L20 = ttk.Label(GUI)
L20.grid(row = 3, column = 0, rowspan = 4)

L21 = ttk.Label(GUI)
L21.grid(row = 3, column = 1)

Button(L00, text = 'camera 1', height = '8', width = '33').grid(row = 0, column = 0)
Button(L00, text = 'camera 2', height = '8', width = '33').grid(row = 0, column = 1)
Button(L00, text = 'camera 3', height = '8', width = '33').grid(row = 0, column = 2)
Button(L00, text = 'camera 4', height = '8', width = '33').grid(row = 1, column = 0)
Button(L00, text = 'camera 5', height = '8', width = '33').grid(row = 1, column = 1)
Button(L00, text = 'camera 6', height = '8', width = '33').grid(row = 1, column = 2)
Label(L20, text = '           ').grid(row = 0, column = 0, rowspan = 2)

def floor1():
    Label(L00, image = f1p1, height = '270', width = '480').grid(row = 0, column = 0)
    Label(L00, image = f1p2, height = '270', width = '480').grid(row = 0, column = 1)
    Label(L00, image = f1p3, height = '270', width = '480').grid(row = 0, column = 2)
    Label(L00, image = f1p4, height = '270', width = '480').grid(row = 1, column = 0)
    Label(L00, image = f1p5, height = '270', width = '480').grid(row = 1, column = 1)
    Label(L00, image = f1p6, height = '270', width = '480').grid(row = 1, column = 2)
    Label(L21, text = '  1 Floor  ').grid(row = 1, column = 0)
    Button(L01, text = 'Count Car', command = count_floor1, width = '15').grid(row = 10, column = 0)
    
    Button(L20, text = ' ', width = '33').grid(row = 0, column = 0)
    Button(L20, text = ' ', width = '33').grid(row = 0, column = 1)
    Button(L20, text = ' ', width = '33').grid(row = 0, column = 2)
    Button(L20, text = ' ', width = '33').grid(row = 1, column = 0)
    Button(L20, text = ' ', width = '33').grid(row = 1, column = 1)
    Button(L20, text = ' ', width = '33').grid(row = 1, column = 2)

    Label(L21, text = '   ').grid(row = 3, column = 0)

def floor2():
    Label(L00, image = f2p1, height = '270', width = '480').grid(row = 0, column = 0)
    Label(L00, image = f2p2, height = '270', width = '480').grid(row = 0, column = 1)
    Label(L00, image = f2p3, height = '270', width = '480').grid(row = 0, column = 2)
    Label(L00, image = f2p4, height = '270', width = '480').grid(row = 1, column = 0)
    Label(L00, image = f2p5, height = '270', width = '480').grid(row = 1, column = 1)
    Label(L00, image = f2p6, height = '270', width = '480').grid(row = 1, column = 2) 
    Label(L21, text = '  2 Floor  ').grid(row = 1, column = 0)
    Button(L01, text = 'Count Car', command = count_floor2, width = '15').grid(row = 10, column = 0)
    
    Button(L20, text = ' ', width = '33').grid(row = 0, column = 0)
    Button(L20, text = ' ', width = '33').grid(row = 0, column = 1)
    Button(L20, text = ' ', width = '33').grid(row = 0, column = 2)
    Button(L20, text = ' ', width = '33').grid(row = 1, column = 0)
    Button(L20, text = ' ', width = '33').grid(row = 1, column = 1)
    Button(L20, text = ' ', width = '33').grid(row = 1, column = 2)

    Label(L21, text = '   ').grid(row = 3, column = 0)

def floor3():
    Label(L00, image = f3p1, height = '270', width = '480').grid(row = 0, column = 0)
    Label(L00, image = f3p2, height = '270', width = '480').grid(row = 0, column = 1)
    Label(L00, image = f3p3, height = '270', width = '480').grid(row = 0, column = 2)
    Label(L00, image = f3p4, height = '270', width = '480').grid(row = 1, column = 0)
    Label(L00, image = f3p5, height = '270', width = '480').grid(row = 1, column = 1)
    Label(L00, image = f3p6, height = '270', width = '480').grid(row = 1, column = 2) 
    Label(L21, text = '  3 Floor  ').grid(row = 1, column = 0)
    Button(L01, text = 'Count Car', command = count_floor3, width = '15').grid(row = 10, column = 0)
    
    Button(L20, text = ' ', width = '33').grid(row = 0, column = 0)
    Button(L20, text = ' ', width = '33').grid(row = 0, column = 1)
    Button(L20, text = ' ', width = '33').grid(row = 0, column = 2)
    Button(L20, text = ' ', width = '33').grid(row = 1, column = 0)
    Button(L20, text = ' ', width = '33').grid(row = 1, column = 1)
    Button(L20, text = ' ', width = '33').grid(row = 1, column = 2)

    Label(L21, text = '   ').grid(row = 3, column = 0)

def count_floor1():
    Label(L20, image = rrr, width = '480').grid(row = 0, column = 0)
    Label(L20, image = rgr, width = '480').grid(row = 0, column = 1)
    Label(L20, image = rrg, width = '480').grid(row = 0, column = 2)
    Label(L20, image = grr, width = '480').grid(row = 1, column = 0)
    Label(L20, image = rrr, width = '480').grid(row = 1, column = 1)
    Label(L20, image = rrr, width = '480').grid(row = 1, column = 2)

    Label(L21, text = '15').grid(row = 3, column = 0)
def count_floor2():
    Label(L20, image = rrr, width = '480').grid(row = 0, column = 0)
    Label(L20, image = rrr, width = '480').grid(row = 0, column = 1)
    Label(L20, image = grr, width = '480').grid(row = 0, column = 2)
    Label(L20, image = rrg, width = '480').grid(row = 1, column = 0)
    Label(L20, image = rrr, width = '480').grid(row = 1, column = 1)
    Label(L20, image = rrr, width = '480').grid(row = 1, column = 2)

    Label(L21, text = '16').grid(row = 3, column = 0)
def count_floor3():
    Label(L20, image = rrr, width = '480').grid(row = 0, column = 0)
    Label(L20, image = rgr, width = '480').grid(row = 0, column = 1)
    Label(L20, image = rrr, width = '480').grid(row = 0, column = 2)
    Label(L20, image = rrr, width = '480').grid(row = 1, column = 0)
    Label(L20, image = ggr, width = '480').grid(row = 1, column = 1)
    Label(L20, image = rrr, width = '480').grid(row = 1, column = 2)

    Label(L21, text = '15').grid(row = 3, column = 0)
total = StringVar()

Label(L01, text = 'Select floor').grid(row = 0, column = 0)
Button(L01, text = '1 Floor', width = '15', command=floor1).grid(row = 1, column = 0)
Button(L01, text = '2 Floor', width = '15', command=floor2).grid(row = 2, column = 0)
Button(L01, text = '3 Floor', width = '15', command=floor3).grid(row = 3, column = 0)
Label(L01, text = ' ').grid(row = 4, column = 0)
Label(L01, text = ' ').grid(row = 5, column = 0)
Label(L01, text = ' ').grid(row = 6, column = 0)
Label(L01, text = ' ').grid(row = 7, column = 0)
Label(L01, text = ' ').grid(row = 8, column = 0)
Label(L01, text = ' ').grid(row = 9, column = 0)
Label(L01, text = ' ').grid(row = 10, column = 0)

Label(L10, text = 'Result display').grid(row = 0, column = 0)


Button(L20, text = ' ', width = '33').grid(row = 0, column = 0)
Button(L20, text = ' ', width = '33').grid(row = 0, column = 1)
Button(L20, text = ' ', width = '33').grid(row = 0, column = 2)
Button(L20, text = ' ', width = '33').grid(row = 1, column = 0)
Button(L20, text = ' ', width = '33').grid(row = 1, column = 1)
Button(L20, text = ' ', width = '33').grid(row = 1, column = 2)

Label(L21, text = 'Choosing:').grid(row = 0, column = 0)
Label(L21, text = '   ').grid(row = 1, column = 0)
Label(L21, text = 'Total:').grid(row = 2, column = 0)
Label(L21, text = '   ').grid(row = 3, column = 0)




GUI.mainloop()

