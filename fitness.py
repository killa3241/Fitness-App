from tkinter import*
from tkinter import messagebox

root5=Tk()

global bg2

root5.title("PLAN OF ACTION")
root5.geometry('1920x1080')
bg5=PhotoImage(file=r"dum1.png")

screen_width = root5.winfo_screenwidth()
screen_height = root5.winfo_screenheight()

mycan5=Canvas(root5,width=screen_width,height=screen_height)
mycan5.pack(fill="both",expand=True)

mycan5.create_image(0,0,image=bg5,anchor='nw')

mycan5.create_text(700,40,text="FITNESS MODULE",font="Algerian 80 ",fill="yellow")

b7=Button(root5,text="EXIT",width=20,height=3,fg="red",bg="light yellow",font="Merriweather 10 bold",command=root5.destroy)
mycan5.create_window(90,40,window=b7)

def cre():
    cred=Toplevel()
    cred.title("CREDITS")
    cred.geometry('1920x1080')
    
    mycan6=Canvas(cred,width=screen_width,height=screen_height,bg="red")
    mycan6.pack(fill="both",expand=True)

    b9=Button(cred,text="MAIN MENU",width=20,height=3,font="Merriweather 10 bold",command=cred.destroy)
    mycan6.create_window(80,40,window=b9)

    mycan6.create_text(600,40,text="CREDITS",font="Merriweather 70 bold",fill="black")
    mycan6.create_text(600,120,text="ANIKAIT NANJUNDAPPA",font="Merriweather 30 bold",fill="light blue")
    mycan6.create_text(600,200,text="CHIRAG A",font="Merriweather 30 bold",fill="light blue")
    mycan6.create_text(600,300,text="ADHESH RAJATH",font="Merriweather 30 bold",fill="light blue")
    mycan6.create_text(600,400,text="ASHISH CHANDRA K",font="Merriweather 30 bold",fill="light blue")
    
