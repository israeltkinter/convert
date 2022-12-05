import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from gtts import gTTS
import subprocess
import speech_recognition as sr
import pyaudio
import socket
import time
import win32api

########################################################################################################################
is_on = True



class Window3(tk.Tk):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("1980x1080")
        self.title("תוכנה")
########################################################################################################################
        self.my_menu = Menu(tearoff=False)
        self.my_menu.add_command(label="פתיחת סרטון ההמרה",command=self.open2,accelerator="Ctrl+O")
        self.my_menu.add_command(label="פתיחת מסמך ההמרה",command=self.open,accelerator="Ctrl+A")
        self.my_menu.add_command(label="פותר בעיות",accelerator="Ctrl+H",command=self.help)
        self.my_menu.add_separator()
        self.my_menu.add_command(label="שלח דואר",command=self.send_mail,accelerator="F5")
        self.my_menu.add_command(label="יציאה", command=self.destroy,accelerator="Ctrl+Q")

        self.bind("<Button-3>",self.my_poup)
        self.bindkeys()

#######################################################################################################################
        self.frame = tk.Frame(self, width=700, height=250, highlightbackground="black", highlightthickness=10)
        self.frame.place(x=250, y=200)
        self.frame2 = tk.Frame(self, width=700, height=300, highlightbackground="black", highlightthickness=10)
        self.frame2.place(x=250, y=500)
        self.show_edit1 = tk.BooleanVar()
        self.show_edit1.set(True)









        self.show_edit2 = tk.BooleanVar()
        self.show_edit2.set(True)

        self.my_menu2 = Menu(tearoff=False)
        self.file = Menu(self.my_menu2, tearoff=False)
        self.edit = Menu(self.my_menu2, tearoff=False)
        self.view = Menu(self.my_menu2, tearoff=False)
        self.help_1 = Menu(self.my_menu2, tearoff=False)
        self.file.add_command(label="פתיחת סרטון ההמרה",command=self.open2,accelerator="Ctrl+O")
        self.file.add_command(label="פתיחת מסמך ההמרה", command=self.open,accelerator="Ctrl+A")
        self.file.add_command(label="יציאה", command=lambda *args:self.destroy(),accelerator="Ctrl+Q")
        self.edit.add_checkbutton(label="טיפים",onvalue=True,offvalue="off",variable=self.show_edit1,command=self.show_type)
        self.edit.add_checkbutton(label="פתרונות אפשריים לשגיאות",onvalue=1,offvalue=False,variable=self.show_edit2,command=self.show_plan)




        self.view.add_radiobutton(label="כתום",command=self.orange,value="First opiton")
        self.view.add_radiobutton(label="שחור",command=self.black,value="Second opiton")
        self.view.add_radiobutton(label="סגול",command=self.purple,value="Third option")
        self.view.add_radiobutton(label="אדום",command=self.red,value=4)
        self.view.add_radiobutton(label="לבן",command=self.white,value=5)
        self.view.add_radiobutton(label="כחול",command=self.blue,value=6)
        self.view.add_radiobutton(label="ירוק",command=self.grin,value=7)

        self.help_1.add_command(label="פותר בעיות",accelerator="Ctrl+H",command=self.help)
        self.help_1.add_command(label="שלח דואר",accelerator="F5",command=self.send_mail)


        self.my_menu2.add_cascade(label="פתח",menu=self.file)
        self.my_menu2.add_cascade(label="הצג",menu=self.edit)
        self.my_menu2.add_cascade(label="רקע",menu=self.view)
        self.my_menu2.add_cascade(label="מתקדם",menu=self.help_1)

