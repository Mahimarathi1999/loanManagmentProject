from tkinter import*
from tkinter import ttk , messagebox
import pymysql

class customer:
    def __init__(self, root):
        self.root=root
        self.root.title=("Loan Management System")
        self.root.geometry('1350x720+0+0')
        title=Label(self.root, text='Loan Management System', font=('tmes new roman', 40,'bold') ,bg='yellow',fg='red' ,borderwidth=10 ,relief=GROOVE)
        title.pack(side=TOP, fill=X)

        # ==============Variables=========================
        self.id = StringVar()
        self.name = StringVar()
        self.mob = StringVar()
        self.adh = StringVar()
        self.ad = StringVar()
        self.pin = StringVar()
        self.amt = StringVar()
        self.emi = StringVar()
        self.tot = StringVar()
        self.rate = StringVar()
        self.time = StringVar()

        #============Details frame=================
        Detail_F= Frame(self.root ,bd=4, relief=RIDGE, bg='powderblue')
        Detail_F.place(x=10 ,y=90,width=580,height=600)

        lbl_id=Label(Detail_F ,text='Loan Id' , font=('times new romman', 17,'bold'))
        lbl_id.grid(row=0,column=0, padx=20, pady=10 , sticky='w')
        txt_id=Entry(Detail_F,font=('times new romman ', 17, 'bold'), bd=3,relief=GROOVE,textvariable=self.id)
        txt_id.grid(row=0,column=1)

        lbl_name=Label(Detail_F ,text='Full Name' , font=('times new romman', 17,'bold'))
        lbl_name.grid(row=1,column=0, padx=20, pady=10 , sticky='w')
        txt_name=Entry(Detail_F,font=('times new romman ', 17, 'bold'), bd=3,relief=GROOVE,textvariable=self.name)
        txt_name.grid(row=1,column=1)

        lbl_mob=Label(Detail_F ,text='Mobile No.' , font=('times new romman', 17,'bold'))
        lbl_mob.grid(row=2,column=0, padx=20, pady=10, sticky='w')
        txt_mob=Entry(Detail_F,font=('times new romman ', 17, 'bold'), bd=3,relief=GROOVE,textvariable=self.mob)
        txt_mob.grid(row=2,column=1)

        lbl_adh=Label(Detail_F ,text='Aadhar No.' , font=('times new romman', 17,'bold'))
        lbl_adh.grid(row=3,column=0, padx=20, pady=10, sticky='w')
        txt_adh=Entry(Detail_F,font=('times new romman ', 17, 'bold'), bd=3,relief=GROOVE,textvariable=self.adh)
        txt_adh.grid(row=3,column=1)

        lbl_ad=Label(Detail_F ,text='Address' , font=('times new romman', 17,'bold'))
        lbl_ad.grid(row=4,column=0, padx=20, pady=10, sticky='w')
        txt_ad=Entry(Detail_F,font=('times new romman ', 17, 'bold'), bd=3,relief=GROOVE,textvariable=self.ad)
        txt_ad.grid(row=4,column=1,pady=10,sticky="w")

        lbl_pin=Label(Detail_F ,text='PinCode' , font=('times new romman', 17,'bold'))
        lbl_pin.grid(row=5,column=0, padx=20, pady=10, sticky='w')
        txt_pin=Entry(Detail_F,font=('times new romman ', 17, 'bold'), bd=3,relief=GROOVE,textvariable=self.pin)
        txt_pin.grid(row=5,column=1,pady=10,sticky="w")

        lbl_amt=Label(Detail_F ,text='Loan Amount' , font=('times new romman', 17,'bold'))
        lbl_amt.grid(row=6,column=0, padx=20, pady=10, sticky='w')
        txt_amt=Entry(Detail_F,font=('times new roman ', 17, 'bold'), bd=3,relief=GROOVE,textvariable=self.amt)
        txt_amt.grid(row=6,column=1,pady=10,sticky="w")

        lbl_time=Label(Detail_F ,text='Number of years' , font=('times new romman', 17,'bold'))
        lbl_time.grid(row=7,column=0, padx=20, pady=10, sticky='w')
        txt_time=Entry(Detail_F,font=('times new romman ', 17, 'bold'), bd=3,relief=GROOVE,textvariable=self.time)
        txt_time.grid(row=7,column=1,pady=10,sticky="w")

        lbl_rate=Label(Detail_F ,text='Interest Rate' , font=('times new romman', 17,'bold'))
        lbl_rate.grid(row=8,column=0, padx=20, pady=10, sticky='w')
        txt_rate=Entry(Detail_F,font=('times new romman ', 17, 'bold'), bd=3,relief=GROOVE,textvariable=self.rate)
        txt_rate.grid(row=8,column=1,pady=10,sticky="w")

        lbl_emi=Label(Detail_F ,text='Monthly EMI' , font=('times new romman', 17,'bold'))
        lbl_emi.grid(row=9,column=0, padx=20, pady=10, sticky='w')
        txt_emi=Entry(Detail_F,font=('times new romman ', 17, 'bold'), bd=3,relief=GROOVE,state=DISABLED,textvariable=self.emi)
        txt_emi.grid(row=9,column=1,pady=10,sticky="w")

        lbl_tot=Label(Detail_F ,text='Total Payable Amount' , font=('times new romman', 17,'bold'))
        lbl_tot.grid(row=10,column=0, padx=20, pady=10, sticky='w')
        txt_tot=Entry(Detail_F,font=('times new romman ', 17, 'bold'), bd=3,relief=GROOVE,state=DISABLED,textvariable=self.tot)
        txt_tot.grid(row=10,column=1,pady=10,sticky="w")

        # ============Right frame=================
        RFrame = Frame(self.root, bd=4, relief=RIDGE)
        RFrame.place(x=595, y=90, width=745, height=525)

        yscroll = Scrollbar(RFrame, orient=VERTICAL)
        self.employee_table = ttk.Treeview(RFrame, column=('id', 'name', 'time', 'rate', 'emi', 'tot', 'mob'),yscrollcommand=yscroll.set)
        yscroll.pack(side=RIGHT, fill=Y)
        yscroll.config(command=self.employee_table.yview)
        self.employee_table.heading('id', text='Loan Id')
        self.employee_table.heading('name', text='Name')
        self.employee_table.heading('time', text='Loan Period')
        self.employee_table.heading('rate', text='Interest Rate')
        self.employee_table.heading('emi', text='Monthly EMI')
        self.employee_table.heading('tot', text='Total Payable')
        self.employee_table.heading('mob', text='Mobile No.')
        self.employee_table['show'] = 'headings'

        self.employee_table.column('id', width=100)
        self.employee_table.column('name', width=100)
        self.employee_table.column('time', width=100)
        self.employee_table.column('rate', width=100)
        self.employee_table.column('emi', width=100)
        self.employee_table.column('tot', width=100)
        self.employee_table.column('mob', width=100)

        self.employee_table.pack(fill=BOTH, expand=1)
        self.fetch()
        self.employee_table.bind("<ButtonRelease-1>",self.get_cursor)
        # ============Button frame=================
        btn_Frame = Frame(self.root, bd=4, relief=RIDGE)
        btn_Frame.place(x=595, y=590, width=745, height=100)

        btn1 = Button(btn_Frame, text='Add record', font='arial 14 bold', bg='limegreen', width=10,command=self.addrecord)
        btn1.grid(row=0, column=0, padx=10, pady=10)

        btn2 = Button(btn_Frame, text='Update', font='arial 14 bold', bg='limegreen', width=10,command=self.update)
        btn2.grid(row=0, column=1, padx=10, pady=10)

        btn3 = Button(btn_Frame, text='Delete', font='arial 14 bold', bg='limegreen', width=10,command=self.delete)
        btn3.grid(row=0, column=2, padx=10, pady=10)

        btn4 = Button(btn_Frame, text='Reset', font='arial 14 bold', bg='limegreen', width=10,command=self.reset)
        btn4.grid(row=0, column=3, padx=10, pady=10)

        btn5 = Button(btn_Frame, text='Exit', font='arial 14 bold', bg='limegreen', width=9,command=self.exit)
        btn5.grid(row=0, column=4, padx=10, pady=10)