def ani():
    global bg
    root=Toplevel()
    root.title("Fitness Module")
    root.geometry('1920x1080')

    bg=PhotoImage(file=r"Dumbell.png")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    mycan=Canvas(root,width=screen_width,height=screen_height)
    mycan.pack(fill="both",expand=True)
    mycan.create_image(0,0,image=bg,anchor='nw')

    mycan.create_text(600,30,text="DETAILS",font="Merriweather 50 bold",fill="light green")
    mycan.create_text(400,70,text="Enter Your Weight(kg)",font=50,fill="light blue")

    e=Entry(root,width=40,bd=0)
    ecan=mycan.create_window(400,110,window=e)

    mycan.create_text(400,140,text="Enter Your Height(cm)",font=50,fill="white")

    e1=Entry(root,width=40,bd=0)
    e1can=mycan.create_window(400,180,window=e1)

    mycan.create_text(400,210,text="Enter Your Age",font=50,fill="white")

    e2=Entry(root,width=40,bd=0)
    e2can=mycan.create_window(400,250,window=e2)

    mycan.create_text(400,280,text="Gender",font=50,fill="white")

    r=DoubleVar()
    r.set(0)

    rb=Radiobutton(root,text="Male",variable=r,value=1.0)
    rb1=Radiobutton(root,text="Female",variable=r,value=0.0)
    mycan.create_window(400,330,window=rb)
    mycan.create_window(400,370,window=rb1)

    mycan.create_text(400,410,text="Exercise Level",font=50,fill="white")

    r1=DoubleVar()
    r1.set(0)

    rb2=Radiobutton(root,text="Sedentary",variable=r1,value=1.2)
    rb3=Radiobutton(root,text="Light activity",variable=r1,value=1.375)
    rb4=Radiobutton(root,text="Moderate activity",variable=r1,value=1.55)
    rb5=Radiobutton(root,text="Very active",variable=r1,value=1.725)
    rb6=Radiobutton(root,text="Intense activity",variable=r1,value=1.9)

    mycan.create_window(400,440,window=rb2)
    mycan.create_window(400,470,window=rb3)
    mycan.create_window(400,500,window=rb4)
    mycan.create_window(400,530,window=rb5)
    mycan.create_window(400,560,window=rb6)
    global x

    def mycal():
        global x
        global y
        global z
        global w
        global s
        x=int(e.get())
        y=int(e1.get())
        z=int(e2.get())
        if e.get()=='' or e1.get()=='' or e2.get()=='':
            messagebox.showerror("Error","Please enter all details,calculate and then proceed")
        if (r.get()==1.0):
            w=(88.362+(13.397*x)+(4.799*y)-(5.677*z))
        if (r.get()==0.0):
            w=(447.593+(9.247*x)+(3.098*y)-(4.330*z))
        s=int(w*(r1.get()))    

        mycan.create_text(900,200,text=str(s)+'Calories/day',fill="light blue",font="Merriweather 20 bold")

    def my2nd():
        global bg1
        root1=Toplevel()
        root1.title("PLAN OF ACTION")
        root1.geometry('1920x1080')
        bg1=PhotoImage(file=r"Dumbell.png")

        mycan1=Canvas(root1,width=screen_width,height=screen_height)
        mycan1.pack(fill="both",expand=True)
        mycan1.create_image(0,0,image=bg1,anchor='nw')

        b3=Button(root1,text="<<Back",width=20,height=3,command=root1.destroy)
        mycan1.create_window(80,40,window=b3)

        #mycan1.create_text(200,300,text="welcome to 2nd window",font=30,fill="yellow")
        #mycan1.create_text(200,300,text=str(s),font=30,fill="yellow")
        r2=DoubleVar()
        r2.set(0)

        mycan1.create_text(600,30,text="HOW WOULD YOU LIKE TO PROCEED?",font="Merriweather 30 bold",fill="light green")

        rb7=Radiobutton(root1,text="Weight gain",width=20,height=3,variable=r2,value=3.0)
        rb8=Radiobutton(root1,text="Weight loss",width=20,height=3,variable=r2,value=2.0)

        mycan1.create_window(500,200,window=rb7)
        mycan1.create_window(500,250,window=rb8)

        dic=dict()
        def mywgt():
            global jj
            jj=r2.get()
            
            if jj==2.0:
                dic={"Calories to loose 0.25kg/week":s-250,"Calories to loose 0.5kg/week":s-500,"To loose 1kg/week":s-1000}
                mycan1.create_text(800,200,text="Calories to loose 0.25kg/week :"+str(s-250),font="Arial 20 bold",fill="light blue")
                mycan1.create_text(800,250,text="Calories to loose 0.5kg/week :"+str(s-500),font="Arial 20 bold",fill="light blue")
                mycan1.create_text(800,300,text="Calories to loose 1kg/week :"+str(s-1000),font="Arial 20 bold",fill="light blue")
                
            if jj==3.0:
                dic={"Calories to gain 0.25kg/week":s+250,"Calories to gain 0.5kg/week":s+500,"to gain 1kg/week":s+1000}
                mycan1.create_text(800,350,text="Calories to gain 0.25kg/week :"+str(s+250),font="Arial 20 bold",fill="light blue")
                mycan1.create_text(800,400,text="Calories to gain 0.25kg/week :"+str(s+500),font="Arial 20 bold",fill="light blue")
                mycan1.create_text(800,450,text="Calories to gain 0.25kg/week :"+str(s+1000),font="Arial 20 bold",fill="light blue")
            #mycan1.create_text(400,500,text=dic)
        
        rb9=Button(root1,text="Show",width=20,height=3,command=mywgt)
        mycan1.create_window(500,400,window=rb9)
        
        def my3rd():
            global bg3
            global bmi
            root2=Toplevel()
            root2.geometry('1920x1080')
            root2.title('BMI')
            root2.geometry("1920x1080")
            bg3=PhotoImage(file=r"Dumbell.png")

            mycan2=Canvas(root2,width=1920,height=1080)
            mycan2.pack(fill="both",expand=True)
            mycan2.create_image(0,0,image=bg3,anchor='nw')

            mycan2.create_text(500,100,text="Your BMI is =",font="Merriweather 40 bold",fill="light green")

            bmi=(x/(y*y))*10000

            mycan2.create_text(500,150,text=bmi,font="Merriweather 20 bold",fill="green")

            if bmi>=25.0:
                mycan2.create_text(500,200,text="Overweight",font="Merriweather 30 bold",fill="red")
            elif bmi>=18.5:
                mycan2.create_text(500,200,text="Normal",font="Merriweather 30 bold",fill="red")
            else: 
                mycan2.create_text(500,200,text="Under weight",font="Merriweather 30 bold",fill="red")

            b5=Button(root2,text="<<Back",width=20,height=3,command=root2.destroy)
            mycan2.create_window(80,40,window=b5)
            
            
        b4=Button(root1,text="Next>>",width=20,height=3,command=my3rd)
        mycan1.create_window(700,600,window=b4)
        


    b=Button(root,text="CALCULATE",width=20,height=3,command=mycal)
    mycan.create_window(650,200,window=b)    

    b1=Button(root,text="NEXT",fg='blue',width=20,height=3,command=my2nd)
    mycan.create_window(650,300,window=b1)

    #mycan.create_text(300,300,text="first window",font=50,fill="yellow")
    mycan.create_text(850,100,text="Enter details, calculate and then proceed",font="Merriweather 20 bold",fill="light blue")

    b2=Button(root,text="MAIN MENU",width=20,height=3,fg="red",bg="light yellow",command=root.destroy)
    mycan.create_window(80,30,window=b2)

