import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
import simulator as sim
import plotting as plot
import webscrape as webs
from tkinter import ttk

# Create the root (base) window where all widgets go
root = tk.Tk()   

# Title of Program
root.title("Simulating a Pandemic")

# Size of Program
root.geometry("1920x1080")

# Background Image
icon = tk.PhotoImage(file = "image.png")
background_image = tk.Label(root,image = icon)
background_image.place(x =-3,y =-3)
def custom_sim_window():
    cutom_sim = tk.Toplevel(root)
    
    # Size of Program
    cutom_sim.geometry("1050x630")

    # Background Image
    icon = tk.PhotoImage(file = "image.png")
    background_image = tk.Label(cutom_sim,image = icon)
    background_image.place(x =-3,y =-3)
    
    '''
    Declaring variables
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
    strictvar=tk.IntVar()

    '''
    Creating functions
    '''

    # Help message command
    def helpmsg():
        tk.messagebox.showinfo("userguide","Enter the inputs.\n The strictness checkbox if ticked, indicates that the people are following the guidelines strictly and we see the plot of the most ideal situation,\n otherwise there is some randomness in wearing masks and obeying lockdown as we all do :) \nClick the start simulator button to plot the graph.")

    # Input taking
    def start_sim():
        l=(sim.initiate_simulation(population.get(),total_days.get(),percentage_immuned.get(),starting_infectors.get(),contagiousness.get(),average_friends.get(),recovery_days.get(),mask_day.get(),lockdown_day.get(),lockdown_days.get(),strictvar.get()))
        plot.plotsim(l,"r")

    '''
    INPUTS
    '''
    L1 = tk.Label(cutom_sim, text="Population:",font=("Arial Bold",30),bg="blue")
    E1 = tk.Entry(cutom_sim,textvariable=population,bd=5)

    L2 = tk.Label(cutom_sim, text="Total Days:",font=("Arial Bold",30),bg="red")
    E2 = tk.Entry(cutom_sim,textvariable=total_days, bd =5)

    L3 = tk.Label(cutom_sim, text="Percentage immuned:",font=("Arial Bold",30),bg="blue")
    E3 = tk.Entry(cutom_sim,textvariable=percentage_immuned, bd =5)

    L4 = tk.Label(cutom_sim, text="Starting infectors:",font=("Arial Bold",30),bg="red")
    E4 = tk.Entry(cutom_sim,textvariable=starting_infectors, bd =5)

    L5 = tk.Label(cutom_sim, text="Contagiousness:",font=("Arial Bold",30),bg="blue")
    E5 = tk.Entry(cutom_sim,textvariable=contagiousness, bd =5)

    L6 = tk.Label(cutom_sim, text="Average friends:",font=("Arial Bold",30),bg="red")
    E6 = tk.Entry(cutom_sim,textvariable=average_friends, bd =5)

    L7 = tk.Label(cutom_sim, text="Recovery days:",font=("Arial Bold",30),bg="blue")
    E7 = tk.Entry(cutom_sim, textvariable=recovery_days,bd =5)

    L8 = tk.Label(cutom_sim, text="Mask day:",font=("Arial Bold",30),bg="red")
    E8 = tk.Entry(cutom_sim, textvariable=mask_day,bd =5)

    L9 = tk.Label(cutom_sim, text="Lockdown start day:",font=("Arial Bold",30),bg="blue")
    E9 = tk.Entry(cutom_sim, textvariable=lockdown_day,bd =5)

    L10 = tk.Label(cutom_sim, text="Lockdown days:",font=("Arial Bold",30),bg="red")
    E10 = tk.Entry(cutom_sim,textvariable=lockdown_days, bd =5)

    strict = tk.Checkbutton(cutom_sim, text = "Strict Rules", variable=strictvar,font=("Arial Bold",30))

    '''
    BUTTONS
    '''
    # Start sim button
    start_simulator = tk.Button(cutom_sim,text="Start Simulator",command=start_sim,font=("Arial Bold",50))

    # Help button
    help_button = tk.Button(cutom_sim,text="Help",command=helpmsg,font=("Arial Bold",50))

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
    strict.grid(row=7,column=2)
    L9.grid(row=8,column=0)
    E9.grid(row=8,column=1)
    L10.grid(row=9,column=0)
    E10.grid(row=9,column=1)
    start_simulator.grid(row=10,column=0)
    help_button.grid(row=10,column=1)

    cutom_sim.mainloop()

def automatic_sim_window():
    auto_sim = tk.Toplevel(root)
    
    # Geometry
    auto_sim.geometry("800x250")

    # Background Image
    icon = tk.PhotoImage(file = "image.png")
    background_image = tk.Label(auto_sim,image = icon)
    background_image.place(x =-3,y =-3)
    
    '''
    Declaring variables
    '''
    country = tk.StringVar()
    type_of_graph = tk.StringVar()
    
    '''
    Fuctions
    '''
    def help_button():
        tk.messagebox.showinfo("help","Sooraj enter a user guide here!")
    
    def start_sim():

        try:
            d1=webs.CovidData(country.get())
            if (type_of_graph.get() == "Cumlative cases Daywise"):
                plot.plotweb(list(d1.total_case_data()),country.get(),'c')
            elif (type_of_graph.get() == "New Daily Cases"):
                plot.plotweb(list(d1.daily_new_case_data()),country.get(),'c')
            elif (type_of_graph.get() == "Active Cases"):
                plot.plotweb(list(d1.active_case_data()),country.get(),'c')
            elif (type_of_graph.get() == "Deaths"):
                plot.plotweb(list(d1.deaths_data()),country.get(),'c')

        except Exception as e:
            # print(e)
            messagebox.showinfo("Error", e)

    '''
    Inputs
    '''
    L1 = tk.Label(auto_sim,text="Country name",font=("Arial Bold",30),bg="red")
    E1 = tk.Entry(auto_sim,textvariable=country,font=("Arial Bold",30))
    L2 = tk.Label(auto_sim,text="Graph type",font=("Arial Bold",30),bg="blue")
    C1=ttk.Combobox(auto_sim,width=25,textvariable=type_of_graph,font=("Arial Bold",20))
    C1['values']=('Cumlative cases Daywise','New Daily Cases','Active Cases','Deaths')
    
    '''
    Buttons
    '''
    B1 = tk.Button(auto_sim,text="Start\nSimulator",font=("Arial Bold",30),command=start_sim)
    B2 = tk.Button(auto_sim,text="Help",font=("Arial Bold",30),command=help_button)
    '''
    Arrangement
    '''
    L1.grid(row=0,column=0)
    E1.grid(row=0,column=1)
    L2.grid(row=1,column=0)
    C1.grid(row=1,column=1)
    B1.grid(row=2,column=0)
    B2.grid(row=2,column=1)

    auto_sim.mainloop()

B1 = tk.Button(root,text ="Custom \nSimulation",command = custom_sim_window,font=("Arial Bold",100))

B2 = tk.Button(root,text = "Automatic \nSimulation",command = automatic_sim_window,font=("Arial Bold",100))

B1.place(x=20,y=100)
B2.place(x=760,y=100)
# Start the event loop
root.mainloop()
