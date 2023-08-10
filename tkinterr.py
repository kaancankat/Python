import tkinter

window =tkinter.Tk()
window.title("python Tkinter")
window.minsize(width=450, height=300)

#label
my_label = tkinter.Label(text="deneme")
my_label.config(bg="black",fg="white")
my_label.pack()

def click_button():
    user_input=my_entry.get()
    print(user_input)

#button
my_button = tkinter.Button(text="this is a button", command=click_button)
my_button.pack()


my_entry = tkinter.Entry(width=20)
my_entry.pack()


window.mainloop()
