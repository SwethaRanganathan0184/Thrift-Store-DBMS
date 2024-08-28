#IMPORTING TKINTER MODULE FOR GUI
from tkinter.ttk import*
from tkinter import *
from tkinter import filedialog
#IMPORTING TKINTER FOR MESSAGEBOX
import tkinter.messagebox as MessageBox
#IMPORTING MySQL CONNECTOR FOR PYTHON MySQL INTEGRATION
import mysql.connector as mysql

#CREATING TABLE FOR TSHIRT
def Tshirt():
    Database = mysql.connect(host = "localhost", user="root", password = "swetha123", database = "thriftstore5")
    cursor=Database.cursor()
    t1 = "CREATE TABLE Tshirt( Colour varchar(30), Conditions varchar(40), Size varchar(30), Final_price varchar(20));"
   
    #cursor.execute(t1)
   
    Database.commit()
    return
#CREATING TABLE FOR JACKET
def Jacket():
    Database = mysql.connect(host = "localhost", user="root", password = "swetha123", database = "thriftstore5")
    cursor=Database.cursor()
    jck1 = "CREATE TABLE Jacket( Colour varchar(30), Conditions varchar(40), Size varchar(30), Final_price varchar(20));"
   
    #cursor.execute(jck1)
   
    Database.commit()
    return
#CREATING TABLE FOR JEANS
def Jeans():
    Database = mysql.connect(host = "localhost", user="root", password = "swetha123", database = "thriftstore5")
    cursor=Database.cursor()
    je1 = "CREATE TABLE Jeans( Colour varchar(30), Conditions varchar(40), Size varchar(30), Final_price char(20));"
   
    #cursor.execute(je1)
   
    Database.commit()
    return
#CREATING TABLE FOR SHIRTS
def Shirts():
    Database = mysql.connect(host = "localhost", user="root", password = "swetha123", database = "thriftstore5")
    cursor=Database.cursor()
    s1 = "CREATE TABLE Shirts( Colour varchar(30), Conditions varchar(40), Size varchar(30), Final_price char(20));"
   
    #cursor.execute(s1)
   
    Database.commit()
    return
#CREATING TABLE FOR PANTS
def Pants():
    Database = mysql.connect(host = "localhost", user="root", password = "swetha123", database = "thriftstore5")
    cursor=Database.cursor()
    p1 = "CREATE TABLE Pants( Colour varchar(30), Conditions varchar(40), Size varchar(30), Final_price char(20));"
   
    #cursor.execute(p1)
   
    Database.commit()
    return
#CREATING TABLE FOR COATS
def Coats():
    Database = mysql.connect(host = "localhost", user="root", password = "swetha123", database = "thriftstore5")
    cursor=Database.cursor()
    c1 = "CREATE TABLE Coats( Colour varchar(30), Conditions varchar(40), Size varchar(30), Final_price char(20));"
   
    #cursor.execute(c1)

    Database.commit()
    return
Tshirt()
Jacket()
Jeans()
Pants()
Shirts()
Coats()

#CREATING WINDOW IN GUI
window=Tk()
window.title("GUI")
img=PhotoImage(file="C:\\Users\\Admin\\Downloads\\THRIFT STORE CLIPART png.png")

#SETTING WINDOW GEOMETRY
window.geometry("1500x2000")

#CREATING LABEL IN GUI
l1=Label(window,image=img)

l1.place(x=450,y=10)

