from tkinter import *
import calendar
def disp_cal():
    n=Tk()
    n.title('Calender')
    n.geometry('700x600')
    
    year=int(enter_year.get())
    cal=calendar.calendar(year)
    cal_disp=Label(n,text=cal,font = "Consolas 10 bold")
    cal_disp.grid(row = 5, column = 1, padx = 80)
    n.mainloop() 
k=Tk()
k.title("Year specification")
k.geometry('400x300')
k.config(bg='#0f4b6e')

year_t=Label(k,text='Enter year',bg='#0f4b6e',fg='white')
enter_year=Entry(k)

year_t.pack()
enter_year.pack()

bt=Button(k,text='Display Calender',relief='solid',command=disp_cal)
bt.pack()
k.mainloop()