########################################################################################################################



        self.label1 = tk.Label(text="המרת טקסט לדיבור ולהפך",font=("Ariel",30,"bold"),fg="#414169")
        self.label1.grid(padx=800,pady=100)
        self.label2 = tk.Label(text="הכנס טקסט",font=("Ariel",20,"bold"),fg="#414169")
        self.label2.place(x=1500,y=250)
        self.label3 = tk.Label(text="שמירת ההמרה", font=("Ariel", 20, "bold"),fg="#414169")
        self.label3.place(x=1500, y=350)
        self.label4 = tk.Label(text="פתיחת סרטון ההמרה", font=("Ariel", 20, "bold"),fg="#414169")
        self.label4.place(x=1500, y=450)
        self.label5 = tk.Label(text="הקלט קול", font=("Ariel", 20, "bold"),fg="#414169")
        self.label5.place(x=1500, y=650)
        self.label6 = tk.Label(text="גודל ההמרה", font=("Ariel", 20, "bold"),fg="#414169")
        self.label6.place(x=1500, y=750)
        self.label7 = tk.Label(text="פתיחת מסמך ההמרה", font=("Ariel", 20, "bold"),fg="#414169",)
        self.label7.place(x=1500, y=850)
        self.label8 = tk.Label(text="פעיל",font=("Ariel", 20, "bold"),fg="#414169")
        self.label8.place(x=1200,y=340)
        self.label9 = tk.Label(self.frame,text="א. ניתן להכניס טקסט בשני השפות אבל לא ביחד",font=("Ariel", 15, "bold"),fg="#414169")
        self.label10 = tk.Label(self.frame,text="ב. כשמכניסים טקסט בשפה העברית כדאי להכניס מילים בודדות",font=("Ariel", 15, "bold"),fg="#414169")
        self.label11 = tk.Label(self.frame,text="ג. וכשמכניסים טקסט בשפה האנגלית אפשר להכניס משפטים שלמים",font=("Ariel", 15, "bold"),fg="#414169")
        self.label12 = tk.Label(self.frame,text="טיפים",font=("Ariel", 20, "bold"),fg="#414169")
        self.label9.place(x=20,y=50)
        self.label10.place(x=20, y=100)
        self.label11.place(x=20, y=150)
        self.label12.place(x=600,y=15)
        self.label13 = tk.Label(self.frame2, text="א. בהקלט קול בדקו אם המיקרופון שלכם עובד", font=("Ariel", 15, "bold"),
                          fg="#414169")
        self.label14 = tk.Label(self.frame2, text="ב. בדקו אם חיבור האינטרנט שלכם פעיל",
                           font=("Ariel", 15, "bold"), fg="#414169")
        self.label15 = tk.Label(self.frame2, text="ג. אם חלק מהטקסט לא מומר בדקו אם כתבתם בשני שפות ביחד",
                           font=("Ariel", 15, "bold"), fg="#414169")
        self.label16 = tk.Label(self.frame2, text="פתרונות אפשריים לשגיאות", font=("Ariel", 20, "bold"), fg="#414169")
        self.label17 = tk.Label(self.frame2, text="ד. בטקסט עדיף שתמירו בשפה האנגלית", font=("Ariel", 15, "bold"), fg="#414169")
        self.label13.place(x=20, y=50)
        self.label14.place(x=20, y=100)
        self.label15.place(x=20, y=150)
        self.label16.place(x=370, y=15)
        self.label17.place(x=20, y=200)

        self.configure = tk.StringVar(value="המרה לא התחילה")
        self.label18 = tk.Label(self,font=("Ariel", 15, "bold"), fg="#414169",textvariable=self.configure)
        self.label18.place(x=1200,y=650)






        self.entry1 = tk.Text(width=40,font=("Ariel",12,"bold"))
        self.entry1.place(x=1100,y=255,height=70)
        self.scrollbar = ttk.Scrollbar(self,command=self.entry1.yview)
        self.scrollbar.place(height=70,x=1080,y=255)
        self.entry1["yscrollcommand"] = self.scrollbar.set

        self.button2 = tk.Button(text="פתח",font=("Ariel",15,"bold"),fg="#414169",command=self.open2)
        self.button2.place(x=1250,y=450,width=100)
        self.button3 = tk.Button(text="המר",command=self.convert_abc,font=("Ariel",15,"bold"),fg="#414169")
        self.button3.place(x=1120,y=510,width=300,height=50)
        self.button4 = tk.Button(text="פתח", font=("Ariel", 15, "bold"), fg="#414169",command= self.open)
        self.button4.place(x=1250, y=850, width=100)
        self.button5 = tk.Button(text="המר", font=("Ariel", 15, "bold"),fg="#414169",command= self.convert_text)
        self.button5.place(x=1120, y=910, width=300, height=50)

        self.variable = tk.IntVar()

        self.on = PhotoImage(file="on\\on.png")
        self.off = PhotoImage(file="on\\off.png")




        self.on_button = tk.Button(image=self.on,bd=0,command=self.switch)
        self.on_button.place(x=1300,y=350)
        self.scale_button = ttk.LabeledScale(variable=self.variable,borderwidth=3)
        self.scale_button.place(x=1300,y=740)




        ########################################################################################################################


        self.config(menu=self.my_menu2)

    def show_type(self):

        if self.show_edit1.get() == False:
            self.frame.place_forget()

        elif self.show_edit1.get() == True:
            self.frame.place(x=250, y=200)

    def show_plan(self):

        if self.show_edit2.get() == False:
            self.frame2.place_forget()

        elif self.show_edit2.get() == True:
            self.frame2.place(x=250, y=500)


    ########################################################################################################################
    def my_poup(self,e):
        self.my_menu.tk_popup(e.x_root, e.y_root)

    def convert_abc(self,*args):
        abca = self.entry1.get(1.0,"end")
        alpabet = "אבגדהוזחטיכלמנסעפצקרשתםןץףך:_+|"
        alpabet2 = "abgdauzhtyklmnsapzkrstmnzfheaov"
        replace = alpabet.replace(alpabet, alpabet2)
        with open("convertion.txt", "w") as w:
            w.close()
        for i in range(len(abca)):
            for j in range(len(alpabet)):
                if abca[i] == alpabet[j]:
                    self.get = self.entry1.get(1.0,"end")
                    self.replace2 = abca[i].replace(abca[i], replace[j])
                    self.mytext = self.replace2
                    with open("convertion.txt","a") as a:
                        a.write(self.mytext)
                        a.close()

        file = set(open("convertion.txt", "r"))


        if file != set():
            try:
                audio = gTTS(text=str(file), lang="en", slow=False)
                if is_on == True:
                    audio.save("example5.mp3")
                else:
                    pass
                subprocess.call("example5.mp3", shell=True)
            except Exception:
                messagebox.showerror("המרת טקסט","אין אינטרנט התחבר לאינטרנט ונסה שוב")


        mytext2 = self.entry1.get(1.0, "end")


        try:
            if self.get != mytext2:
                audio2 = gTTS(text=mytext2, lang="en", slow=False)
                if is_on == True:
                    audio2.save("example5.mp3")
                else:
                    pass
                subprocess.call("example5.mp3", shell=True)
        except AttributeError:
            try:
                audio2 = gTTS(text=mytext2, lang="en", slow=False)
                if is_on == True:
                    audio2.save("example5.mp3")
                else:
                    pass
                subprocess.call("example5.mp3", shell=True)
            except AssertionError:
                messagebox.showerror("טקסט", "לא הכנסת טקסט להמרה")
            except Exception:
                messagebox.showerror("המרת טקסט", "אין אינטרנט התחבר לאינטרנט ונסה שוב")
        except Exception:
            messagebox.showerror("המרת טקסט","אין אינטרנט התחבר לאינטרנט ונסה שוב")


    def orange(self):
        self.config(bg="orange")
        self.label1.config(bg="orange",fg="brown")
        self.label2.config(bg="orange",fg="brown")
        self.label3.config(bg="orange",fg="brown")
        self.label4.config(bg="orange",fg="brown")
        self.label5.config(bg="orange",fg="brown")
        self.label6.config(bg="orange",fg="brown")
        self.label7.config(bg="orange",fg="brown")
        self.label8.config(bg="orange",fg="brown")
        self.button2.config(bg="orange",activebackground="orange",fg="brown",activeforeground="brown")
        self.button3.config(bg="orange",activebackground="orange",fg="brown",activeforeground="brown")
        self.button4.config(bg="orange",activebackground="orange",fg="brown",activeforeground="brown")
        self.button5.config(bg="orange",activebackground="orange",fg="brown",activeforeground="brown")
        self.on_button.config(bg="orange",fg="brown")
        self.label18.config(bg="orange",fg="brown")
        self.scale_button.configure(borderwidth=1)
        self.frame.config(bg="white")
        self.frame2.config(bg="white")
        self.label9.config(bg="white",fg="black")
        self.label10.config(bg="white", fg="black")
        self.label11.config(bg="white", fg="black")
        self.label12.config(bg="white", fg="black")
        self.label13.config(bg="white", fg="black")
        self.label14.config(bg="white", fg="black")
        self.label15.config(bg="white", fg="black")
        self.label16.config(bg="white", fg="black")
        self.label17.config(bg="white", fg="black")





    def black(self):
        self.config(bg="black")
        self.label1.config(bg="black",fg="white")
        self.label2.config(bg="black",fg="white")
        self.label3.config(bg="black",fg="white")
        self.label4.config(bg="black",fg="white")
        self.label5.config(bg="black",fg="white")
        self.label6.config(bg="black",fg="white")
        self.label7.config(bg="black",fg="white")
        self.label8.config(bg="black",fg="white")
        self.frame.config(bg="white")
        self.frame2.config(bg="white")
        self.label9.config(bg="white",fg="black")
        self.label10.config(bg="white", fg="black")
        self.label11.config(bg="white", fg="black")
        self.label12.config(bg="white", fg="black")
        self.label13.config(bg="white", fg="black")
        self.label14.config(bg="white", fg="black")
        self.label15.config(bg="white", fg="black")
        self.label16.config(bg="white", fg="black")
        self.label17.config(bg="white", fg="black")
        self.button2.config(bg="black",fg="white",activebackground="black",activeforeground="white")
        self.button3.config(bg="black",fg="white",activebackground="black",activeforeground="white")
        self.button4.config(bg="black",fg="white",activebackground="black",activeforeground="white")
        self.button5.config(bg="black",fg="white",activebackground="black",activeforeground="white")
        self.on_button.config(bg="black")
        self.label18.config(bg="black",fg="white")
        self.scale_button.configure(borderwidth=1)
        self.frame.config(bg="white")
        self.frame2.config(bg="white")
        self.label9.config(bg="white", fg="black")
        self.label10.config(bg="white", fg="black")
        self.label11.config(bg="white", fg="black")
        self.label12.config(bg="white", fg="black")
        self.label13.config(bg="white", fg="black")
        self.label14.config(bg="white", fg="black")
        self.label15.config(bg="white", fg="black")
        self.label16.config(bg="white", fg="black")
        self.label17.config(bg="white", fg="black")

    def purple(self):
        self.config(bg="purple")
        self.label1.config(bg="purple",fg="white")
        self.label2.config(bg="purple",fg="white")
        self.label3.config(bg="purple",fg="white")
        self.label4.config(bg="purple",fg="white")
        self.label5.config(bg="purple",fg="white")
        self.label6.config(bg="purple",fg="white")
        self.label7.config(bg="purple",fg="white")
        self.label8.config(bg="purple",fg="white")
        self.button2.config(bg="purple",activebackground="purple",activeforeground="white",fg="white")
        self.button3.config(bg="purple",fg="white",activebackground="purple",activeforeground="white")
        self.button4.config(bg="purple",fg="white",activebackground="purple",activeforeground="white")
        self.button5.config(bg="purple",fg="white",activebackground="purple",activeforeground="white")
        self.on_button.config(bg="purple")
        self.label18.config(bg="purple",fg="white")
        self.scale_button.configure(borderwidth=1)
        self.frame.config(bg="white")
        self.frame2.config(bg="white")
        self.label9.config(bg="white", fg="black")
        self.label10.config(bg="white", fg="black")
        self.label11.config(bg="white", fg="black")
        self.label12.config(bg="white", fg="black")
        self.label13.config(bg="white", fg="black")
        self.label14.config(bg="white", fg="black")
        self.label15.config(bg="white", fg="black")
        self.label16.config(bg="white", fg="black")
        self.label17.config(bg="white", fg="black")

    def red(self):
        self.config(bg="red")
        self.label1.config(bg="red",fg="white")
        self.label2.config(bg="red",fg="white")
        self.label3.config(bg="red",fg="white")
        self.label4.config(bg="red",fg="white")
        self.label5.config(bg="red",fg="white")
        self.label6.config(bg="red",fg="white")
        self.label7.config(bg="red",fg="white")
        self.label8.config(bg="red",fg="white")
        self.button2.config(bg="red",fg="white",activebackground="red",activeforeground="white")
        self.button3.config(bg="red",fg="white",activebackground="red",activeforeground="white")
        self.button4.config(bg="red",fg="white",activebackground="red",activeforeground="white")
        self.button5.config(bg="red",fg="white",activebackground="red",activeforeground="white")
        self.on_button.config(bg="red")
        self.label18.config(bg="red",fg="white")
        self.scale_button.configure(borderwidth=1)
        self.frame.config(bg="white")
        self.frame2.config(bg="white")
        self.label9.config(bg="white", fg="black")
        self.label10.config(bg="white", fg="black")
        self.label11.config(bg="white", fg="black")
        self.label12.config(bg="white", fg="black")
        self.label13.config(bg="white", fg="black")
        self.label14.config(bg="white", fg="black")
        self.label15.config(bg="white", fg="black")
        self.label16.config(bg="white", fg="black")
        self.label17.config(bg="white", fg="black")


    def white(self):
        self.config(bg="white")
        self.label1.config(bg="white",fg="black")
        self.label2.config(bg="white",fg="black")
        self.label3.config(bg="white",fg="black")
        self.label4.config(bg="white",fg="black")
        self.label5.config(bg="white",fg="black")
        self.label6.config(bg="white",fg="black")
        self.label7.config(bg="white",fg="black")
        self.label8.config(bg="white",fg="black")
        self.button2.config(bg="white",fg="black",activebackground="white",activeforeground="black")
        self.button3.config(bg="white",fg="black",activebackground="white",activeforeground="black")
        self.button4.config(bg="white",fg="black",activebackground="white",activeforeground="black")
        self.button5.config(bg="white",fg="black",activebackground="white",activeforeground="black")
        self.on_button.config(bg="white")
        self.label18.config(bg="white",fg="black")
        self.scale_button.configure(borderwidth=1)
        self.frame.config(bg="white")
        self.frame2.config(bg="white")
        self.label9.config(bg="white", fg="black")
        self.label10.config(bg="white", fg="black")
        self.label11.config(bg="white", fg="black")
        self.label12.config(bg="white", fg="black")
        self.label13.config(bg="white", fg="black")
        self.label14.config(bg="white", fg="black")
        self.label15.config(bg="white", fg="black")
        self.label16.config(bg="white", fg="black")
        self.label17.config(bg="white", fg="black")


    def blue(self):
        self.config(bg="Azure")
        self.label1.config(bg="Azure",fg="black")
        self.label2.config(bg="Azure",fg="black")
        self.label3.config(bg="Azure",fg="black")
        self.label4.config(bg="Azure",fg="black")
        self.label5.config(bg="Azure",fg="black")
        self.label6.config(bg="Azure",fg="black")
        self.label7.config(bg="Azure",fg="black")
        self.label8.config(bg="Azure",fg="black")
        self.button2.config(bg="Azure",fg="black",activebackground="Azure",activeforeground="black")
        self.button3.config(bg="Azure",fg="black",activebackground="Azure",activeforeground="black")
        self.button4.config(bg="Azure",fg="black",activebackground="Azure",activeforeground="black")
        self.button5.config(bg="Azure",fg="black",activebackground="Azure",activeforeground="black")
        self.on_button.config(bg="Azure")
        self.label18.config(bg="Azure",fg="black")
        self.scale_button.configure(borderwidth=1)
        self.frame.config(bg="white")
        self.frame2.config(bg="white")
        self.label9.config(bg="white", fg="black")
        self.label10.config(bg="white", fg="black")
        self.label11.config(bg="white", fg="black")
        self.label12.config(bg="white", fg="black")
        self.label13.config(bg="white", fg="black")
        self.label14.config(bg="white", fg="black")
        self.label15.config(bg="white", fg="black")
        self.label16.config(bg="white", fg="black")
        self.label17.config(bg="white", fg="black")


    def grin(self):
        self.config(bg="#40E0D0")
        self.label1.config(bg="#40E0D0",fg="black")
        self.label2.config(bg="#40E0D0",fg="black")
        self.label3.config(bg="#40E0D0",fg="black")
        self.label4.config(bg="#40E0D0",fg="black")
        self.label5.config(bg="#40E0D0",fg="black")
        self.label6.config(bg="#40E0D0",fg="black")
        self.label7.config(bg="#40E0D0",fg="black")
        self.label8.config(bg="#40E0D0",fg="black")
        self.button2.config(bg="#40E0D0",fg="black",activebackground="#40E0D0",activeforeground="black")
        self.button3.config(bg="#40E0D0",fg="black",activebackground="#40E0D0",activeforeground="black")
        self.button4.config(bg="#40E0D0",fg="black",activebackground="#40E0D0",activeforeground="black")
        self.button5.config(bg="#40E0D0",fg="black",activebackground="#40E0D0",activeforeground="black")
        self.on_button.config(bg="#40E0D0")
        self.label18.config(bg="#40E0D0",fg="black")
        self.scale_button.configure(borderwidth=1)
        self.frame.config(bg="white")
        self.frame2.config(bg="white")
        self.label9.config(bg="white", fg="black")
        self.label10.config(bg="white", fg="black")
        self.label11.config(bg="white", fg="black")
        self.label12.config(bg="white", fg="black")
        self.label13.config(bg="white", fg="black")
        self.label14.config(bg="white", fg="black")
        self.label15.config(bg="white", fg="black")
        self.label16.config(bg="white", fg="black")
        self.label17.config(bg="white", fg="black")


    def switch(self):
        global is_on


        if is_on:
            self.on_button.config(image=self.off)
            self.label8.config(text="לא פעיל")
            is_on = False
        else:
            self.label8.config(text="פעיל")
            self.on_button.config(image=self.on)

            is_on = True






    def convert_text(self):
        try:
            with open("example.txt","w") as w:
                w.close()
        except FileNotFoundError:
            pass

        get1 = self.variable.get()

        init_rec = sr.Recognizer()
        try:
            if get1 == 0:
                messagebox.showerror("קול","בחרת אפס שניות")
            else:
                self.configure.set("המרה התחילה דבר כעת!!!")
                with sr.Microphone() as source:

                    audio_data = init_rec.record(source, duration=get1)

                    text = init_rec.recognize_google(audio_data)
                    self.label18.config(text="המרה הפסיקה!!!")
                with open("example.txt","a") as a:
                    a.write(text)
                    a.close()
                subprocess.call("example.txt",shell=True)

        except Exception as e:
            mbox = messagebox.askretrycancel("קול שגיאה!","התוכנה לא קלטה את המיקרופון שלך\n לנסות שנית או להפסיק")

            if mbox is True:
                try:
                    with sr.Microphone() as source:
                        audio_data2 = init_rec.record(source, duration=get1)

                        text = init_rec.recognize_google(audio_data2)
                        self.label18.config(text="המרה הפסיקה!!!")
                        with open("example.txt", "a") as r2:
                            r2.write(text)
                            r2.close()
                    subprocess.call("example.txt",shell=True)

                except Exception:
                    messagebox.showerror("קול שגיאה","התוכנה לא הצליחה לקלוט קול מהמיקרופון שלך\n בדוק אותו ולאחר מכן נסה שנית")
                    self.label18.config(text="המרה הפסיקה!!!")

            else:
                self.label18.config(text="המרה הפסיקה!!!")

    def open(self,*args):
        try:
            subprocess.call("example.txt",shell=True)
        except FileNotFoundError:
            messagebox.showerror("פתיחה","לא המרת כלום ולכן אין מסמך לפתיחה")


    def open2(self,*args):
        subprocess.call("example5.mp3",shell=True)




    def help(self=None,*args):

        def help2():
            for x in range(7):
                my_label.config(text=my_progres["value"])
                my_progres["value"] += 15
                root.update_idletasks()
                time.sleep(1)
            my_progres.stop()
            mylabel2 = tk.Label(root, font=("Ariel", 15, "bold"), bg="white")
            mylabel2.place(x=450, y=250)
            mylabel3 = tk.Label(root, font=("Ariel", 15, "bold"), bg="white")
            mylabel3.place(x=150, y=300)
            mylabel4 = tk.Label(root, font=("Ariel", 15, "bold"), bg="white")
            mylabel4.place(x=10, y=350)
            mylabel5 = tk.Label(root, font=("Ariel", 15, "bold"), bg="white")
            mylabel5.place(x=10, y=400)
            mylabel6 = tk.Label(root, font=("Ariel", 15, "bold"), bg="white")
            mylabel6.place(x=250, y=450)
            if str(self.entry1.get(1.0, "end")).strip() == "":
                mylabel2.config(text="!לא הכנסת טקסט להמרה", fg="red")
            else:
                mylabel2.config(text="בסדר הכנסת טקסט להמרה", fg="blue")

            IPaddress = socket.gethostbyname(socket.gethostname())
            if IPaddress == "127.0.0.1":
                mylabel3.config(text=" !אינך מחובר לאינטרנט", fg="red")

            else:
                mylabel3.config(text=f" בסדר אתה מחובר לאינטרנט עם הכתובת הזו {IPaddress}", fg="blue")
            try:
                file = open("example.txt")
                file.close()
                mylabel4.config(text="בסדר הצלחנו לפתוח את מסמך ההמרה", fg="blue")
            except FileNotFoundError:
                mylabel4.config(text="לא הצלחנו לפתוח את מסמך ההמרה אם ניסית להמיר בקול בדוק את המיקרופון שלך",
                                fg="red")
            try:
                file = open("example5.mp3")
                file.close()
                mylabel5.config(text="בסדר הצלחנו לפתוח את סרטון ההמרה", fg="blue")
            except FileNotFoundError:
                mylabel5.config(text="לא הצלחנו לפתוח את סרטון ההמרה אם ניסית להמיר בדוק את חיבור האינטרנט שלך",
                                fg="red")
            if str(self.entry1.get(1.0, "end")).strip() != "" and IPaddress != "127.0.0.1" and open("example.txt") and open("example5.mp3"):
                mylabel6.config(text="!!!ואו הכל בסדר לא הצלחנו למצוא בעיות",fg="blue")

        def stop():
            my_progres.stop()
            root.destroy()

        root = Toplevel(self)
        root.geometry("700x500+500+100")
        root.title("פותר בעיות")
        root.resizable(False, False)

        root.configure(bg="white")

        label = tk.Label(root, text="פתרון בעיות", font=("Ariel", 20, "bold"), bg="white")
        label.place(x=300, y=70)

        my_progres = ttk.Progressbar(root, orient="horizontal",
                                     length=350, mode="determinate")
        my_progres.place(x=190, y=130)

        my_button = ttk.Button(root, text="התחל",command=help2)
        my_button.place(x=450, y=160)
        my_button2 = ttk.Button(root, text="ביטול",command=stop)
        my_button2.place(x=200, y=160)

        my_label = tk.Label(root, text="", bg="white")
        my_label.place(x=350, y=160)
        my_label2 = tk.Label(root, text="", bg="white")
        my_label2.place(x=450, y=250)

        root.mainloop()








    def send_mail(self,*args):
        win32api.ShellExecute(0, 'open', 'mailto:ymb6143@gmail.com', None, None, 0)



    def bindkeys(self,*args):
        self.bind("<Control-o>", self.open2)
        self.bind("<Control-a>", self.open)
        self.bind("<Control-q>",lambda *args:self.destroy())
        self.bind("<Control-h>",self.help)
        self.bind("<KeyPress-F5>",self.send_mail)

        
        








