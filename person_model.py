from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from person_agent import PersonAgent

width = 20
height = 20
class PersonModel(Model):
  def __init__(self, N):
      self.numAgents = N
      self.schedule = RandomActivation(self)
      self.grid = MultiGrid(width,height, True)
      self.running = True

      for i in range(self.numAgents):
          x = self.random.randrange(width)
          y = self.random.randrange(height)
          agent = PersonAgent(i, self)
          self.schedule.add(agent)
          self.grid.place_agent(agent, (x, y))
          if i == 0:
              agent.isContaminated = True
              agent.isTransmitter = True

  def step(self):
      self.schedule.step()
