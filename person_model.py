from mesa import Agent, Model
from mesa.time import RandomActivation

class PersonAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.isContaminated = False
        self.encountersWithContaminated = 0      


class PersonModel(Model):
    def __init__(self, N):
        self.number_of_agents = N

        for i in range(self.number_of_agents):
            agent = PersonAgent(i, self)