########################################################################################################################





#######################################################################################################################






def saved(username,password):
    with open("names.db", "a") as names:
        names.write(username)
        names.write("\n")
        names.close()
    with open("passwords.db", "a") as passwords:
        passwords.write(password)
        passwords.write("\n")
        passwords.close()



def signin(username,password,get1,self):
    f = set(line.strip() for line in open('passwords.db'))
    b = set(line.strip() for line in open('names.db'))





    if username not in b:
        messagebox.showerror("לא חוקי","שם משתמש לא חוקי")
    elif password not in f:
        messagebox.showerror("לא חוקי","סיסמה לא חוקית")
    elif get1 != "5713":
        messagebox.showerror("לא חוקי","קוד אימות לא נכון")
    else:
        messagebox.showinfo("התחברות", "התחברת בהצלחה")
        self.destroy()
        window = Window3()
        window.mainloop()






class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("הרשמה")
        self.geometry("800x600+500+200")
        self.resizable(False, False)





########################################################################################################################
        container = tk.Frame(width=800,height=600,bg="white")
        container.pack()
########################################################################################################################
        label1 = tk.Label(container,text="הרשמה למערכת",font=("Ariel",30,"bold"),fg="#414169",bg="white")
        label1.place(x=300,y=70)
        label2 = tk.Label(container,text="הכנס את שמך",font=("Ariel", 20, "bold"),fg="#414169",bg="white")
        label2.place(x=500,y=200)
        label3 = tk.Label(container, text="הכנס את סיסמתך", font=("Ariel", 20, "bold"), fg="#414169", bg="white")
        label3.place(x=500, y=270)
        label4 = tk.Label(container, text="הכנס שוב את סיסמתך", font=("Ariel", 20, "bold"), fg="#414169", bg="white")
        label4.place(x=500, y=340)
        label5 = tk.Label(container, text="הכנס שם זיהוי", font=("Ariel", 20, "bold"), fg="#414169", bg="white")
        label5.place(x=500, y=410)
