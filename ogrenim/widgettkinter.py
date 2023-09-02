from tkinter import *

window = Tk()
window.title("tkinter python")
window.minsize(width=600,height=600)
window.config(padx=20,pady=20)

label=Label(text="my label")
label.config(bg="black")
label.config(fg="white")
label.config(padx=10,pady=10)
label.pack()

def button_clicked():
    print("button clicked")
    print(text.get("1.0",END))
    
Button= Button(text="button", command=button_clicked)
Button.config(padx=10,pady=10)
Button.pack()

Entry= Entry(width=20)
Entry.pack()

text=Text(width=20,height=5)
text.pack()

def scale_selected(value):
    print(value)

my_scale = Scale(from_= 0, to= 50,command=scale_selected)
my_scale.pack()

def check_selected():
    print(check_state.get())


check_state = IntVar()
my_checkbutton = Checkbutton(text="check",variable=check_state,command=check_selected)
my_checkbutton.pack()

def radioselected():
    print(radio_checkedstate.get())


radio_checkedstate= IntVar()
my_radiobutton= Radiobutton(text="1. option",value=10,variable=radio_checkedstate,command=radioselected)
my_radiobutton2=Radiobutton(text="2. option",value=20,variable=radio_checkedstate,command=radioselected)
my_radiobutton.pack()
my_radiobutton2.pack()

my_listbox= Listbox()
name_List = ["atıl","ABC","KJF"]
for i in range(len(name_List)):
    my_listbox.insert(i,name_List[i])
my_listbox.bind
my_listbox.pack()


window.mainloop()