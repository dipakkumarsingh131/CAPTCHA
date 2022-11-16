from tkinter import *
from PIL import Image, ImageTk          #LIB TO IMPORT IMAGE
from random import *                              #RANDOM LIB TO IMP ALL MODULES


img_opt={1:"bird",6:"cake",11:"road"}               #DICT FOR CONTAINING IMAGES
random_number=randrange(1,16,5)                             #GENERATE RANDOM NO BETWEEN 1-16
img_ran={ 1:"b1.jpg", 2:"b2.jpg", 3:"b3.jpg", 4:"b4.jpg", 5:"b5.jpg", 6:"c1.jpg", 7:"c2.jpg", 8:"c3.jpg", 9:"c4.jpg", 10:"c5.jpg", 11:"r1.jpg", 12:"r2.jpg",13:"r3.jpg", 14:"r4.jpg", 15:"r5.jpg" }
img_1=randrange(1,16,1)                           #RANDOM NUMBER OF Img_MAGE FROM
img_2=randrange(1,16,1)
img_3=randrange(1,16,1)
img_4=randrange(1,16,1)
img_5=randrange(1,16,1)
img_6=randrange(1,16,1)
img_7=randrange(1,16,1)
img_8=randrange(1,16,1)
img_9=randrange(1,16,1)
img_S=[img_1,img_2,img_3,img_4,img_5,img_6,img_7,img_8,img_9]           #LImg_ST OF ALL SELECTED RANDOM NUMBER
img_T=[]                                               #EMPTY LIST TO STORE CORRECT OPTION



#ADDING CORRECT OPTION ACCORDING TO CATEGORIES IN DIFFERENCE OF 5
for x in range(9):
    if (img_S[x]==random_number or img_S[x]==random_number+1 or img_S[x]==random_number+2 or img_S[x]==random_number+3 or img_S[x]==random_number+4 ):
        img_T.append(img_S[x])


#HEADING
root= Tk()
root.title("Image Captcha Verification")
_l1=Label(root,text="Select all images which contain a "+img_opt[random_number] , relief = SUNKEN  , font = "Helvetca 20 bold ")
_l1.grid(row=0,columnspan=3)

img = ImageTk.PhotoImage(Image.open(img_ran[img_1]))
imglabel1 = Label(root,image=img,bg="black", width=150, height=150)
imglabel1.grid(row=1, column=0)

img1 = ImageTk.PhotoImage(Image.open(img_ran[img_2]))
imglabel2 = Label(root,image=img1, bg="black", width=150, height=150)
imglabel2.grid(row=1, column=1)

img2 = ImageTk.PhotoImage(Image.open(img_ran[img_3]))
imglabel3 = Label(root, image=img2, bg="black", width=150, height=150)
imglabel3.grid(row=1, column=2)

img3 = ImageTk.PhotoImage(Image.open(img_ran[img_4]))
imglabel4 = Label(root, image=img3, bg="black", width=150, height=150)
imglabel4.grid(row=2, column=0)

img4 = ImageTk.PhotoImage(Image.open(img_ran[img_5]))
imglabel5 = Label(root, image=img4, bg="black", width=150, height=150)
imglabel5.grid(row=2, column=1)

img5 = ImageTk.PhotoImage(Image.open(img_ran[img_6]))
imglabel6 = Label(root, image=img5, bg="black", width=150, height=150)
imglabel6.grid(row=2, column=2)

img6 = ImageTk.PhotoImage(Image.open(img_ran[img_7]))
imglabel7 = Label(root, image=img6, bg="black", width=150, height=150)
imglabel7.grid(row=3, column=0)

img7 = ImageTk.PhotoImage(Image.open(img_ran[img_8]))
imglabel8 = Label(root, image=img7, bg="black", width=150, height=150)
imglabel8.grid(row=3, column=1)

img8 = ImageTk.PhotoImage(Image.open(img_ran[img_9]))
imglabel9 = Label(root, image=img8, bg="black", width=150, height=150)
imglabel9.grid(row=3, column=2)

#CREATING VARIABLE 
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()

#AND BUTTON
c1=Checkbutton(root,variable=var1,highlightthickness=0,bd=0,offvalue=0,onvalue=img_1)
c1.grid(row=1,column=0)


c2=Checkbutton(root,variable=var2,highlightthickness=0,bd=0,offvalue=0,onvalue=img_2)
c2.grid(row=1,column=1)


c3=Checkbutton(root, variable=var3,highlightthickness=0,bd=0,offvalue=0,onvalue=img_3)
c3.grid(row=1, column=2)

c4=Checkbutton(root, variable=var4,highlightthickness=0,bd=0,offvalue=0,onvalue=img_4)
c4.grid(row=2, column=0)

c5=Checkbutton(root, variable=var5,highlightthickness=0,bd=0,offvalue=0,onvalue=img_5)
c5.grid(row=2, column=1)

c6=Checkbutton(root, variable=var6,highlightthickness=0,bd=0,offvalue=0,onvalue=img_6)
c6.grid(row=2, column=2)

c7=Checkbutton(root, variable=var7,highlightthickness=0,bd=0,offvalue=0,onvalue=img_7)
c7.grid(row=3, column=0)

c8=Checkbutton(root, variable=var8,highlightthickness=0,bd=0,offvalue=0,onvalue=img_8)
c8.grid(row=3, column=1)

c9=Checkbutton(root, variable=var9,highlightthickness=0,bd=0,offvalue=0,onvalue=img_9)
c9.grid(row=3, column=2)


#FUNCTION TO VERIFY CAPTCHA
def verifyCaptcha():
    l_var=[var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get(),var9.get()]
    correctList=[]
    userOpted=[]
    for i in range(9):
        if(l_var[i]!=0):
            userOpted.append(l_var[i])
            if(l_var[i] in img_T):
                correctList.append(l_var[i])

    if(len(correctList)==len(img_T)==len(userOpted)):
        imglabel1.destroy()
        c1.destroy()
        imglabel2.destroy()
        c2.destroy()
        imglabel3.destroy()
        c3.destroy()
        imglabel4.destroy()
        c4.destroy()
        imglabel5.destroy()
        c5.destroy()
        imglabel6.destroy()
        c6.destroy()
        imglabel7.destroy()
        c7.destroy()
        imglabel8.destroy()
        c8.destroy()
        imglabel9.destroy()
        c9.destroy()
        la=Label(root,text="Captcha Verified!",width=25,height=10  ,fg="green" , font = "Helvetca 20 bold" ) 
        la.grid(row=1,column=1)
        button.destroy()
        _l1.destroy()
    else:
        imglabel1.destroy()
        c1.destroy()
        imglabel2.destroy()
        c2.destroy()
        imglabel3.destroy()
        c3.destroy()
        imglabel4.destroy()
        c4.destroy()
        imglabel5.destroy()
        c5.destroy()
        imglabel6.destroy()
        c6.destroy()
        imglabel7.destroy()
        c7.destroy()
        imglabel8.destroy()
        c8.destroy()
        imglabel9.destroy()
        c9.destroy()
        lb=Label(root,text="Uh Oh! Captcha Mismatch! Try Again!",fg="red",width=45,height=10  , font = "Helvetca 20 bold" )
        lb.grid(row=1,column=1)
        button.destroy()
        _l1.destroy()
        
    
button=Button(root,width=15,height=3,bd=5, bg="blue"  ,fg="white",text="Verify",command=verifyCaptcha)
button.grid(row=4,column=1)
