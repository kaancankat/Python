from tkinter import *

#window
window = Tk()
window.title("Vücut Index Programı")
window.minsize(width=500, height=500)

#label
my_label1 = Label(text="Kilonuzu girin")
my_label1.config(fg="black", font='Arial', padx=50, pady=10)
my_label1.pack()

my_entry2 = Entry(width=20)
my_entry2.focus()
my_entry2.pack()

my_label2 = Label(text="Boyunuzu girin")
my_label2.config(fg="black", font='Arial', padx=50, pady=10)
my_label2.pack()

my_entry = Entry(width=20)
my_entry.pack()

result_label = Label(text="", font="Arial")
result_label.config(pady=20)
result_label.pack()

def calculate_bmi():
    try:
        boy = float(my_entry.get())
        kilo = float(my_entry2.get())
        
        if boy <= 0 or kilo <= 0:
            result_label.config(text="Geçerli boy ve kilo girin")
            return
        
        kitle_index = kilo / (boy ** 2)
        result_label.config(text=f"Kitle İndeksi: {kitle_index:.2f}")
    except ValueError:
        result_label.config(text="Geçerli sayı girin")

#button
calculate_button = Button(text="Hesapla", command=calculate_bmi)
calculate_button.config(width=10, font="Arial", padx=10, pady=10)
calculate_button.pack()

window.mainloop()
