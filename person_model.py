from mesa import Agent, Model
from mesa.time import RandomActivation

class PersonAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.isContaminated = False
        self.encountersWithContaminated = 0      

    def step(self):
        contamination_level = "contaminated" if self.isContaminated else "not contaminated"
        print("Hi, I am agent " + str(self.unique_id) + " and I'm " + contamination_level)

class PersonModel(Model):
    def __init__(self, N):
        self.number_of_agents = N
        self.schedule = RandomActivation(self)

        for i in range(self.number_of_agents):
            agent = PersonAgent(i, self)
            self.schedule.add(agent)

    def step(self):
        self.schedule.step()