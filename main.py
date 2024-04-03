from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self, root):  
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
 
 #first
        img = Image.open(r"C:\Users\Manvi\Desktop\RProject\Camera based attendance-python\assets\college.jpeg")
        img = img.resize((500,200))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=200)
#second
        img1 = Image.open(r"C:\Users\Manvi\Desktop\RProject\Camera based attendance-python\assets\scan.jpeg")
        img1 = img1.resize((500,200))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=200)
#third
        img2 = Image.open(r"C:\Users\Manvi\Desktop\RProject\Camera based attendance-python\assets\college2.jpeg")
        img2 = img2.resize((500,200))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=550, height=200)
#bg
        img3 = Image.open(r"C:\Users\Manvi\Desktop\RProject\Camera based attendance-python\assets\img3-bg.jpeg")
        img3 = img3.resize((1530,710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=50)
#student button
        img4 = Image.open(r"C:\Users\Manvi\Desktop\RProject\Camera based attendance-python\assets\studentButton.jpeg")
        img4 = img4.resize((280,220))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=280,height=220)

        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=300,width=280,height=40)
#Detect face button
        img5 = Image.open(r"C:\Users\Manvi\Desktop\RProject\Camera based attendance-python\assets\faceDetector.jpeg")
        img5 = img5.resize((280,220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=280,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=300,width=280,height=40)
#Attendance face button
        img6 = Image.open(r"C:\Users\Manvi\Desktop\RProject\Camera based attendance-python\assets\attendance.jpeg")
        img6 = img6.resize((280,220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=280,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=800,y=300,width=280,height=40)
#Help desk button
        img7 = Image.open(r"C:\Users\Manvi\Desktop\RProject\Camera based attendance-python\assets\helpDesk.jpeg")
        img7 = img7.resize((280,220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=280,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1100,y=300,width=280,height=40)
#Train face button
        img8 = Image.open(r"C:\Users\Manvi\Desktop\RProject\Camera based attendance-python\assets\trainData.jpg")
        img8 = img8.resize((280,220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=380,width=280,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=550,width=280,height=40)
#Photos face button
        img9 = Image.open(r"C:\Users\Manvi\Desktop\RProject\Camera based attendance-python\assets\photos.jpeg")
        img9 = img9.resize((280,220))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=380,width=280,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=550,width=280,height=40)
#Developer face button
        img10 = Image.open(r"C:\Users\Manvi\Desktop\RProject\Camera based attendance-python\assets\developer.jpeg")
        img10 = img10.resize((280,220))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=500,y=380,width=280,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=550,width=280,height=40)








if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
