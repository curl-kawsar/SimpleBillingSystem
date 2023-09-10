from tkinter import *
from tkinter import messagebox
import tempfile
import os

root=Tk()
root.title('Billing System')
root.geometry('1280x720')
bg_color='#2D9290'


#=====================variables===================
Bread=IntVar()
Wine=IntVar()
Rice=IntVar()
Gal=IntVar()
Total=IntVar()

cb=StringVar()
cw=StringVar()
cr=StringVar()
cg=StringVar()
total_cost=StringVar()
# ===========Function===============
def total():
    if Bread.get()==0 and Wine.get()==0 and Rice.get()==0 and Gal.get()==0:
        messagebox.showerror('Error','Please select number of quantity')
    else:
        b=Bread.get()
        w=Wine.get()
        r=Rice.get()
        g=Gal.get()

        t=float(b*145+w*115+r*110+g*10)
        Total.set(b + w + r + g)
        total_cost.set('৳ ' + str(round(t, 2)))

        cb.set('৳ '+str(round(b * 145, 2)))
        cw.set('৳ '+str(round(w*115,2)))
        cr.set('৳ '+str(round(r*110,2)))
        cg.set('৳ '+str(round(g*10,2)))






def receipt():
    textarea.delete(1.0,END)
    textarea.insert(END,' আইটেম\t          পরিমাণ\t\t      মূল্য')
    textarea.insert(END, f"\n================================")
    textarea.insert(END,f'\n চাল\t\t{Bread.get()}\t  {cb.get()}')
    textarea.insert(END,f'\n\n ডাল\t\t{Wine.get()}\t  {cw.get()}')
    textarea.insert(END,f'\n\n চিনি\t\t{Rice.get()}\t  {cr.get()}')
    textarea.insert(END,f'\n\n ডিম\t\t{Gal.get()}\t  {cg.get()}')
    textarea.insert(END, f"\n\n================================")
    textarea.insert(END,f'\nমোট দাম\t\t{Total.get()}\t{total_cost.get()}')
    


def print():
    q=textarea.get('1.0','end-1c')
    filename=tempfile.mktemp('.txt')
    open(filename,'w').write(q)
    os.startfile(filename,'Print')


def reset():
    textarea.delete(1.0,END)
    Bread.set(0)
    Wine.set(0)
    Rice.set(0)
    Gal.set(0)
    Total.set(0)

    cb.set('')
    cw.set('')
    cr.set('')
    cg.set('')
    total_cost.set('')

def exit():
    if messagebox.askyesno('Exit','আপনি কি সত্যিই প্রস্থান করতে চান?'):
        root.destroy()

title=Label(root,pady=5,text="SIMPLE BILLING SYSTEM BY FOLDCURL",bd=12,bg="green",fg='white',font=('times new roman', 35 ,'bold'),relief=GROOVE,justify=CENTER)
title.pack(fill=X)

#===============Product Details=================
F1 = LabelFrame(root, text='পণ্যের বিবরণ', font=('times new roman', 18, 'bold'), fg='gold',bg=bg_color,bd=15,relief=RIDGE)
F1.place(x=5, y=90,width=800,height=500)

#=====================Heading==========================
itm=Label(F1, text='আইটেম', font=('Helvetic',25, 'bold'), fg='black',bg=bg_color)
itm.grid(row=0,column=0,padx=20,pady=15)

n=Label(F1, text='পরিমাণ', font=('Helvetic',25, 'bold'), fg='black',bg=bg_color)
n.grid(row=0,column=1,padx=30,pady=15)

cost=Label(F1, text='মূল্য', font=('Helvetic',25, 'bold'), fg='black',bg=bg_color)
cost.grid(row=0,column=2,padx=30,pady=15)

#===============Product============

bread=Label(F1, text='চাল', font=('times new rommon',15, 'bold'),fg='lawngreen',bg=bg_color)
bread.grid(row=1,column=0,padx=20,pady=15)
b_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Bread,justify=CENTER)
b_txt.grid(row=1,column=1,padx=20,pady=15)
cb_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cb,justify=CENTER)
cb_txt.grid(row=1,column=2,padx=20,pady=15)

wine=Label(F1, text='ডাল', font=('times new rommon',15, 'bold'), fg='lawngreen',bg=bg_color)
wine.grid(row=2,column=0,padx=20,pady=15)
w_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Wine,justify=CENTER)
w_txt.grid(row=2,column=1,padx=20,pady=15)
cw_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cw,justify=CENTER)
cw_txt.grid(row=2,column=2,padx=20,pady=15)

rice=Label(F1, text='চিনি', font=('times new rommon',15, 'bold'), fg='lawngreen',bg=bg_color)
rice.grid(row=3,column=0,padx=20,pady=15)
r_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Rice,justify=CENTER)
r_txt.grid(row=3,column=1,padx=20,pady=15)
cr_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cr,justify=CENTER)
cr_txt.grid(row=3,column=2,padx=20,pady=15)

gal=Label(F1, text='ডিম', font=('times new rommon',15, 'bold'), fg='lawngreen',bg=bg_color)
gal.grid(row=4,column=0,padx=20,pady=15)
g_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Gal,justify=CENTER)
g_txt.grid(row=4,column=1,padx=20,pady=15)
cg_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cg,justify=CENTER)
cg_txt.grid(row=4,column=2,padx=20,pady=15)

t=Label(F1, text='মোট', font=('times new rommon',18, 'bold'), fg='lawngreen',bg=bg_color)
t.grid(row=5,column=0,padx=20,pady=15)
t_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Total,justify=CENTER)
t_txt.grid(row=5,column=1,padx=20,pady=15)
totalcost_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=total_cost,justify=CENTER)
totalcost_txt.grid(row=5,column=2,padx=20,pady=15)

#=====================Bill areea====================
F2=Frame(root,relief=GROOVE,bd=10)
F2.place(x=820,y=90,width=430,height=500)
bill_title=Label(F2,text='রসিদ',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F2,orient=VERTICAL)
scrol_y.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15',yscrollcommand=scrol_y.set)
textarea.pack(fill=BOTH)
scrol_y.config(command=textarea.yview)



#=====================Buttons========================
F3 =Frame(root,bg=bg_color,bd=15,relief=RIDGE)
F3.place(x=5, y=590,width=1270,height=120)

btn1 = Button(F3, text='মোট', font='arial 25 bold', padx=5, pady=5, bg='green',fg='white',width=10,command=total)
btn1.grid(row=0,column=0,padx=20,pady=10)

btn2 = Button(F3, text='রসিদ', font='arial 25 bold', padx=5, pady=5, bg='green',fg='white',width=10,command=receipt)
btn2.grid(row=0,column=1,padx=10,pady=10)

btn3 = Button(F3, text='ছাপান', font='arial 25 bold', padx=5, pady=5, bg='green',fg='white',width=10,command=print)
btn3.grid(row=0,column=2,padx=10,pady=10)

btn4 = Button(F3, text='রিসেট', font='arial 25 bold', padx=5, pady=5, bg='green',fg='white',width=10,command=reset)
btn4.grid(row=0,column=3,padx=10,pady=10)

btn5 = Button(F3, text='বাহির', font='arial 25 bold', padx=5, pady=5, bg='green',fg='white',width=10,command=exit)
btn5.grid(row=0,column=4,padx=10,pady=10)





root.mainloop()