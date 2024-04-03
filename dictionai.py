#importing library
from tkinter import *
from tkinter import Tk, Label
from PIL import ImageTk, Image
import time


w=Tk()
w.title('DictionAI')
image = ImageTk.PhotoImage(Image.open('ai.png'))

#show icon on window
icon = PhotoImage(file='icon.png')
w.iconphoto(False,icon)


width_of_window = 600
height_of_window = 520
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

w.overrideredirect(1) #for hiding titlebar




Frame(w, width=600, height=520, bg='lavender').place(x=0,y=0)

bg_label = Label(w, image= image, bg = 'lavender')
bg_label.place(x = 45, y =-15)



label=Label(w, text='Loading...',  fg='black',  bg="lavender") #decorate it
label.configure(font=("Times New Roman", 16,"bold"))
label.place(x=50,y=450)

#making animation

image_a=ImageTk.PhotoImage(Image.open('circle2.png'))
image_b=ImageTk.PhotoImage(Image.open('circle1.png'))




for i in range(3): #3 loops
    l1=Label(w, image=image_a, borderwidth=0, relief=SUNKEN).place(x=270, y=370)
    l2=Label(w, image=image_b, borderwidth=0, relief=SUNKEN).place(x=290, y=370)
    l3=Label(w, image=image_b, borderwidth=0, relief=SUNKEN).place(x=310, y=370)
    l4=Label(w, image=image_b, borderwidth=0, relief=SUNKEN).place(x=330, y=370)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=270, y=370)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=290, y=370)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=310, y=370)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=330, y=370)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=270, y=370)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=290, y=370)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=310, y=370)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=330, y=370)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=270, y=370)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=290, y=370)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=310, y=370)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=330, y=370)
    w.update_idletasks()
    time.sleep(0.5)


#Front Page
def fp():
    root = Tk()
    root.title('Home')
    root.minsize(600, 520)
    root.config(bg='#333333')

    # show icon on window
    icon = PhotoImage(file='icon.png')
    root.iconphoto(False, icon)

    def engdictPage():
        root.destroy()
        import englishdict

    def bandictPage():
        root.destroy()
        import bangladict


    # QUERY
    querylabel = Label(root, text='Which language do you prefer?', bg='#333333', fg='white', font=('Times New Roman', 20, 'bold'))
    querylabel.place(x=100, y=100)





    img_btn=Image.open(r"engdictionary.png")
    img_btn=img_btn.resize((156,156),Image.Resampling.LANCZOS)
    img=ImageTk.PhotoImage(img_btn)


    #dictionary button
    imgb1=Button(root,image=img,cursor="hand2",command=engdictPage,activebackground='#333333',bg="#333333",border=0,borderwidth=0)
    imgb1.place(x=125,y=150,width=180,height=180)


    img_btn1=Image.open(r"bangladictionary.png")
    img_btn1=img_btn1.resize((156,156),Image.Resampling.LANCZOS)
    img1=ImageTk.PhotoImage(img_btn1)


    #chatbot button
    imgb2=Button(root,image=img1,command=bandictPage,cursor="hand2",activebackground='#333333',bg="#333333",border=0)
    imgb2.place(x=275,y=150,width=180,height=180)



    root.mainloop()


w.destroy()
fp()
w.mainloop()


