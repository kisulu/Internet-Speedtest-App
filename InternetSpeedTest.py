from tkinter import *
try:
    import speedtest
except:
    print("import speedtest Not Available")

root = Tk()
root.title("Internet Speed Test")
root.geometry("280x500")
root.resizable(False, False)
root.configure(bg="#1a212d")

def Check():
    test=speedtest.Speedtest()
    Uploading=round(test.upload()/(1024*1024),2)
    upload.config(text=Uploading)
    #print(Uploading)

    downloading=round(test.download()/(1024*1024),2)
    download.config(text=downloading)
    Download.config(text=downloading)
    #print(downloading)

    servernames=[]
    test.get_servers(servernames)
    ping.config(text=test.results.ping)
    #print(test.results.ping)

# icon
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

# images
top = PhotoImage(file="top.png")
Label(root, image=top, bg="#1a212d").pack()

Main = PhotoImage(file="Main.png")
Label(root, image=Main, bg="#1a212d").pack(pady=(40,0))

button =PhotoImage(file="button.png")
Button = Button(root, image=button, bg="#1a212d", bd=0, activebackground="#1a212d", cursor="hand2", command=Check)
Button.pack(pady=10)

Label(root, text="PING", font="arial 6 bold", bg="#384056").place(x=35,y=0)
Label(root, text="DOWNLOAD", font="arial 6 bold", bg="#384056").place(x=120,y=0)
Label(root, text="UPLOAD", font="arial 6 bold", bg="#384056").place(x=220,y=0)

Label(root, text="MS", font="arial 7 bold", bg="#384056", fg="white").place(x=40,y=75)
Label(root, text="MBPS", font="arial 7 bold", bg="#384056", fg="white").place(x=125,y=75)
Label(root, text="MBPS", font="arial 7 bold", bg="#384056", fg="white").place(x=215,y=75)


Label(root, text="Download", font="arial 15 bold", bg="#384056", fg="white").place(x=105,y=240)
Label(root, text="MBPS", font="arial 15 bold", bg="#384056", fg="white").place(x=120,y=340)

ping = Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
ping.place(x=50,y=50, anchor="center")

download = Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
download.place(x=140,y=50, anchor="center")

upload = Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
upload.place(x=232,y=50, anchor="center")

Download = Label(root, text="00", font="arial 40 bold", bg="#384056")
Download.place(x=155,y=300, anchor="center")


mainloop()
