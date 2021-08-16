#import TweepyV5
from tkinter import *
from PIL import ImageTk,Image

def windowOne():
    newWindow = Toplevel(root):
        newWindow.title('Automated Twitter Content Milker')
        newWindow.geometry('400x400')
        newWindow.iconbitmap('UIData/logo.ico')


def splash():
    splashRoot.destroy()
    root = Tk()
    root.title('Automated Twitter Content Milker')
    root.iconbitmap('UIData/logo.ico')
    root.geometry('400x400')

    Copyr = ImageTk.PhotoImage(Image.open('UIData/Logopng.png'))

    header = Label(root, text = 'AUTOMATED TWITTER CONTENT MILKER',
                   font=("Courier", 14))
    #Copyrcool = Label(root, image=Copyr, height = 50, width = 50)
    bA = Button(root,borderwidth = 0.6,
                activebackground = 'grey',
                height = 5,
                font =('Courier', 8),
                text = 'Configure and Upload Video')
    bB = Button(root,borderwidth = 0.6,
                activebackground = 'grey',
                height = 5,
                font =('Courier', 8),
                text = 'Schedule Automated Video Upload')
    bC = Button(root,borderwidth = 0.6,
                activebackground = 'grey',
                height = 5,
                font =('Courier', 8),
                text = 'Customize Video')
    bD = Button(root,borderwidth = 0.6,
                activebackground = 'grey',
                height = 5,
                font =('Courier', 8),
                text = 'Exit Application',
                command=root.destroy)

    

    header.place(relx=0.5,rely=0.02,anchor='center',)
    bA.place(relx = 0.24,rely=0.25,anchor='center')
    bB.place(relx = 0.28,rely=0.46,anchor='center')
    bC.place(relx = 0.14,rely=0.68, anchor = 'center')
    bD.place(relx = 0.15,rely=0.9, anchor = 'center')
    #Copyrcool.place(relx=0,rely=0, anchor = 'se')

    root.resizable(False, False)     
    root.mainloop()



splashRoot = Tk()
splashRoot.geometry('400x400')
splashRoot.overrideredirect(True)
splashRoot.iconbitmap('UIData/logo.ico')

splashLogo = ImageTk.PhotoImage(Image.open('UIData/Logopng.png'))


spashImage = Label(image=splashLogo)
spashImage.place(x=0,y=0,relwidth=1,relheight=1)




splashRoot.after(2000,splash)

mainloop()
