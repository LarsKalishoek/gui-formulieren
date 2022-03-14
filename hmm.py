import tkinter


#making the first window and giving the players name
def window1():
    window1 = tkinter.Tk()
    window1.title("KYS")
    window1.geometry("400x300")
    label1 = tkinter.Label(
        window1,
        text = "Welcome, what is your name"
        ) 
    label1.pack()
    label1.place(anchor="n",x = "200", y = "50")
    entry1 = tkinter.Entry(
        window1,
        width= 20,
    	)
    entry1.pack()
    entry1.place(anchor= "n", x = "200", y = "75")
    button1 = tkinter.Button(
        window1,
        text = "Start the game ",
        command = lambda:[window1.destroy(), window2()]
        
    )
    button1.pack()
    button1.place(anchor= "n", x = "200", y = "100")
    window1.mainloop()

#making the 2nd window
def window2():
    window2 = tkinter.Tk()
    window2.title("KYS")
    window2.geometry("400x300")
    label = tkinter.Label(
        window2,
        text = "Welcome to KYS a game about dying,",
    )
    label.place(anchor= "n", x = "200", y = "25")
    label2 = tkinter.Label(
        window2,
        text = "ALL your choices have an impact on the game, so choose WISELY",
    )
    label2.place(anchor= "n", x = "200", y = "45")
    label3 = tkinter.Label(
        window2,
        text = "So your first option is.."
    )
    label3.place(anchor= "n", x = "200", y = "75")
    label4 = tkinter.Label(
        window2,
        text = ""
    )
    button1 = tkinter.Button(
        window2,
        text = "penis"
    )
    button1.place(anchor= "n", x = "100", y = "175")
    button2 = tkinter.Button(
        window2,
        text = "penis"
    )
    button2.place(anchor= "n", x = "300", y = "175")
window1()
