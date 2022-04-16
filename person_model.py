from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from person_agent import PersonAgent
from random import randrange

width = 20
height = 20

def genPos():
    x = randrange(width)
    y = randrange(height)
    return x, y

class PersonModel(Model):
  def __init__(self, N):
      self.numAgents = N
      self.schedule = RandomActivation(self)
      self.grid = MultiGrid(width,height, True)
      self.running = True
      self.filledPositions = []

      for i in range(self.numAgents):
          x, y = genPos()
          while (x,y) in self.filledPositions:
            x, y = genPos()
          self.filledPositions.append((x,y))
          agent = PersonAgent(i, self)
          self.schedule.add(agent)
          self.grid.place_agent(agent, (x, y))
          if i == 0:
              agent.isContaminated = True
              agent.isTransmitter = True

  def step(self):
      self.schedule.step()
      

