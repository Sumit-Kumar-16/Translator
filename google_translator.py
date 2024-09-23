from cProfile import label
from cgitb import text
from tkinter import*
from tkinter import ttk
from turtle import title, width
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans = Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text


def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = sor_txt.get(1.0,END)
    textget = change(text = msg, src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)



root = Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg="silver")
lab_txt=Label(root,text="Translator",font=("Time New Roman",40,"bold",),bg="silver")
lab_txt.place(x=100,y=40,height=70,width=320)

frame = Frame(root).pack(side=BOTTOM)
lab_txt=Label(root,text="Source Text",font=("Time New Roman",20,"bold"),fg="Green",bg="silver")
lab_txt.place(x=100,y=110,height=20,width=300)

sor_txt =Text(frame,font=("Time New Roman",10,),wrap=WORD)
sor_txt.place(x=10,y=140,height=150,width=480)

list_text =list(LANGUAGES.values())

comb_sor=ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height=30,width=100)
comb_sor.set("English")

button_change=Button(frame,text="Translate",relief=RAISED, command=data)
button_change.place(x=130,y=300,height=30,width=100)


comb_dest=ttk.Combobox(frame,value=list_text)
comb_dest.place(x=250,y=300,height=30,width=100)
comb_dest.set("English")


lab_txt=Label(root,text="Destination Text",font=("Time New Roman",20,"bold"),fg="Green",bg="silver")
lab_txt.place(x=100,y=360,height=20,width=300)

dest_txt =Text(frame,font=("Time New Roman",10,),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)


root.mainloop()