b6=Button(root5,text="BMI & OTHER DETAILS",bg="light green",width=30,height=3,font="Merriweather 10 bold",command=ani)
mycan5.create_window(650,200,window=b6)

b8=Button(root5,text="CREDITS",bg="pink",width=30,height=3,font="Merriweather 10 bold",command=cre)
mycan5.create_window(650,500,window=b8)

def time():
    root=Toplevel()
    root.geometry('1920x1080')
    root.configure(bg="cyan")

    value1=IntVar()
    value2=IntVar()

    

              
    def excercise():
        #global value1,value2
        top=Toplevel()
        top.geometry("1920x1080")
        top.configure(bg="magenta")

        Radiobutton(top,text="Shoulders and back",font=40,variable=value2,value=4).pack()#grid(row=7,column=7)
        Radiobutton(top,text="Upper Body",font=40,variable=value2,value=5).pack()#grid(row=8,column=7)
        Radiobutton(top,text="Lower Body",font=40,variable=value2,value=6).pack()#grid(row=9,column=7)

        def part():
            
            if (value1.get()==1 and value2.get()==4) :
                lbl00=Label(top,text="""                        
                  Beginner Shoulders and Back Exercises:
                          Jumping Jacks 30sec
                          Arm raises 16 sec
                          Side arm raise 16sec
                          Rhomboid pulls x10(2sets)
                          Knee pushup x14
                          Prone triceps pushup x14
                          Arm scissors 30sec
                          Childs pose 30sec
                      """,font=40,bg="magenta",anchor=S).pack()#grid(row=4,column=0)
            elif (value1.get()==2 and value2.get()==4):
                lbl0=Label(top,text="""
                  Intermediate Shoulders and Back Exercises:
                         Jumping jacks 30sec
                         Incline pushups x14(2sets)
                         Rhomboid pulls x12(2sets)
                         Hover pushup x 14(2sets)
                         Swimmer and superman x12(2sets)
                         Hip hinge x10
                         Childs pose 30sec

                      """,font=40,bg="magenta",anchor=S).pack()#grid(row=4,column=0)
                      
            elif (value1.get()==3 and value2.get()==4):
                 lbl=Label(top,text="""
                  Advanced Shoulders and Back Exercises :
                       Jumping jacks 30sec
                       Pushups x15(2sets)
                       Hyperextension x14(2sets)
                       Reverse pushups x12(2sets)
                       Side lying floor stretch left 30sec
                       Side lying floor stretch right 30sec
                       Pike pushups x12(2sets)
                       Cat cow pose 30sec
                       Supine pushups x14(2sets)
                       Childs pose 30sec

                       """,font=40,bg="magenta",anchor=S).grid(row=4,column=0)
            elif (value1.get()==1 and value2.get()==5):
                lbl1=Label(top,text="""Beginner Upper Body Exercises :

                                            Jumping jacks x20
                                            Incline push up x6 (2 sets)
                                            Knee push up x4(2sets)
                                            Push up x4(2 sets)
                                            Wide arm push up x4(2sets),
                                            Cobra stretch (20 sec)
                                            Chest stretch (20 sec)

                      """,font='30,Helvetica',bg="magenta",anchor=S).pack()#grid(row=4,column=0)
            elif (value1.get()==2 and value2.get()==5):
                lbl2=Label(top,text="""         Intermediate Upper Body Exercises:

                  
                                                        Jumping jacks x40
                                                        Incline push up x12 (2 sets)
                                                        Knee push up x10(2sets)
                                                        Push up x8(2 sets)
                                                        Wide arm push up x8(2sets)
                                                        Cobra stretch (40 sec)
                                                        Chest stretch (40 sec)
                      """,font=40,bg="magenta",anchor=S).pack()#grid(row=4,column=0)
            elif (value1.get()==3 and value2.get()==5) :
                lbl3=Label(top,text="""             Advanced Upper Body Exercises:


                                                        Jumping jacks x60
                                                        Incline push up x16(3 sets)
                                                        Knee push up x20(3sets)
                                                        Push up x16(2 sets)
                                                        Wide arm push up x16(3sets)
                                                        Cobra stretch (60 sec)
                                                        Chest stretch (60 sec)
                                                        """,font='30,Helvitca',bg="magenta",anchor=S).pack()#grid(row=4,column=0)
                      
            elif (value1.get()==1 and value2.get()==6):
                lbl4=Label(top,text="""          Beginner Lower Body Exercises:


                                                        Jumping Jacks 30sec
                                                        Squats x12(2sets)
                                                        Forward lunge x7(2sets)
                                                        Backward lunge x7(2sets)
                                                        Calf stretch right 20sec
                                                        Calf stretch left 20sec
                                                        Knee to chest left 30sec
                                                        Knee to chest right 30sec
                                                        """,font='30,Helvetica',bg="magenta",anchor=S).pack()#grid(row=4,column=0)
            elif value1.get()==2 and value2.get()==6:
                lbl5=Label(top,text="""         
                 Intermediate Lower Body Exercises:

                             Jumping Jacks 30sec
                             Squats x12(3sets)
                             Forward lunge x14(2sets)
                             Backward lunge x14(2sets)
                             Calf stretch right 30sec
                            Calf stretch left 30sec
                            Sumo squat x12(2sets)
                             Wall sit 30sec

                                                        """,font="40,Helvetica",bg="magenta",anchor=S).pack()#grid(row=4,column=0)
            elif (value1.get()==3 and value2.get()==6):
                lbl6=Label(top,text="""             Advanced Lower Body Exercises:

                                                            Burpees x10
                                                            Squats x 14(3sets)
                                                            Jumping squats x14(2sets)
                                                            Wall sit 40 sec
                                                            Side leg circles right x12(3sets)
                                                            Side leg circles left x 12 (3sets)
                                                            Left quad stretch with wall 30sec
                                                            Right quad stretch with wall 30sec
                                                            Calf stretch right 30sec
                                                            Calf stretch left 30sec         
                                                            """,font=40,bg="magenta",anchor=S).pack()#grid(row=4,column=0)

        btn1=Button(top,text="Click here for suggestions",command=part).pack()  #grid(row=10,column=10)
        b3=Button(top,text="<<Back",width=20,height=3,command=top.destroy)
        b3.place(relx=0.1,rely=0.1)
        
          

    myLabel = Label(root,text="No. of pushups you can do",font=40).pack()#grid(row=0,column=0)

    Radiobutton(root,text="3-5 (Beginner)",font=40,variable=value1,value=1).pack()#grid(row=1,column=0)
    Radiobutton(root,text="10 (Intermediate)",font=40,variable=value1,value=2).pack()#grid(row=2,column=0)
    Radiobutton(root,text=">10 (Advanced)",font=40,variable=value1,value=3).pack()#grid(row=3,column=0)

    btn=Button(root,text="Which part of the body do you want to work on?",font=40,command=excercise).pack()  #grid(row=4,column=0)
    xy=Button(root,text="Main Menu",width=10,height=3,command=root.destroy)
    xy.place(relx=0.1,rely=0.1)    

    root.mainloop()


