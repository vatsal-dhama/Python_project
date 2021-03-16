import tkinter as tk
from tkinter import messagebox
import simulator as sim
import manish as plot

# Create the root (base) window where all widgets go
root = tk.Tk()   

# Title of Program
root.title("Simulating a Pandemic")

# Size of Program
root.geometry("1280x720")

# Menubar created
menubar = tk.Menu(root)

# Background Image
icon = tk.PhotoImage(file = "image.png")
background_image = tk.Label(root,image = icon)
background_image.place(x =-3,y =-3)
'''
Declaring string variables
'''
population=tk.IntVar()
total_days=tk.IntVar()
percentage_immuned=tk.DoubleVar()
starting_infectors=tk.IntVar()
contagiousness=tk.DoubleVar()
average_friends=tk.IntVar()
recovery_days=tk.IntVar()
mask_day=tk.IntVar()
lockdown_day=tk.IntVar()
lockdown_days=tk.IntVar()

'''
 Creating functions
'''
# Exit button command
def exit_button_pushed():
    global root
    root.destroy()  # Kill the root window

# Help message command
def helpmsg():
    tk.messagebox.showinfo("userguide","this is user guide")

# Credits message command
def credits_msg():
    tk.messagebox.showinfo("credits","gui creater OP🔥")

# Input taking
def start_sim():
    l=(sim.initiate_simulation(population.get(),total_days.get(),percentage_immuned.get(),starting_infectors.get(),contagiousness.get(),average_friends.get(),recovery_days.get(),mask_day.get(),lockdown_day.get(),lockdown_days.get()))
    plot.plotweb(l,"simulation","r")
'''
INPUTS
'''
#population,total_days,percentage_immuned,starting_infectors,contagiousness,average_friends,recovery_days,mask_day,lockdown_day,lockdown_days
L1 = tk.Label(root, text="Enter Population:"  )
E1 = tk.Entry(root,textvariable=population,bd=5)

L2 = tk.Label(root, text="Enter Total Days:")
E2 = tk.Entry(root,textvariable=total_days, bd =5)

L3 = tk.Label(root, text="Enter Percentage immuned:")
E3 = tk.Entry(root,textvariable=percentage_immuned, bd =5)

L4 = tk.Label(root, text="Enter Starting infectors:")
E4 = tk.Entry(root,textvariable=starting_infectors, bd =5)

L5 = tk.Label(root, text="Enter Contagiousness:")
E5 = tk.Entry(root,textvariable=contagiousness, bd =5)

L6 = tk.Label(root, text="Enter Average friends:")
E6 = tk.Entry(root,textvariable=average_friends, bd =5)

L7 = tk.Label(root, text="Enter Recovery days:")
E7 = tk.Entry(root, textvariable=recovery_days,bd =5)

L8 = tk.Label(root, text="Enter Mask day:")
E8 = tk.Entry(root, textvariable=mask_day,bd =5)

L9 = tk.Label(root, text="Enter Lockdown day:")
E9 = tk.Entry(root, textvariable=lockdown_day,bd =5)

L10 = tk.Label(root, text="Enter Lockdown days:")
E10 = tk.Entry(root,textvariable=lockdown_days, bd =5)

# Start sim button
start_simulator = tk.Button(root,text="Start Simulator",command=start_sim,font=("Arial Bold",50))

# Credits button
credits_button = tk.Button(root,text="Credits",command=credits_msg,font=("Arial Bold",50))

# Help button
help_button = tk.Button(root,text="Help",command=helpmsg,font=("Arial Bold",50))

# Exit button
exit_button = tk.Button(root, text = "Exit", command = exit_button_pushed , font=("Arial Bold",50))

'''
ARRANGEMENT

'''
L1.grid(row=0,column=0)
E1.grid(row=0,column=1)
L2.grid(row=1,column=0)
E2.grid(row=1,column=1)
L3.grid(row=2,column=0)
E3.grid(row=2,column=1)
L4.grid(row=3,column=0)
E4.grid(row=3,column=1)
L5.grid(row=4,column=0)
E5.grid(row=4,column=1)
L6.grid(row=5,column=0)
E6.grid(row=5,column=1)
L7.grid(row=6,column=0)
E7.grid(row=6,column=1)
L8.grid(row=7,column=0)
E8.grid(row=7,column=1)
L9.grid(row=8,column=0)
E9.grid(row=8,column=1)
L10.grid(row=9,column=0)
E10.grid(row=9,column=1)
start_simulator.grid(row=10,column=0)
credits_button.grid(row=11,column=0)
help_button.grid(row=10,column=1)
exit_button.grid(row=11,column=1)

# Start the event loop
root.config(menu=menubar)
root.mainloop()
