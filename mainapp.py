#from functions import *
from tkinter import *
from subprocess import Popen,PIPE
import subprocess
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import pandas as  pd
import numpy as np
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

nice_data= pd.DataFrame()
def password():
    passwd = simpledialog.askstring("Password","Enter your password",show="*",parent=window)
    return passwd
def update_cpu():
    users=[]
    cpu=[]


    command_u="chmod 777 user.sh"
    command_u1="./user.sh"
    os.system(command_u)
    os.system(command_u1)

    with open("users.txt") as file:
        #next(file)
        for line in file:
            line = line.strip() #or some other preprocessing
            users.append(line)
        users.append("root")
    print(users)

    for i in range(len(users)):
        print(users[i])
        command="chmod 777 cpu.sh"
        #subprocess.call(command)
        command2="./cpu.sh "+users[i]+""
        print(command2)
        os.system(command)
        os.system(command2)
        with open("cpu.txt") as cpu_file:
            lines = []
            #next(file)
            for line in cpu_file:
                line = line.strip() #or some other preprocessing
                lines.append(line)
            lines.pop(0)
            lines=list(map(float,lines))
            print(lines)
            cpu.append(sum(lines))
            print("cpu sum is ",sum(lines))

    print(cpu)
    print(users)

    figure2 = Figure(figsize=(5,4), dpi=100)
    subplot2 = figure2.add_subplot(111)
    labels2 = users
    pieSizes = cpu
    subplot2.pie(pieSizes, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90)
    subplot2.axis('equal')
    pie2 = FigureCanvasTkAgg(figure2,tab1_frame1)
    pie2.get_tk_widget().grid(row=3,column=4)

def update_memory():
    users=[]
    memory=[]

    with open("users.txt") as file:
        #next(file)
        for line in file:
            line = line.strip() #or some other preprocessing
            users.append(line)
        users.append("root")

    print(users)

    for i in range(len(users)):
        print(users[i])
        command3="chmod 777 memory.sh"
        #subprocess.call(command3)
        command4="./memory.sh "+users[i]+""
        #subprocess.call(command4)"""
        os.system(command3)
        os.system(command4)

        with open("memory.txt") as mem_file:
            lines = []
            #next(file)
            for line in mem_file:
                line = line.strip() #or some other preprocessing
                lines.append(line)
            lines.pop(0)
            lines=list(map(float,lines))
            print(lines)
            memory.append(sum(lines))
            print("memory sum is ",sum(lines))

    print(memory)
    print(users)

    figure2 = Figure(figsize=(5,4), dpi=100)
    subplot2 = figure2.add_subplot(111)
    labels2 = users
    pieSizes = memory
    subplot2.pie(pieSizes, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90)
    subplot2.axis('equal')
    pie2 = FigureCanvasTkAgg(figure2,mem_frame1)
    pie2.get_tk_widget().grid(row=3,column=4)

def update_nice():
    pid=[]
    cpu=[]

    command_u="chmod 777 pid.sh"
    command_u1="./pid.sh"
    os.system(command_u)
    os.system(command_u1)

    with open("pid.txt") as file:
        #next(file)
        for line in file:
            line = line.strip() #or some other preprocessing
            pid.append(line)
    print(pid)

    for i in range(len(pid)):
        print(users[i])
        command="chmod 777 nice.sh"
        #subprocess.call(command)
        command2="./cpu.sh "+users[i]+""
        print(command2)
        os.system(command)
        os.system(command2)
        with open("cpu.txt") as cpu_file:
            lines = []
            #next(file)
            for line in cpu_file:
                line = line.strip() #or some other preprocessing
                lines.append(line)
            lines.pop(0)
            lines=list(map(float,lines))
            print(lines)
            cpu.append(sum(lines))
            print("cpu sum is ",sum(lines))

    print(cpu)
    print(users)

def nice_data():
    command_u="chmod 777 pid.sh"
    command_u1="./pid.sh"
    os.system(command_u)
    os.system(command_u1)
    data=pd.read_csv("pid.csv",header=None)
    return data

nice_data=nice_data()
print(nice_data)

def update_nicevalue(pid,value):

    pid=str(pid)
    nice=str(value)
    password1=password()
    command3="echo "+password1+" | sudo -S renice "+nice+" "+pid+""
    print(command3)
    subprocess.call(command3,shell=True)
    messagebox.showinfo("sucess", "nice value updated")
    command_u="chmod 777 pid.sh"
    command_u1="./pid.sh"
    os.system(command_u)
    os.system(command_u1)
    nice_data=pd.read_csv("pid.csv",header=None)
    print(nice_data)
    ques3(nice_data)
    #command="chmod 777 nice.sh"
    #subprocess.call(command)
    #command2="./nice.sh "+newvalue+""
    #os.system(command)
    #os.system(command2)



window = Tk()
window.configure(background='lavender')

window.title('SYSTEM ADMIN TOOL')
note = ttk.Notebook(window)

tab1 = ttk.Frame(note)
tab2 = ttk.Frame(note)
tab3 = ttk.Frame(note)
tab4 = ttk.Frame(note)

note.add(tab1, text = "CPU")
note.add(tab2, text = "MEMORY")
note.add(tab3, text = "QUES-3")
note.add(tab4, text = "QUES-4")

note.pack(expand=1,fill="both")