def bld():
    root = Tk()
    root.geometry('1920x1080')

    ent=IntVar(root,name="int")
    et=IntVar(root,name="int1")

    label=Label(root,text="Enter your Heart rate : ",font=("Merryweather",15)).grid(row=0,column=0)
    e=Entry(root,width=70,textvariable=ent)
    e.grid(row=0,column=1)
    e.insert(0," ")

    lbl=Label(root,text="Enter your blood sugar level(mg/dL): ",font=("Merryweather",15)).grid(row=7,column=0)
    e1=Entry(root,width=70,textvariable=et)
    e1.grid(row=7,column=1)
    e1.insert(1," ")

    def heartrate():   
        a=ent.get()
        if a<=0:
            lbl=Label(root,text="""Data entered is invalid
            
            
            
                                                            """,font=("Chiller",20),bg="light red").grid(row=2,column=0)
        elif a<60:
            label1=Label(root,text="You have low Blood Pressure:",font=("Chiller",20)).grid(row=2,column=0)
            label2=Label(root,text="""                    
                                      1.Drink more water, less alcohol.
                                      2.Pay attention to body positions.Don't sit with legs crossed.
                                      3.Eat small, low-carb meals.Limit high-carbohydrate foods such as potatoes, rice, pasta and bread.
                                      4.Exercise regularly.At least 30 minutes of moderate physical activity every day.""",padx=50,pady=50,font=("Helvetica",12),bg="light red",anchor=E).grid(row=4,column=0)
        elif (a>60 and a<120):
            label3=Label(root,text="You have normal Blood Pressure:",font=("Arial",20)).grid(row=2,column=0)
            label4=Label(root,text=                        
              """ 1.Exercise is very effective in maintaining a constant heart rate.
                  2.Diet must consist of fruits, vegetables, low-fat dairy, whole grains, poultry, fish, and nuts.
                    Avoid fats, red meat, and excess sugar.
                  3.Your body only needs about 500 milligrams of salt a day.Do not consume more than this.                   
                  4.Avoid the habit of smoking or drinking.            """,padx=50,pady=50,font=("Helvetica",12),bg="light red").grid(row=4,column=0)
        elif (a)>120:
            label5=Label(root,text="You have high Blood Pressure:",font=("Jokerman",20)).grid(row=2,column=0)
            label6=Label(root,text="""             
               1.Getting at least 150 minutes of physical activity each week (about 30 minutes a day, 5 days a week)
               2.Avoid smoking at it increases blood pressure due to large adrenaline release.
               3.Eating a healthy diet, including limited salt in diet.
               4.Avoid intake of alcohol as it affects heart rate.
               5.Manage stress by doing meditation or yoga. """,padx=50,pady=50,font=("Arial",20),bg="light red").grid(row=4,column=0)
        root.setvar(name="int",value=0)
    button=Button(root,text="CHECK",command=heartrate).grid(row=1,column=0,columnspan=2)
    

    def val1():
        x=et.get()
        if x<=0:
            lbl1=Label(root,text="""       Data entered is invalid
            
            
            
                                                            """,font=("Chiller",16)).grid(row=9,column=0)
        elif 0 < x < 80:
            lbl1=Label(root,text="You have LOW BLOOD SUGAR LEVEL",font=("Chiller",16)).grid(row=9,column=0)
            lbl2=Label(root,text=
                       '''Here are some suggestions
                          1)Take four glucose tablets.                                  
                          2)Drink four ounces of fruit juice.                        
                          3)Drink four ounces of regular soda, not diet soda.                                                          .
                          4)Eat four pieces of hard candy.''',padx=70,pady=80,font=("Arial",14),bg="cyan",anchor=E).grid(row=10,column=0)

        elif 80 <= x <=130:
            lbl1=Label(root,text="Your BLOOD SUGAR LEVEL is NORMAL",font=("Chiller",16)).grid(row=9,column=0)
            lbl2=Label(root,text=
                       """Here are some suggestions:
                       1)Keep track of your blood sugar levels to see what makes them go up or down.
                       2)Eat at regular times, and don't skip meals.
                       3)Choose foods lower in calories, saturated fat, trans fat, sugar, and salt.
                       4)Track your food, drink, and physical activity.
                       5)Drink water instead of juice or soda. """,padx=70,pady=80,font=("Arial",14),bg="cyan",anchor=E).grid(row=10,column=0)
        elif x >130:
            lbl1=Label(root,text="        Your BLOOD SUGAR LEVEL is HIGH       ",font=("Jokerman",16)).grid(row=9,column=0)
            lbl2=Label(root,text=
                       '''Here are some suggestions
                          1) Be more active. Regular exercise can help keep your blood sugar levels on track. 
                          2)Take medicine as instructed. 
                          3)If your blood sugar is often high, your doctor may change how much medicine you take or when you take it.
                          4)Follow your diabetes meal plan. 
                          5)Ask your doctor or dietitian for help if you’re having trouble sticking to it.
                          6)Check your blood sugar as directed by your doctor. 
                          7)Check more often if you’re sick or if you’re concerned about high or low blood sugar.
                          8)Talk to your doctor about adjusting how much insulin you take and what types of insulin to use.''',padx=70,pady=80,font=("Arial",20),fg="cyan",anchor=E).grid(row=10,column=0)
        root.setvar(name ="int1", value = 0)
    
    btn=Button(root,text="CHECK",command=val1).grid(row=8,column=0,columnspan=2)

    Butn=Button(root,text="MAIN MENU",width =10,height=3,command=root.destroy)
    Butn.place(relx=0.9,rely=0.03)
    
        

    
                     
          
b10=Button(root5,text="FITNESS ADVICE",bg="light blue",width=30,height=3,font="Merriweather 10 bold",command=time)
mycan5.create_window(650,300,window=b10)

b11=Button(root5,text="HEART RATE & BLOOD SUGAR",bg="ivory",width=30,height=3,font="Merriweather 10 bold",command=bld)
mycan5.create_window(650,400,window=b11)

      
root5.mainloop()
