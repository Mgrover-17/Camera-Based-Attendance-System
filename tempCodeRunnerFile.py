img3 = Image.open(r"C:\Users\Manvi\Desktop\RProject\Camera based attendance-python\assets\background.jpeg")
        img3 = img3.resize((1530,710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)