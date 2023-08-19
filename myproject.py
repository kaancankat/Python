from tkinter import *


list1=[]
#window
window = Tk()
window.title=("vücut index programı")
window.minsize(width=500,height=500)

#label
my_label=Label(text="kilonuzu girin")
my_label.config(fg="black")
my_label.config(font='Arial')
my_label.config(padx=50,pady=50)
my_label.pack()


#entry
#def my_entryselected():
#    print(my_entry.get())



my_entry2=Entry(width=20)
my_entry2.focus()
my_entry2.pack()


my_label=Label(text="boyunuzu girin")
my_label.config(fg="black")
my_label.config(font='Arial')
my_label.config(padx=50,pady=50)
my_label.pack()


my_entry=Entry(width=20)
my_entry.pack()

sonuclabel= Label(text=int(global(kitleindex)), font="ariel")
sonuclabel.config(pady=20)
sonuclabel.pack()

def buttonclicked():
    boy = int(my_entry.get())
    kilo = int(my_entry2.get())    
    
    if boy and kilo != int:
        print("lütfen sayı giriniz")
    
    
        
    kitleindex= kilo**2 / boy
    print(int(kitleindex)) 

    

#button
my_button=Button(text="hesapla",command=buttonclicked)
my_button.config(width=10,font="ariel")
my_button.config(padx=10,pady=10)
my_button.pack()



window.mainloop()