# ====================Functions===================
    def total(self):
        p=int(self.amt.get())
        r=int(self.rate.get())
        n=int(self.time.get())
        t=(p*r*n*12)/100
        m=(p+t)/(n*12)
        self.emi.set(str(round(m,2)))
        self.tot.set(str(t+p))

    def addrecord(self):
        if self.id.get()=='' or self.amt.get=='':
               messagebox.showerror('Error ',' Customer details are must')
        else:
            self.total()
            con=pymysql.connect(host='localhost', user='root', password='', database='loanemp')
            cur = con.cursor()
            cur.execute("Select * from customer")
            rows=cur.fetchall()
            for row in rows:
                if row[0]==self.id.get():
                    messagebox.showerror('Error ','Duplicate entry not allowed')
                    return
            cur.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.id.get(),
                                                                                    self.name.get(),
                                                                                    self.time.get(),
                                                                                    self.rate.get(),
                                                                                    self.emi.get(),
                                                                                    self.tot.get(),
                                                                                    self.mob.get(),
                                                                                    self.adh.get(),
                                                                                    self.ad.get(),
                                                                                    self.pin.get(),
                                                                                    self.amt.get()))

        con.commit()
        self.fetch()
        con.close()

    def fetch(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='loanemp')
        cur = con.cursor()
        cur.execute("Select * from customer")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('',END , values=row)

        con.commit()
        con.close()

    def get_cursor(self,ev):
        cur_row=self.employee_table.focus()
        content=self.employee_table.item(cur_row)
        row=content['values']
        self.id.set(row[0])
        self.name.set(row[1])
        self.time.set(row[2])
        self.rate.set(row[3])
        self.emi.set(row[4])
        self.tot.set(row[5])
        self.mob.set(row[6])
        self.adh.set(row[7])
        self.ad.set(row[8])
        self.pin.set(row[9])
        self.amt.set(row[10])

    def update(self):
        if self.id.get=='':
            messagebox.showerror('Error','Input information for update')
        else:
            self.total()
            con = pymysql.connect(host='localhost', user='root', password='', database='loanemp')
            cur = con.cursor()
            cur.execute("update customer set Name=%s , Years=%s ,Rate=%s ,EMI=%s , Total_Payable_Amount=%s, Mobile_NUmber=%s ,Aadhar_Number=%s , Address=%s , Pin_code=%s, Amount=%s where Loan_id=%s", (self.name.get(),
                                                                                                                                                                                                   self.time.get(),
                                                                                                                                                                                                   self.rate.get(),
                                                                                                                                                                                                   self.emi.get(),
                                                                                                                                                                                                   self.tot.get(),
                                                                                                                                                                                                   self.mob.get(),
                                                                                                                                                                                                   self.adh.get(),
                                                                                                                                                                                                   self.ad.get(),
                                                                                                                                                                                                   self.pin.get(),
                                                                                                                                                                                                   self.amt.get(),
                                                                                                                                                                                                   self.id.get()))
            messagebox.showinfo('info',f'Record {self.id.get()} Updated Successfully')
            con.commit()
            self.fetch()
            con.close()
    def delete(self):
        if self.id.get=='':
            messagebox.showerror('Error','Input loan id to delete the record')
        else:
            con = pymysql.connect(host='localhost', user='root', password='', database='loanemp')
            cur = con.cursor()
            cur.execute("delete from customer where Loan_id=%s",self.id.get())
            con.commit()
            con.close()
            self.fetch()
            self.reset()

    def reset(self):
        self.id.set('')
        self.name.set('')
        self.mob.set('')
        self.adh.set('')
        self.ad.set('')
        self.pin.set('')
        self.amt.set('')
        self.emi.set('')
        self.tot.set('')
        self.rate.set('')
        self.time.set('')

    def exit(self):
        if messagebox.askyesno('Exit', 'Do you really want to exit?'):
            root.destroy()
root=Tk()
obj=customer(root)
root.mainloop()