l2=Label(window,text="Hello,Welcome to our Thrift Store! \n Would you like to:",font=("Arial bold",35),fg="dark blue")
l2.place(x=340,y=350)
#DEFINING CLICK SEQUENCE FOR DONATION PORTAL
def clicked():
    l2.config(text="Welcome to the donation portal",font=("Arial bold",35))
    l2.place(x=370,y=350)
    l3=Label(window,text="Choose the type of cloth:",font=('Arial bold',25),justify=RIGHT,fg="purple")
    l3.place(x=10,y=410)
   
    #cloth material
    combom = Combobox(window, font=("Arial Bold",20))
    combom["values"]=("Tshirt","Jeans","Jacket","Pants","Shirts","Coats")
    combom.current()
    combom.place(x=10,y=470)

    #Condition of cloth
    l4=Label(window,text="Condition:",font=("Arial bold",25),fg="purple")
    l4.place(x=470, y=410)
    combo=Combobox(window,font=('Arial bold',20))
    combo["values"]=("Brand New With Tag","Never Worn,No Tag","Gently Worn")
    combo.current()
    combo.place(x=470,y=470)

    #Colour
    l5=Label(window,text="Colour:",font=("Arial bold",25),fg="purple")
    l5.place(x=850,y=410)
    txtcol=Entry(window,width=10)
    txtcol.place(x=850,y=470)

    #Size
    l6=Label(window,text="Size:",font=("Arial bold",25),fg="purple")
    l6.place(x=1000,y=410)
    combosz=Combobox(window,font=("Arial bold",20))
    combosz["values"]=("Small(S)","Medium(M)","Large(L)","Extra Large(XL)")
    combosz.current()
    combosz.place(x=1000,y=470)
    #COMMAND FOR INSERTNG VALUES FROM GUI TO TABLE IN MySQL
    def insert():
        combomt=combom.get()
        comboc=combo.get()
        colours=txtcol.get()
        sizes=combosz.get()

        #ASSIGNING VARIABLES FOR PRICE OF CLOTHING
        Tsi=1000
        Jai=1500
        Jei=2000
        Shi=1500
        Pai=1500
        Coi=3000
        #FINAL PRICE DEFINITION ACCORDING TO CONDITION OF CLOTH
        if comboc=="Brand New With Tag":
            Tsi=str(0.75 * Tsi)
            Jai=str(0.75 * Jai)
            Jei=str(0.75 * Jei)
            Shi=str(0.75 * Shi)
            Pai=str(0.75 * Pai)
            Coi=str(0.75 * Coi)
        if comboc=="Never Worn,No Tag":
            Tsi=str(0.5 * Tsi)
            Jai=str(0.5 * Jai)
            Jei=str(0.5 * Jei)
            Shi=str(0.5 * Shi)
            Pai=str(0.5 * Pai)
            Coi=str(0.5 * Coi)
        if comboc=="Gently Worn":
            Tsi=str(0.25 * Tsi)
            Jai=str(0.25 * Jai)
            Jei=str(0.25 * Jei)
            Shi=str(0.25 * Shi)
            Pai=str(0.25 * Pai)
            Coi=str(0.25 * Coi)

        #Tsi FOR TSHIRT
        #Jai FOR JACKETS
        #Jei FOR JEANS
        #Shi FOR SHIRTS
        #Pai FOR PANTS
        #Coi FOR COATS

        #MESSAGEBOX FOR FILLING ALL THE FIELDS
        if (combomt=="" or comboc=="" or colours=="" or sizes==""):
            MessageBox.showinfo("Insert Status","All Fields are required")
           
            #tshirt
        if combomt == "Tshirt":
            Database=mysql.connect(host="localhost",user="root",password="swetha123",database="thriftstore5")
            cursor=Database.cursor()
            tshirt1 = "INSERT INTO Tshirt values('"+ colours +"','"+ comboc +"','"+ sizes +"','"+ Tsi +"')"
            cursor.execute(tshirt1)
            cursor.execute("commit");
            MessageBox.showinfo("Donation status","Thank you! Donated successfully")

            #jacket
        if combomt == "Jacket":
            Database=mysql.connect(host="localhost",user="root",password="swetha123",database="thriftstore5")
            cursor=Database.cursor()
            tshirt1 = "INSERT INTO Jacket values('"+ colours +"','"+ comboc +"','"+ sizes +"','"+ Jai +"')"
            cursor.execute(tshirt1)
            cursor.execute("commit");
            MessageBox.showinfo("Donation status","Thank you! Donated successfully")

            #jeans
        if combomt == "Jeans":
            Database=mysql.connect(host="localhost",user="root",password="swetha123",database="thriftstore5")
            cursor=Database.cursor()
            tshirt1 = "INSERT INTO Jeans values('"+ colours +"','"+ comboc +"','"+ sizes +"','"+ Jei +"')"
            cursor.execute(tshirt1)
            cursor.execute("commit");
            MessageBox.showinfo("Donation status","Thank you! Donated successfully")

            #shirts
        if combomt == "Shirts":
            Database=mysql.connect(host="localhost",user="root",password="swetha123",database="thriftstore5")
            cursor=Database.cursor()
            tshirt1 = "INSERT INTO Shirts values('"+ colours +"','"+ comboc +"','"+ sizes +"','"+ Shi +"')"
            cursor.execute(tshirt1)
            cursor.execute("commit");
            MessageBox.showinfo("Donation status","Thank you! Donated successfully")

            #pants
        if combomt == "Pants":
            Database=mysql.connect(host="localhost",user="root",password="swetha123",database="thriftstore5")
            cursor=Database.cursor()
            tshirt1 = "INSERT INTO Pants values('"+ colours +"','"+ comboc +"','"+ sizes +"','"+ Pai +"')"
            cursor.execute(tshirt1)
            cursor.execute("commit");
            MessageBox.showinfo("Donation status","Thank you! Donated successfully")

            #coats
        if combomt == "Coats":
            Database=mysql.connect(host="localhost",user="root",password="swetha123",database="thriftstore5")
            cursor=Database.cursor()
            tshirt1 = "INSERT INTO Coats values('"+ colours +"','"+ comboc +"','"+ sizes +"','"+ Coi +"')"
            cursor.execute(tshirt1)
            cursor.execute("commit");
            MessageBox.showinfo("Donation status","Thank you! Donated successfully")

       

       
       
    #Finalise donation button
    btf=Button(window,text="Finalise Your Donation!",font=("Arial bold",18),bg="pink", command=insert)
    btf.place(x=500,y=550)
    btf.config(height=2,width=20)


