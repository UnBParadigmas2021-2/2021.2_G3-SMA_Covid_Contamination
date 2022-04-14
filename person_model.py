from mesa import Agent, Model
from mesa.time import RandomActivation


class PersonAgent(Agent):
    recoveryDay = 7

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.isContaminated = False
        # self.encountersWithContaminated = 0
        self.isSymptomatic = True
        self.daysContaminated = 0
        self.isTransmitter = False

    def probabilityInfection(self, symptomatic):
        if not symptomatic:
            return self.random.choices([True, False], [0.58, 0.42])[0]

        return True

    def updateStatus(self):
        if self.daysContaminated == self.recoveryDay:
            self.isContaminated = False

        if self.isContaminated:
            self.daysContaminated += 1
        else:
            self.daysContaminated = 0

    def verifyContact(self):
        other_agent = self.random.choice(self.model.schedule.agents)

        if self.isContaminated == True:
            other_agent.isContaminated = True

        elif other_agent.isContaminated == True:
            self.probabilityCalculator(other_agent.isSymptomatic)
            self.isContaminated = True
            self.isSymptomatic = self.random.choice([True, False])

    def printStatus(self):
        contamination_level = "contaminated" if self.isContaminated else "not contaminated"
        print("Hi, I am agent " + str(self.unique_id) +
              " and I'm " + contamination_level)

    def step(self):

        self.verifyContact()
        self.updateStatus()
        self.printStatus()


class PersonModel(Model):
    def __init__(self, N):
        self.number_of_agents = N
        self.schedule = RandomActivation(self)

        for i in range(self.number_of_agents):
            agent = PersonAgent(i, self)
            self.schedule.add(agent)

            if i == 0:
                agent.isContaminated = True

    def step(self):
        self.schedule.step()
