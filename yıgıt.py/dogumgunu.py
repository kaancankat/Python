import tkinter as tk
from tkinter import messagebox
import datetime

def kutlama_kontrol():
    dogum_gunu = datetime.date(2008,9,5)
    bugun = datetime.date.today()
    
    if bugun.month == dogum_gunu.month and bugun.day == dogum_gunu.day:
        messagebox.showinfo("Doğum Günü Kutlaması", "Doğum gününüz kutlu ve iyi günler")
    else:
        messagebox.showinfo("Doğum Günü Kutlaması", "Üzgünüm, doğum gününüz değil.")


root = tk.Tk()
root.title("Doğum Günü Kutlama Uygulaması")

kutla_buton = tk.Button(root, text="Doğum Gününü Kutla", command=kutlama_kontrol)
kutla_buton.pack(pady=20)

root.mainloop()