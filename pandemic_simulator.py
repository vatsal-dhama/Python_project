from scipy.stats import norm
import random
import matplotlib.pyplot as plt 

class Person():
    def __init__(self,percentage_immuned,average_friends):
        if (random.randint(0,100)>percentage_immuned):
            self.immune = False
        else:
            self.immune = True
        self.mask = False
        self.contagiousness = 0
        self.friends = round((norm.rvs(loc=average_friends,scale=1.5,size=1))[0])
        self.days_under_pandemic = 0
    def wearMask(self):
        self.mask = True
        self.contagiousness /= 2

def initiate_simulation():
    # Collecting the inputs from the user
    People_List = []
    cases = []

    population = int(input("Enter the population : "))
    total_days = int(input("Enter the number of days for which the simulation should take place : "))
    percentage_immuned = int(input("Enter the percentage of people initially immune to the pandemic : "))
    starting_infectors = int(input("Enter the number of people who are initially infected : "))
    contagiousness = int(input("Enter the percentage chance of getting infected by a person who is already infected : "))
    average_friends = int(input("Enter the average number of people with whom one make interactions : "))
    recovery_days = int(input("Enter the number of days required to recover from the pandemic : "))
    mask_day = int(input("From which day should people start wearing masks (enter 0 for no masks) : "))
    lockdown_day = int(input("From which day should lockdown be implemented (enter 0 for no lockdown) : "))
    lockdown_days = int(input("Enter the number of days for which lockdown should be implemented : ")) 
    
    for i in range(population):
        People_List.append(Person(percentage_immuned,average_friends))

    infectors_index_list = random.sample(range(0,population-1),starting_infectors)
    for index in infectors_index_list:
        People_List[index].immune = False
        People_List[index].contagiousness = round(norm.rvs(size = 1,loc = contagiousness,scale = 1.5)[0])
    
    cases.append(starting_infectors)

    # Starting the simulation
    current_day = 1
    while(current_day <= total_days):
        
        for i in People_List:
            if (i.contagiousness > 0):
                i.days_under_pandemic += 1
                
                if ((current_day >= lockdown_day) and (current_day <= lockdown_day + lockdown_days)):
                    friends_met = 0
                else:
                    try:
                        friends_met = random.randint(0,i.friends)
                    except:
                        friends_met = 0
                
                if (mask_day != 0):
                    if (current_day >= mask_day):
                        if(i.mask == False):
                            i.wearMask()

                index_of_friends = random.sample(range(0,population-1),friends_met)
                for j in index_of_friends:
                    if (People_List[j].contagiousness == 0) and (People_List[j].immune == False):
                        if(random.randint(0,100)<i.contagiousness):
                            People_List[j].contagiousness = round(norm.rvs(size = 1,loc = contagiousness,scale = 1.5)[0])
                if (i.days_under_pandemic == recovery_days):
                    i.contagiousness = 0
                    i.immune = True

        cases_per_day = 0
        for i in People_List:
            if (i.contagiousness > 0):
                cases_per_day += 1
        cases.append(cases_per_day)

        if cases_per_day == 0:
            break

        current_day += 1
    

    plt.plot(cases)
    plt.show()

initiate_simulation()
    