########################################################################################################################
        self.entry1 = ttk.Entry(container,width=35)
        self.entry1.place(x=250,y=210,height=30)
        self.entry2 = ttk.Entry(container, width=35)
        self.entry2.place(x=250, y=280, height=30)
        self.entry3 = ttk.Entry(container, width=35)
        self.entry3.place(x=250, y=350, height=30)
        self.entry4 = ttk.Entry(container, width=35)
        self.entry4.place(x=250, y=420, height=30)
########################################################################################################################
        button1 = tk.Button(container,text="התחבר",font=("Ariel",20,"bold"),fg="#414169",bg="white",width=10,command=self.signin)
        button1.place(x=440,y=490)
        button2 = tk.Button(container, text="הרשם", font=("Ariel", 20, "bold"),fg="#414169", bg="white", width=10,command=self.signup)
        button2.place(x=220, y=490)
########################################################################################################################
    def signup(self):
        get1 = self.entry1.get()
        get2 = self.entry2.get()
        get3 = self.entry3.get()
        get4 = self.entry4.get()


        if len(get1) < 4:
            messagebox.showerror("שם","שם מידי קצר")
        elif len(get2) < 8:
            messagebox.showerror("סיסמה","סיסמה מידי קצרה")
        elif get3 != get2:
            messagebox.showerror("שוב סיסמה","הסיסמאות אינן תואמות")
        elif len(get4) < 4:
            messagebox.showerror("שם זיהוי","שם זיהוי מידי קצר")
        else:
            saved(get4,get2)
            messagebox.showinfo("הרשמה","!נרשמת בהצלחה")