#CREATING BUTTON FOR CLOTH DONATION
   
bt=Button(window,text="Donate Clothes for the Store!", font=('Arial bold',15),bg='skyblue',command=clicked)
bt.place(x=90,y=550)
bt.config(height=4,width=25)

#CREATING COMMAND CLICK SEQUENCE FOR PURCHASE PORTAL
def clicked2():
   
   
    l2.config(text="Welcome to the purchase portal",fg="green",font = ("Arial Bold",35))
    l2.place(x=370, y=350)
    l3=Label(window,text="Choose the type of cloth:",font=('Arial bold',25),justify=RIGHT,fg="brown")
    l3.place(x=10,y=410)

    #cloth material
    combom = Combobox(window, font=("Arial Bold",20))
    combom["values"]=("Tshirt","Jeans","Jacket","Pants","Shirts","Coats")
    combom.current()
    combom.place(x=10,y=470)

    #Condition of cloth
    l4=Label(window,text="Condition:",font=("Arial bold",25),fg="brown")
    l4.place(x=470,y=410)
    combo=Combobox(window,font=('Arial bold',20))
    combo["values"]=("Brand New With Tag","Never Worn,No Tag","Gently Worn")
    combo.current()
    combo.place(x=470,y=470)

    #Colour
    l5=Label(window,text="Colour:",font=("Arial bold",25),fg="brown")
    l5.place(x=850,y=410)
    txtcol=Entry(window,width=10)
    txtcol.place(x=850,y=470)

    #Size
    l6=Label(window,text="Size:",font=("Arial bold",25),fg="brown")
    l6.place(x=1000,y=410)
    combosz=Combobox(window,font=("Arial bold",20))
    combosz["values"]=("Small(S)","Medium(M)","Large(L)","Extra Large(XL)")
    combosz.current()
    combosz.place(x=1000,y=470)

    def purchase():
        combomt=combom.get()
        comboc=combo.get()
        colours=txtcol.get()
        sizes=combosz.get()
       
        if (combomt=="" or comboc=="" or colours=="" or sizes==""):
            MessageBox.showinfo("Purchase Status","All Fields are required")
            #tshirt
        if combomt == "Tshirt":
            Database=mysql.connect(host="localhost",user="root",password="swetha123",database="thriftstore5")
            cursor=Database.cursor()
            rows = cursor.execute("select count(*) from tshirt WHERE Colour = '"+ colours +"' and Conditions = '"+ comboc +"' and Size = '"+ sizes +"';")
            x = cursor.fetchone()[0]
            tshirt2=int(x)
            #MessageBox.showinfo(x)
            #MessageBox.showinfo(type(tshirt2))
            if tshirt2>0:
                tshirt1 = "DELETE FROM Tshirt where Colour = '"+ colours +"' and Conditions = '"+ comboc +"' and Size = '"+ sizes +"';"
                cursor.execute(tshirt1)
                cursor.execute("commit");
                MessageBox.showinfo("Purchase status","Thank you for the purchase")
            else:
                MessageBox.showinfo("Purchase status","Out of Stock :(")
               
               

               
               
           
               
            #jacket
        if combomt == "Jacket":
            Database=mysql.connect(host="localhost",user="root",password="swetha123",database="thriftstore5")
            cursor=Database.cursor()
            rows = cursor.execute("select count(*) from Jacket WHERE Colour = '"+ colours +"' and Conditions = '"+ comboc +"' and Size = '"+ sizes +"';")
            x = cursor.fetchone()[0]
            tshirt2=int(x)
            #MessageBox.showinfo(x)
            #MessageBox.showinfo(type(tshirt2))
            if tshirt2>0:
                tshirt1 = "DELETE FROM Jacket where Colour = '"+ colours +"' and Conditions = '"+ comboc +"' and Size = '"+ sizes +"';"
                cursor.execute(tshirt1)
                cursor.execute("commit");
                MessageBox.showinfo("Purchase status","Thank you for the purchase")
            else:
                MessageBox.showinfo("Purchase status","Out of Stock :(")
               
           
               

            #jeans
        if combomt == "Jeans":
            Database=mysql.connect(host="localhost",user="root",password="swetha123",database="thriftstore5")
            cursor=Database.cursor()
            rows = cursor.execute("select count(*) from Jeans WHERE Colour = '"+ colours +"' and Conditions = '"+ comboc +"' and Size = '"+ sizes +"';")
            x = cursor.fetchone()[0]
            tshirt2=int(x)
            #MessageBox.showinfo(x)
            #MessageBox.showinfo(type(tshirt2))
            if tshirt2>0:
                tshirt1 = "DELETE FROM Jeans where Colour = '"+ colours +"' and Conditions = '"+ comboc +"' and Size = '"+ sizes +"';"
                cursor.execute(tshirt1)
                cursor.execute("commit");
                MessageBox.showinfo("Purchase status","Thank you for the purchase")
            else:
                MessageBox.showinfo("Purchase status","Out of Stock :(")
               
           

            #shirts
        if combomt == "Shirts":
            Database=mysql.connect(host="localhost",user="root",password="swetha123",database="thriftstore5")
            cursor=Database.cursor()
            rows = cursor.execute("select count(*) from Shirts WHERE Colour = '"+ colours +"' and Conditions = '"+ comboc +"' and Size = '"+ sizes +"';")
            x = cursor.fetchone()[0]
            tshirt2=int(x)
            #MessageBox.showinfo(x)
            #MessageBox.showinfo(type(tshirt2))
            if tshirt2>0:
                tshirt1 = "DELETE FROM Shirts where Colour = '"+ colours +"' and Conditions = '"+ comboc +"' and Size = '"+ sizes +"';"
                cursor.execute(tshirt1)
                cursor.execute("commit");
                MessageBox.showinfo("Purchase status","Thank you for the purchase")
            else:
                MessageBox.showinfo("Purchase status","Out of Stock :(")
               
   
               

            #pants
        if combomt == "Pants":
            Database=mysql.connect(host="localhost",user="root",password="swetha123",database="thriftstore5")
            cursor=Database.cursor()
            rows = cursor.execute("select count(*) from Pants WHERE Colour = '"+ colours +"' and Conditions = '"+ comboc +"' and Size = '"+ sizes +"';")
            x = cursor.fetchone()[0]
            tshirt2=int(x)
            #MessageBox.showinfo(x)
            #MessageBox.showinfo(type(tshirt2))
            if tshirt2>0:
                tshirt1 = "DELETE FROM Pants where Colour = '"+ colours +"' and Conditions = '"+ comboc +"' and Size = '"+ sizes +"';"
                cursor.execute(tshirt1)
                cursor.execute("commit");
                MessageBox.showinfo("Purchase status","Thank you for the purchase")
            else:
                MessageBox.showinfo("Purchase status","Out of Stock :(")
               
           

            #coats
        if combomt == "Coats":
            Database=mysql.connect(host="localhost",user="root",password="swetha123",database="thriftstore5")
            cursor=Database.cursor()
            rows = cursor.execute("select count(*) from Coats WHERE Colour = '"+ colours +"' and Conditions = '"+ comboc +"' and Size = '"+ sizes +"';")
            x = cursor.fetchone()[0]
            tshirt2=int(x)
            #MessageBox.showinfo(x)
            #MessageBox.showinfo(type(tshirt2))
            if tshirt2>0:
                tshirt1 = "DELETE FROM Coats where Colour = '"+ colours +"' and Conditions = '"+ comboc +"' and Size = '"+ sizes +"';"
                cursor.execute(tshirt1)
                cursor.execute("commit");
                MessageBox.showinfo("Purchase status","Thank you for the purchase")
            else:
                MessageBox.showinfo("Purchase status","Out of Stock :(")
               
       
           

           

    #Purchase button
    btp=Button(window,text="Let's Buy it",font=("Arial bold",18),bg="pink", command=purchase)
    btp.place(x=500,y=550)
    btp.config(height=2,width=20)
   
#Click to start buying button to go to the purchase portal
bt1=Button(window,text="Click to start buying!",font=('Arial bold',15),bg='skyblue',command=clicked2)
bt1.place(x=900,y=550)
bt1.config(height=4,width=25)
