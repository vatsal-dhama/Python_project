from scipy.stats import norm
import random

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

def initiate_simulation(population,total_days,percentage_immuned,starting_infectors,contagiousness,average_friends,recovery_days,mask_day,lockdown_day,lockdown_days,strict):
    
    People_List = []
    cases = []
    
    for i in range(population):
        People_List.append(Person(percentage_immuned,average_friends))

    infectors_index_list = random.sample(range(0,population-1),starting_infectors)
    
    for index in infectors_index_list:
        People_List[index].immune = False
        People_List[index].contagiousness = round(norm.rvs(size = 1,loc = contagiousness,scale = 1.5)[0])
    
    cases.append(starting_infectors)

    current_day = 1
    
    while(current_day <= total_days):
        
        for i in People_List:
                if (i.contagiousness > 0):
                    i.days_under_pandemic += 1
                
                if ((current_day >= lockdown_day) and (current_day <= lockdown_day + lockdown_days) and (lockdown_day!=0)):
                    
                    if(strict == 0):
                        try:
                            friends_met = random.randint(0,i.friends/4) # assuming a person meets at most 25% of his friends during lockdown
                        except:
                            friends_met = 0
                    else:
                        friends_met = 0
                    
                else:
                    try:
                        friends_met = random.randint(0,i.friends)
                    except:
                        friends_met = 0
                
                if (mask_day != 0):
                    
                    if (current_day >= mask_day):
                            
                        if(strict == 1):
                            
                            if(i.mask == True):
                                    i.contagiousness *= 2
                                    i.mask = False

                            i.wearMask()
                        
                        else:
                            
                            if(i.mask == True):
                                    i.contagiousness *= 2
                                    i.mask = False

                            if(random.randint(0,100) <= 75): # assuming 75% chance that the person will wear mask 
                                i.wearMask()

                index_of_friends = random.sample(range(0,population-1),friends_met)
                
                for j in index_of_friends:
                    
                    if ((People_List[j].contagiousness == 0) and (People_List[j].immune == False)):
                        
                        if(People_List[j].mask == True):
                            if(random.randint(0,100)<i.contagiousness/2):
                                People_List[j].contagiousness = round(norm.rvs(size = 1,loc = contagiousness,scale = 1.5)[0])
                                People_List[j].mask = False
                        else:
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

    return(cases)
    
