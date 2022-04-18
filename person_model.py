from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from person_agent import PersonAgent
from utils import width, height, update_tx
from random import randrange

def genPos():
    x = randrange(width)
    y = randrange(height)
    return x, y

class PersonModel(Model):
  def __init__(self, persons, initial_infected, tx_death, tx_transmission):
        self.numAgents = persons
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(width,height, True)
        self.running = True
        self.filledPositions = []
        update_tx(tx_death,tx_transmission)
        print("Valores atualizados")

        for i in range(self.numAgents):
            x, y = genPos()
            while (x,y) in self.filledPositions:
                x, y = genPos()
            self.filledPositions.append((x,y))
            agent = PersonAgent(i, self)
            self.schedule.add(agent)
            self.grid.place_agent(agent, (x , y))
            if i < initial_infected:
                agent.isContaminated = True
                agent.isTransmitter = True

  def step(self):
        self.schedule.step()
