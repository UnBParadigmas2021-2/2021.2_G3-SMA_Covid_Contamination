from mesa import Agent
from utils import width, height, get_tx

class PersonAgent(Agent):
    recoveryDay = 7

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.isContaminated = False
        self.isSymptomatic = False
        self.daysContaminated = 0
        self.isTransmitter = False
        self.isAlive = True

    def probabilityInfection(self, symptomatic):
        tx_transmission, _ =   get_tx()
        if tx_transmission < 0:
            if not symptomatic:
                return self.random.choices([True, False], [0.58, 0.42])[0]
            return True
        else:
            return self.random.choices([True, False], [tx_transmission, 1-tx_transmission])[0]

    
    def our_neighborhood(self):
        x, y = self.pos
        neighborhood = []
        if(x + 1 < width):
            neighborhood.append((x+1, y))
        if(x - 1 >= 0):
            neighborhood.append((x-1, y))
        if( y + 1 < height):
            neighborhood.append((x, y+1))
        if( y - 1 >= 0):
            neighborhood.append((x, y-1))

        return neighborhood
            
    def move(self):
        if self.isAlive:
            neighborhood = self.our_neighborhood()
            move_to = self.random.choice(neighborhood)
            self.model.grid.move_agent(self, move_to)
    
    def updateStatus(self):
        if self.daysContaminated == self.recoveryDay:
            self.isContaminated = False
            self.isTransmitter = False                

        if self.isContaminated:
            self.daysContaminated += 1
            if self.isSymptomatic:
                _, tx_death = get_tx()
                self.isAlive = self.random.choices([True, False], [ 1 - tx_death, tx_death ])[0]
        else:
            self.daysContaminated = 0

        if self.daysContaminated == 3:
            self.isTransmitter = True                

    def verifyContact(self):
        contact = self.model.grid.get_cell_list_contents([self.pos])

        for agent in contact:
            if self.isTransmitter and not agent.isContaminated and agent.isAlive:
                agent.isContaminated = self.probabilityInfection(
                    self.isSymptomatic)
                # if agent.isContaminated:
                #     print(f"Eu, agente {str(self.unique_id)}, contaminei o agente {str(agent.unique_id)}")
                # else:
                #     print(f"Eu, agente {str(self.unique_id)}, entrei em contato, mas não contaminei o agente {str(agent.unique_id)}")

            elif agent.isTransmitter and not self.isContaminated and agent.isAlive:
                self.isContaminated = self.probabilityInfection(
                    agent.isSymptomatic)
                if self.isContaminated:
                    self.isSymptomatic = self.random.choices([True, False],[0.7, 0.3])[0]
                #     print(f"Eu, agente {str(self.unique_id)}, fui contaminado pelo agente {str(agent.unique_id)}")
                # else:
                #     print(f"Eu, agente {str(self.unique_id)}, entrei em contato, mas não fui contaminado pelo agente {str(agent.unique_id)}")



    def printStatus(self, other_agent):
        contamination_level = "contaminated" if self.isContaminated else "not contaminated"
        # print("Hi, I am agent " + str(self.unique_id) +
        #       " and I'm " + contamination_level)

        print(f"{str(self.unique_id)} => {other_agent.unique_id}")

    def step(self):
        other_agent = self.random.choice(self.model.schedule.agents)

        while other_agent.unique_id == self.unique_id:
            other_agent = self.random.choice(self.model.schedule.agents)
        
        if self.isAlive:
            self.move()
            self.verifyContact()
            self.updateStatus()
      #  self.printStatus(other_agent)
