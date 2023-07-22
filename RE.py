# version 4.0
# 1.Customizable Message
# 2.Importing from a CSV File
# 3.Browse File
# 4.GUI

# Import Module
from tkinter import *
from pywhatkit import *
from tkinter.filedialog import askopenfilename
import os

# create root window
root = Tk()
root.configure(bg='#A7FFE4',padx=10,pady=10)

# root window title and dimension
root.title("Welcome to RE WhatsApp Bulk Messenger")
# Set geometry(widthxheight)
root.geometry('400x300')

# adding a 1st label to the root window
lb1 = Label(root, text = "Phone Numbers: ",fg='#E1FFEE',bg='#FFA1CF')
lb1.grid(column =0, row =0,padx=10,pady=10)
#-------------------------------------------------------------------------
# adding 1st Entry Field
lb12 = Label(root, text = "",bg='#A7FFE4',fg='#E1FFEE')
lb12.grid(column =1, row =0,padx=10,pady=10)
# function to display user text when
# Browse button is clicked
def Browsed():
    global filename
    filename = askopenfilename()
    res= os.path.basename(filename).split('/')[-1]
    lb12.configure(text = res,bg='#FFA1CF')
    

# button widget with red color text inside
btn1 = Button(root, text = "Browse" ,fg = "red", command=Browsed)
# Set Button Grid
btn1.grid(column=2, row=0,padx=10,pady=10)

#-------------------------------------------------------------------------

# adding a 2nd label to the root window
lb2 = Label(root, text = "Enter the Message",fg='#E1FFEE',bg='#FFA1CF')
lb2.grid(column =0, row =1)

# adding 2nd Entry Field
txt2 = Entry(root, width=10)
txt2.grid(column =1, row =1,padx=10,pady=10)


#-------------------------------------------------------------------------
# function to display user text when
# Send Now button is clicked
def clicked():
    #b=open(filename,'r')
    #a=b.read()
    #c= a.split(',')
    c= ['8939691599','9150612802','8838914887','7358510307']
    h = len(c)   
    s1 = '+91'
    msg = txt2.get() 
    for i in c:    
        i = str(i)
        i = s1 + i   
        print(i)    
        sendwhatmsg_instantly(i,msg,10,True,2)   
    res = "Sucessfully Sent the Message: \n" + msg + "\nto " + str(h) + " People\n"
    lb3.configure(text = res)
    
        

# button widget with red color text inside
btn2 = Button(root, text = "Send Now" , fg = "red", command=clicked)
# Set Button Grid
btn2.grid(column=1, row=2)
#-------------------------------------------------------------------------

# adding a 3rd label to the root window
lb3 = Label(root, text = "",fg = "red",bg='#A7FFE4')
lb3.grid(column =0, row =3,padx=10,pady=10)

# adding a 4th label to the root window
lb4 = Label(root, text = "© Copyrights RE 2022. All rights reserved. Designed by Rephel",fg = "red")
lb4.grid(column =0, row =4,padx=10,pady=10,columnspan=4)
 

# Execute Tkinter
root.mainloop()