########################################################################################################################


########################################################################################################################
    def signin(self):
        self.destroy()
        root3 = Window2()
        root3.mainloop()






########################################################################################################################
class Window2(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600+500+200")
        self.title("התחברות")
        self.resizable(False, False)
########################################################################################################################
        container = tk.Frame(self,width=800,height=600,bg="white")
        container.pack()
########################################################################################################################
        label1 = tk.Label(container,text="התחברות למערכת",font=("Ariel",30,"bold"),bg="white",fg="#414169")
        label1.place(x=300,y=70)
        label2 = tk.Label(container, text="הכנס שם משתמש", font=("Ariel", 20, "bold"), bg="white", fg="#414169")
        label2.place(x=500, y=200)
        label3 = tk.Label(container, text="הכנס סיסמה", font=("Ariel", 20, "bold"), bg="white", fg="#414169")
        label3.place(x=500, y=270)
        label4 = tk.Label(container, text="הכנס את המספר 5713", font=("Ariel", 20, "bold"), bg="white", fg="#414169")
        label4.place(x=500, y=340)
        label5 = tk.Label(container, text="כדי לוודא שאתה לא רובוט", font=("Ariel", 12, "bold"), bg="white", fg="#414169")
        label5.place(x=550, y=380)
########################################################################################################################
        self.entry1 = ttk.Entry(container, width=35)
        self.entry1.place(x=250, y=210, height=30)
        self.entry2 = ttk.Entry(container, width=35,show="*")
        self.entry2.place(x=250, y=280, height=30)
        self.entry3 = ttk.Entry(container, width=35)
        self.entry3.place(x=250, y=350, height=30)
########################################################################################################################
        self.check = tk.IntVar()
        self.check2 = tk.IntVar()
        self.check3 = tk.IntVar()
        button1 = tk.Button(container, text="התחבר", font=("Ariel", 20, "bold"),fg="#414169", bg="white", width=10,command=self.signin2)
        button1.place(x=440, y=490)
        button2 = tk.Button(container, text="הרשם", font=("Ariel", 20, "bold"),fg="#414169", bg="white", width=10,command=self.signup2)
        button2.place(x=220, y=490)
        button3 = ttk.Checkbutton(container,onvalue=1,offvalue=0,variable=self.check,text="שמור סיסמה ושם משתמש לפעם הבאה\n או מחק סיסמה שמורה",command=self.saved)
        button3.place(x=550,y=420)
        self.button4 = ttk.Checkbutton(container,onvalue=1,offvalue=0,variable=self.check2,text="הראה סיסמה שמורה",command=self.show)
        self.button4.place(x=550, y=465)
        self.button5 = ttk.Checkbutton(container,onvalue=1,offvalue=0,variable=self.check3,text="הצג סיסמה",command=self.show_entry)
        self.button5.place(x=525,y=310)

        fileopen = list(line.strip() for line in open('name and password.txt'))
        if fileopen == list():
            self.button4["state"] = "disabled"

    def signin2(self):
        get1 = self.entry1.get()
        get2 = self.entry2.get()
        get3 = self.entry3.get()
        signin(get1,get2,get3,self)



    def signup2(self):
        self.destroy()
        root = Window()
        root.mainloop()

    def saved(self):
        if self.check.get() == 1:
            with open("name and password.txt","a") as a:
                a.write(self.entry1.get())
                a.write("\n")
                a.write(self.entry2.get())
                a.write("\n")
                a.close()
        elif self.check.get() == 0:
            with open("name and password.txt","w") as w:
                w.close()
    def show(self):
        try:
            fileopen = list(line.strip() for line in open('name and password.txt'))
            if self.check2.get() == 1:
                self.entry1.insert(0,fileopen[0])
                self.entry2.insert(0,fileopen[1])
            elif self.check2.get() == 0:
                self.entry1.delete(0,"end")
                self.entry2.delete(0,"end")
        except FileNotFoundError:
            pass
            


    def show_entry(self):
        if self.check3.get() == 1:
            self.entry2["show"] = ""
        else:
            self.entry2["show"] = "*"






root1 = Window2()
root1.mainloop()



########################################################################################################################


