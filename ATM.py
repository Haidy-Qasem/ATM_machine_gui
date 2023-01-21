from tkinter import *
import time

window=Tk()
window.geometry("900x950")
window.title("ITI ATM")
window.configure(bg="navajo white")

top=Frame(window,width=800,height=50,bg="navajo white")
top.pack(side=TOP)
label_1=l=Label(top,font=(20),text="ITI ATM",fg="maroon",bg="navajo white",bd=10,anchor="w")
label_1.grid(row=0,column=3)

F1=Frame(window,bg="navajo white",width=400,height=700)
F1.pack(side=RIGHT)

F2=Frame(window,bg="navajo white",width=300,height=700)
F2.pack(side=LEFT)

num=StringVar()
amount=StringVar()
wthdrow=StringVar()

def bank_system_data ():
	global account_bal
	accounts_no=["0011","0022","0033"]
	account=num.get()
	if account in accounts_no :
		label.config(text="User in System")
		bank_system_data={"0011":1000,"0022":2000,"0033":4000}
		balance=bank_system_data[account]
		account_bal=balance
	else :
		label.config(text="User NOT in System")
btnsubmit=Button(F2,bd=5,text="Submit",bg="white",command=bank_system_data)
btnsubmit.grid(row=1,column=8)

def deposit ():
	global account_bal
	amo=float(amount.get())
	bal= account_bal+amo
	label3.config(text=("Minimum Balance:",str(bal)))
btndeposit=Button(F2,bd=5,text="Deposit",bg="white",command=deposit)
btndeposit.grid(row=4,column=8)

def withdrow():
	global account_bal
	wd=float(wthdrow.get())
	if account_bal >= wd:
		ace=account_bal-wd
		label4.config(text=("Balance=",str(ace)))
	else:
		label4.config(text="Insufficient Balance")
btnwithdrow=Button(F2,bd=5,text="Withdraw",bg="white",command=withdrow)
btnwithdrow.grid(row=8,column=8)		
	

def bal():
	global account_bal 
	label5.config(text=("Balance=",str(account_bal)))
btnbal=Button(F2,bd=5,text="Balance",bg="white",command=bal)
btnbal.grid(row=10,column=8)	


def reset ():
	num.set("")
	amount.set("")
	wthdrow.set("")
	label.config(text="")
	label3.config(text="")
	label4.config(text="")
	label5.config(text="")
btnreset=Button(F2,bd=5,text="Reset",bg="white",command=reset)
btnreset.grid(row=11,column=8)

		
label1=Label(F1,text="Enter Your Password",fg="maroon",bg="white",bd=10)
label1.grid(row=1,column=3)
text=Entry(F1,textvariable=num,insertwidth=4,fg="maroon",bg="white",bd=10)
text.grid(row=1,column=4)
label=Label(F1,fg="maroon",bg="white",bd=10)
label.grid(row=2,column=4)

lbl=Label(F1,text="Enter how much to deposit",fg="maroon",bg="white",bd=10)
lbl.grid(row=4,column=3)
text=Entry(F1,textvariable=amount,insertwidth=4,fg="maroon",bg="white",bd=10)
text.grid(row=4,column=4)
label3=Label(F1,fg="maroon",bg="white",bd=10)
label3.grid(row=5,column=4)

lbl=Label(F1,text="Enter how much to withdrow",fg="maroon",bg="white",bd=10)
lbl.grid(row=8,column=3)
text=Entry(F1,textvariable=wthdrow,insertwidth=4,fg="maroon",bg="white",bd=10,justify="right")
text.grid(row=8,column=4)
label4=Label(F1,fg="maroon",bg="white",bd=10)
label4.grid(row=9,column=4)
label5=Label(F1,fg="maroon",bg="white")
label5.grid(row=10,column=4)

btnexit=Button(F2,bd=5,text="Exit",bg="white",command=window.destroy)
btnexit.grid(row=12,column=8)

window.mainloop()
