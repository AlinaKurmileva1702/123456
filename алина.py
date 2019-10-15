from tkinter import*

root=Tk()
root.title("Численность популяций")
root.geometry("500x500")
lb_neogr=Label(root,text="Неограниченный рост",width=51,bg="red")
lb_neogr.place(x=45,y=20)

lb_a=Label(root,text="a",bg="red",width=2)
lb_a.place(x=10,y=50)

ent_a=Entry(root,bg="white",width=10)
ent_a.place(x=45,y=50)

bt_1=Button(root,text="Неограниченный рост",width=10)
bt_1.place(x=145,y=50)

lb_Xn1=Label(root,text="Xn",bg="orange",width=2)
lb_Xn1.place(x=250,y=50)

lb_Xn1_otv=Label(root,bg="white",width=18)
lb_Xn1_otv.place(x=280,y=50)

lb_ogr=Label(root,text="Ограниченный рост",width=51,bg="orange")
lb_ogr.place(x=45,y=80)

lb_b=Label(root,text="b",bg="yellow",width=2)
lb_b.place(x=10,y=110)

ent_b=Entry(root,bg="white",width=10)
ent_b.place(x=45,y=110)

bt_2=Button(root,text="Ограниченный рост",width=10)
bt_2.place(x=145,y=110)

lb_Xn2=Label(root,text="Xn",bg="green",width=2)
lb_Xn2.place(x=250,y=110)

lb_Xn2_otv=Label(root,bg="white",width=12)
lb_Xn2_otv.place(x=280,y=110)

lb_ogr2=Label(root,text="Ограниченный рост с отловом",width=51,bg="yellow")
lb_ogr2.place(x=45,y=140)

lb_a=Label(root,text="c",bg="blue",width=2)
lb_a.place(x=10,y=170)

ent_c=Entry(root,bg="white",width=10)
ent_c.place(x=45,y=170)

bt_3=Button(root,text="Ограниченный рост с отловом",width=10)
bt_3.place(x=145,y=170)

lb_Xn3=Label(root,text="Xn",bg="purple",width=2)
lb_Xn3.place(x=250,y=170)

lb_Xn3_otv=Label(root,bg="white",width=12)
lb_Xn3_otv.place(x=280,y=170)

lb_ger=Label(root,text="Жертва-Хищник",width=51,bg="green")
lb_ger.place(x=45,y=200)

lb_d=Label(root,text="d",bg="red",width=2)
lb_d.place(x=10,y=230)

ent_d=Entry(root,bg="white",width=5)
ent_d.place(x=35,y=230)

bt_4=Button(root,text="Жертва-хищник",width=10)
bt_4.place(x=210,y=230)

lb_f=Label(root,text="f",bg="orange",width=2)
lb_f.place(x=75,y=230)

ent_f=Entry(root,bg="white",width=5)
ent_f.place(x=100,y=230)

lb_q=Label(root,text="q",bg="yellow",width=2)
lb_q.place(x=140,y=230)

ent_q=Entry(root,bg="white",width=5)
ent_q.place(x=165,y=230)

lb_Xn4=Label(root,text="Жер.",bg="green",width=3)
lb_Xn4.place(x=220,y=270)

lb_Xn4_otv=Label(root,bg="white",width=8)
lb_Xn4_otv.place(x=245,y=270)

lb_Yn=Label(root,text="Хищ.",bg="blue",width=3)
lb_Yn.place(x=320,y=270)

lb_Yn_otv=Label(root,bg="white",width=8)
lb_Yn_otv.place(x=345,y=270)

lb_x1=Label(root,text="Жер.",bg="orange",width=5)
lb_x1.place(x=10,y=260)

ent_x1=Entry(root,bg="white",width=6)
ent_x1.place(x=55,y=260)

lb_y1=Label(root,text="Хищ.",bg="yellow",width=5)
lb_y1.place(x=10,y=290)

ent_y1=Entry(root,bg="white",width=6)
ent_y1.place(x=55,y=290)

lb_n=Label(root,text="a",bg="green",width=2)
lb_n.place(x=10,y=320)

ent_n=Entry(root,bg="white",width=10)
ent_n.place(x=55,y=320)

canv=Canvas(root,width=260,height=130,bg="white")
canv.place(x=140,y=300)

bt=Button(root,text="График",width=10)
bt.place(x=12,y=350)

def neogr_rost(event):
    a = float(ent_a.get())
    N = int(ent_n.get())
    gertv = int(ent_x1.get())

    for i in range(N):
        gertv = gertv*a

    lb_Xn1_otv["text"] = str(int(gertv))
        
bt_1.bind("<Button-1>",neogr_rost)

def ogr_rost(event):
    a = float(ent_a.get())
    b = float(ent_b.get())
    N = int(ent_n.get())
    gertv = int(ent_x1.get())

    for i in range(N):
        gertv =(a-b*gertv)*gertv

    lb_Xn2_otv["text"] = str(int(gertv))
        
bt_2.bind("<Button-1>",ogr_rost)

def ogr_rost_s_otlovom(event):
    a = float(ent_a.get())
    b = float(ent_b.get())
    c = float(ent_c.get())
    N = int(ent_n.get())
    gertv = int(ent_x1.get())

    for i in range(N):
        gertv =(a-b*gertv)*gertv-c

    lb_Xn3_otv["text"] = str(int(gertv))
        
bt_3.bind("<Button-1>",ogr_rost_s_otlovom)

def xichnik_gertva(event):
    a = float(ent_a.get())
    b = float(ent_b.get())
    c = float(ent_c.get())
    d= float(ent_d.get())
    f = float(ent_f.get())
    q = float(ent_q.get())
    N = int(ent_n.get())
    gertv = int(ent_x1.get())
    xichnik = int(ent_y1.get())
    
    for i in range(N):
        xichnik=d*xichnik+q*gertv*xichnik
        gertv =(a-b*gertv)*gertv-c-f*gertv*xichnik
        
        
    lb_Xn4_otv["text"] = str(int(gertv))
    lb_Yn_otv["text"] = str(int(xichnik))
        
bt_4.bind("<Button-1>",xichnik_gertva)

root.mainloop()
