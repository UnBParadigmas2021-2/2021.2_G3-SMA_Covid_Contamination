from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from person_agent import PersonAgent
from utils import width, height, update_tx


class PersonModel(Model):
  def __init__(self, persons, initial_infected, tx_death, tx_transmission):
        self.numAgents = persons
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(width,height, True)
        self.running = True
        update_tx(tx_death,tx_transmission)
        print("Valores atualizados")

        for i in range(self.numAgents):
            x = self.random.randrange(width)
            y = self.random.randrange(height)
            agent = PersonAgent(i, self)
            self.schedule.add(agent)
            self.grid.place_agent(agent, (x , y))
            if i < initial_infected:
                agent.isContaminated = True
                agent.isTransmitter = True

  def step(self):
        self.schedule.step()