#-----------------------------tab1 content---------------------------------------
tab2_frame1 =LabelFrame(tab1,text="CPU PIE",bg="lavender",bd=1,width=500, height=80)
tab2_frame1.grid(row=1, column=1)
tab1_frame1 =LabelFrame(tab1,text="PIE-CHART of CPU usage of different users",bd=2,bg="lavender",width=500, height=80)
tab1_frame1.grid(row=3, column=1,padx=30,pady=5)


button1 =Button (tab2_frame1, text='Start',padx=5,pady=5,command=update_cpu)
button1.grid(row=1,column=1,padx=10,pady=5)

button1 =Button (tab2_frame1, text='Update',bg="tan1",padx=5,pady=5,command=update_cpu)
button1.grid(row=1,column=2,padx=10,pady=5)

button1 =Button (tab2_frame1, text='Exit',bg="red", command=window.destroy)
button1.grid(row=1,column=3,padx=10,pady=5)
#-----------------------------tab2 content---------------------------------------
tab2_frame1 =LabelFrame(tab2,text="CPU PIE",bg="lavender",bd=1,width=500, height=80)
tab2_frame1.grid(row=1, column=1)
mem_frame1 =LabelFrame(tab2,text="PIE-CHART of MEMORY usage of different users",bd=2,bg="lavender",width=500, height=80)
mem_frame1.grid(row=3, column=1,padx=30,pady=5)


button1 =Button (tab2_frame1, text='Start',padx=5,pady=5,command=update_memory)
button1.grid(row=1,column=1,padx=10,pady=5)

button1 =Button (tab2_frame1, text='Update',bg="tan1",padx=5,pady=5,command=update_memory)
button1.grid(row=1,column=2,padx=10,pady=5)

button1 =Button (tab2_frame1, text='Exit',bg="red", command=window.destroy)
button1.grid(row=1,column=3,padx=10,pady=5)

#-----------------------------tab3 content---------------------------------------
def ques3(nice_data):
    tab3_frame1 =LabelFrame(tab3,text="UPDATING NICE VALUE",bd=5,fg="blue",bg="lavender"  ,width=500, height=80)
    tab3_frame1.grid(row=1, column=1,padx=30,pady=10)

    label1 = Label(tab3_frame1, text="PID",bg="lavender",padx=10, pady=1,borderwidth=2, relief="flat")
    label1.grid(row=1,column=1,padx=10,pady=5)

    label1 = Label(tab3_frame1, text="NICE VALUE",bg="lavender",padx=10, pady=1,borderwidth=2, relief="flat")
    label1.grid(row=1,column=3,padx=10,pady=5)

    label1 = Label(tab3_frame1, text="UPDATING VALUE",bg="lavender",padx=10, pady=1,borderwidth=2, relief="flat")
    label1.grid(row=1,column=5,padx=10,pady=5)

    e1_order=StringVar()
    e2_order=StringVar()
    e3_order=StringVar()
    e4_order=StringVar()
    e5_order=StringVar()

    for i in range(2,7):
        label1 = Label(tab3_frame1, text=nice_data.iloc[i-2,0],bg="light cyan",padx=10, pady=1,borderwidth=2, relief="groove")
        label1.grid(row=i,column=1,padx=10,pady=5)

        label1 = Label(tab3_frame1, text=nice_data.iloc[i-2,1],bg="light cyan",padx=10, pady=1,borderwidth=2, relief="groove")
        label1.grid(row=i,column=3,padx=10,pady=5)


    e1=Spinbox(tab3_frame1, from_=-20, to=19,width=8,textvariable=e1_order)
    e1.grid(row=2,column=5,padx=10, pady=1)

    e2=Spinbox(tab3_frame1, from_=-20, to=19,width=8,textvariable=e2_order)
    e2.grid(row=3,column=5,padx=10, pady=1)

    e3=Spinbox(tab3_frame1, from_=-20, to=19,width=8,textvariable=e3_order)
    e3.grid(row=4,column=5,padx=10, pady=1)

    e4=Spinbox(tab3_frame1, from_=-20, to=19,width=8,textvariable=e4_order)
    e4.grid(row=5,column=5,padx=10, pady=1)

    e5=Spinbox(tab3_frame1, from_=-20, to=19,width=8,textvariable=e5_order)
    e5.grid(row=6,column=5,padx=10, pady=1)

    button1 =Button (tab3_frame1, text='Update',bg="tan1",padx=5,pady=5,command=lambda: update_nicevalue(nice_data.iloc[0,0],e1_order.get()))
    button1.grid(row=2,column=7,padx=10,pady=5)

    button1 =Button (tab3_frame1, text='Update',bg="tan1",padx=5,pady=5,command=lambda: update_nicevalue(nice_data.iloc[1,0],e2_order.get()))
    button1.grid(row=3,column=7,padx=10,pady=5)

    button1 =Button (tab3_frame1, text='Update',bg="tan1",padx=5,pady=5,command=lambda: update_nicevalue(nice_data.iloc[2,0],e3_order.get()))
    button1.grid(row=4,column=7,padx=10,pady=5)

    button1 =Button (tab3_frame1, text='Update',bg="tan1",padx=5,pady=5,command=lambda: update_nicevalue(nice_data.iloc[3,0],e4_order.get()))
    button1.grid(row=5,column=7,padx=10,pady=5)

    button1 =Button (tab3_frame1, text='Update',bg="tan1",padx=5,pady=5,command=lambda: update_nicevalue(nice_data.iloc[4,0],e5_order.get()))
    button1.grid(row=6,column=7,padx=10,pady=5)

ques3(nice_data)


window.mainloop()
exit()
