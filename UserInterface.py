import TweepyV6
from tkinter import *
from PIL import ImageTk,Image



    
def splash(:)
    def windowOne():
        windowA = Toplevel(root)
        windowA.title('Configure and Upload Video')
        windowA.iconbitmap('UIData/logo.ico')
        windowA.geometry('400x400')
        windowA.resizable(False, False)


        checkboxes = {}
    
        tndList = list()
        #varList = list[var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,
                       #var12,var13,var14,var15]
        tbl = TweepyV6.findTrends()
        
        for i in range(0,15):
            name = tbl[i]
            currentVar = IntVar()
            nowBox = Checkbutton(windowA, text=name,
                        variable = currentVar
                        )
            nowBox.var = currentVar
            nowBox.grid(row=i)
            checkboxes[nowBox] = name

        def buttonCheck():    
            output = []
            for box in checkboxes:
                if box.var.get() == 1:
                    output.append(checkboxes[box])
            print(output)
            return output




        publishA = Button(windowA,borderwidth = 0.6,
            activebackground = 'grey',
            height = 2,
            font =('Courier', 8),
            text = 'Upload Video!',
            command=lambda: TweepyV6.getTweets(buttonCheck()),
           ).grid(row = 7,column = 1,rowspan = 2)

        
            
        
    def windowTwo():
        windowB = Toplevel(root)
        windowB.title('Schedule Automated Video Upload')
        windowB.iconbitmap('UIData/logo.ico')
        windowB.geometry('400x400')
        windowB.resizable(False, False)
    def windowThree():
        windowC = Toplevel(root)
        windowC.title('Customize Video')
        windowC.iconbitmap('UIData/logo.ico')
        windowC.geometry('400x400')
        windowC.resizable(False, False)


            
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
                text = 'Configure and Upload Video',
                command = windowOne)
    bB = Button(root,borderwidth = 0.6,
                activebackground = 'grey',
                height = 5,
                font =('Courier', 8),
                text = 'Schedule Automated Video Upload',
                command = windowTwo)
    bC = Button(root,borderwidth = 0.6,
                activebackground = 'grey',
                height = 5,
                font =('Courier', 8),
                text = 'Customize Video',
                command = windowThree)
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

    
    mainloop()




splashRoot = Tk()
splashRoot.geometry('400x400')
splashRoot.overrideredirect(True)
splashRoot.iconbitmap('UIData/logo.ico')

splashLogo = ImageTk.PhotoImage(Image.open('UIData/Logopng.png'))


spashImage = Label(image=splashLogo)
spashImage.place(x=0,y=0,relwidth=1,relheight=1)




splashRoot.after(2000,splash)

mainloop()
