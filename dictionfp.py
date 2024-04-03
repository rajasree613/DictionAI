from tkinter import *
from PIL import Image,ImageTk


def fp():
    root = Tk()
    root.title('Home')
    root.minsize(600, 520)
    root.config(bg='#333333')

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
fp()


