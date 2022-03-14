import tkinter
window = tkinter.Tk()
window.title("Dambord")
window.geometry("940x940")
frame = tkinter.Frame(window)
z=1
for x in range(10):
    if z==0:
        z=1
    else:
        z=0
    for y in range(10):
        if z == 0:
            b="black"
            z=1
        else:
            b="white"
            z=0
        label = tkinter.Label(frame,padx=40.6,pady=30.7,bg=b).grid(row=y,column=x)
frame.pack(expand=True)
window.mainloop()