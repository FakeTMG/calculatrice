from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root=Tk()
style=ttk.Style()
style.theme_use("classic")
style.map("Info.TButton", background=[('disabled', '#6d1b1b')])


def set_text(text):
    Ncalcul.insert(END,text)
    return

style=ttk.Style()
style.configure('TButton', foreground='#fc0c0c', font=('Arial',18))

Ncalcul=ttk.Entry(root,font=('Arial', 20, 'bold'))
Ncalcul.grid(row=0, column=0, columnspan=5, pady=10,ipadx=70,ipady=10)

bu1=ttk.Button(root,text='%',command=lambda:[set_text(" % "),ButtonClick(1)])
bu1.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)

bu2=ttk.Button(root,text='power',command=lambda:[set_text(" ** "),ButtonClick(2)])
bu2.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)

bu3=ttk.Button(root,text='C',command=lambda:Ncalcul.delete(0,END))
bu3.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)

bu4=ttk.Button(root,text='Del',command=lambda:Ncalcul.delete(len(Ncalcul.get())-1))
bu4.grid(row=1,column=3,sticky='snew',ipadx=40,ipady=40)

bu5=ttk.Button(root,text='7',command=lambda:set_text("7"))
bu5.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)

bu6=ttk.Button(root,text='8',command=lambda:set_text("8"))
bu6.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)

bu7=ttk.Button(root,text='9',command=lambda:set_text("9"))
bu7.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)

bu8=ttk.Button(root,text='X',command=lambda:[set_text(" * "),ButtonClick(8)])
bu8.grid(row=2,column=3,sticky='snew',ipadx=40,ipady=40)

bu9=ttk.Button(root,text='4',command=lambda:set_text("4"))
bu9.grid(row=3,column=0,sticky='snew',ipadx=40,ipady=40)

bu10=ttk.Button(root,text='5',command=lambda:set_text("5"))
bu10.grid(row=3,column=1,sticky='snew',ipadx=40,ipady=40)

bu11=ttk.Button(root,text='6',command=lambda:set_text("6"))
bu11.grid(row=3,column=2,sticky='snew',ipadx=40,ipady=40)

bu12=ttk.Button(root,text='-',command=lambda:[set_text(" - "),ButtonClick(12)])
bu12.grid(row=3,column=3,sticky='snew',ipadx=40,ipady=40)

bu13=ttk.Button(root,text='1',command=lambda:set_text("1"))
bu13.grid(row=4,column=0,sticky='snew',ipadx=40,ipady=40)

bu14=ttk.Button(root,text='2',command=lambda:set_text("2"))
bu14.grid(row=4,column=1,sticky='snew',ipadx=40,ipady=40)

bu15=ttk.Button(root,text='3',command=lambda:set_text("3"))
bu15.grid(row=4,column=2,sticky='snew',ipadx=40,ipady=40)

bu16=ttk.Button(root,text='+',command=lambda:[set_text(" + "),ButtonClick(16)])
bu16.grid(row=4,column=3,sticky='snew',ipadx=40,ipady=40)

bu17=ttk.Button(root,text='/',command=lambda:[set_text(" / "),ButtonClick(17)])
bu17.grid(row=5,column=0,sticky='snew',ipadx=40,ipady=40)

bu18=ttk.Button(root,text='0',command=lambda:set_text("0"))
bu18.grid(row=5,column=1,sticky='snew',ipadx=40,ipady=40)

bu19=ttk.Button(root,text='.',command=lambda:set_text("."))
bu19.grid(row=5,column=2,sticky='snew',ipadx=40,ipady=40)

buS=ttk.Button(root,text='=',command=lambda:GetTheNumbers())
buS.grid(row=5,column=3,sticky='snew',ipadx=40,ipady=40)

def findElements(lst1, lst2):
    return [lst1[i] for i in lst2]


def GetTheNumbers():
    try:
        punctuations = '*/-%+'
        my_str = Ncalcul.get()
        no_punct = ""
        for char in my_str:
            if char not in punctuations:
                no_punct = no_punct + char
        print(no_punct)
        selem = no_punct.split()
        print(selem)
        list_of_floats = []
        for item in selem:
            list_of_floats.append(float(item))
        print(list_of_floats)
        lst2 = [0]
        lst3 = [1]
        number1 = findElements(list_of_floats, lst2)
        print(number1)
        number2 = findElements(list_of_floats, lst3)
        print(number2)
        zipped_lists = zip(number1, number2)
        if 1 in p1 or '%' in my_str:
            sum = [x % y for (x, y) in zipped_lists]
            messagebox.showinfo(title="Results",message=sum)
            p1.clear()
        elif 2 in p1 or '**' in my_str:
            sum = [x ** y for (x, y) in zipped_lists]
            messagebox.showinfo(title="Results",message=sum)
            p1.clear()
        elif 8 in p1 or '*' in my_str:
            sum = [x * y for (x, y) in zipped_lists]
            messagebox.showinfo(title="Results", message=sum)
            p1.clear()
        elif 12 in p1 or '-' in my_str:
            sum = [x - y for (x, y) in zipped_lists]
            messagebox.showinfo(title="Results", message=sum)
            p1.clear()
        elif 16 in p1 or '+' in my_str:
            sum = [x + y for (x, y) in zipped_lists]
            messagebox.showinfo(title="Results", message=sum)
            p1.clear()
        elif 17 in p1 or '/' in my_str:
            sum = [x / y for (x, y) in zipped_lists]
            messagebox.showinfo(title="Results", message=sum)
            p1.clear()
    except IndexError:
        messagebox.showinfo(title="Error", message="Please leave a space between each element.")
    except ValueError:
        messagebox.showinfo(title="Error", message="You can't use a comma please change it with a point.")
    Ncalcul.delete(0,END)


p1=[]
def ButtonClick(id):
    p1.append(id)
    print("p1:{}".format(p1))

root.mainloop()
