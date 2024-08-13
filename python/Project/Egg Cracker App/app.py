from tkinter import *
from tkinter import messagebox


def app():
    # Initialize the count variable
    global count
    count = 0

    def message():
        global count
        answer = messagebox.askyesno(message="Want to crack another egg?")
        if answer:  # User clicked 'Yes'
            count = 0
            button.config(state="normal", image=egg1)
        else:  # User clicked 'No'
            window.destroy()
            print("Goodbye!")
            
    def increase_count():
        global count
        count += 1
        # label.config(text=f"Count: {count}")
        if count == 3:
            # label.config(text=f"Count: {count} (The egg has cracked a bit!)")
            button.config(image=egg2)
        elif count == 5:
            # label.config(text=f"Count: {count} (The egg has cracked a bit!)")
            button.config(image=egg3)
        elif count == 8:
            # label.config(text=f"Count: {count} (The egg has cracked a bit!)")
            button.config(image=egg4)
        elif count == 10:
            # label.config(text=f"Count: {count} (The egg is cracked!)", fg="red")
            button.config(image=egg5, state=DISABLED)
            messagebox.showinfo(title = "Egg Cracked!!", message = "Egg Cracked!!")
            message()


    window = Tk()

    egg1 = PhotoImage(file='egg1.png')
    egg2 = PhotoImage(file='egg2.png')
    egg3 = PhotoImage(file='egg3.png')
    egg4 = PhotoImage(file='egg4.png')
    egg5 = PhotoImage(file='egg5.png')

    WIDTH = 330
    HEIGHT = 350
    window.geometry(f"{WIDTH}x{HEIGHT}")
    window.resizable(False, False)
    window.title("Egg Cracker App")
    window.config(bg="#d8ffdf")

    # label = Label(window,
    #               text=f"Count: {count}",
    #               fg='blue',
    #               bg="#d8ffdf",
    #               font=("Times", 15))
    # label.pack(pady=10)

    button = Button(window, text="Increase Count",
                    command=increase_count,
                    borderwidth=0,
                    highlightthickness=0,
                    border=None,
                    image=egg1, 
                    bg="#d8ffdf",
                    fg='red',
                    activebackground="#d8ffdf",
                    state="normal")

    button.pack()

    window.mainloop()