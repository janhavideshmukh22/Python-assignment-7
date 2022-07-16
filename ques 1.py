from tkinter import *
def get_gst():
    a=int(netprice_t.get())
    b=int(originalcost_t.get())
    display.insert(0,f'GST rate ={((a-b)*100)/b}')

k=Tk()
k.title("GST rate calculator")
k.geometry('400x300')
k.config(bg='#0f4b6e')

netprice_t=Entry(k)
originalcost_t=Entry(k)

netprice_lbl=Label(k,text='Net Price',bg='#0f4b6e',fg='white')
originalcost_lbl=Label(k,text='Original Cost',bg='#0f4b6e',fg='white')

netprice_lbl.pack()
netprice_t.pack()
originalcost_lbl.pack()
originalcost_t.pack()

bt=Button(k,text="Get GST Rate",relief='solid',command=get_gst)
bt.pack(pady=10)

display=Entry(k,width=38,font=('Arial',14))
display.pack(pady=5)
k.mainloop()
