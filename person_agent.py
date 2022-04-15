from mesa import Agent

class PersonAgent(Agent):
    recoveryDay = 7

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.isContaminated = False
        self.isSymptomatic = False
        self.daysContaminated = 0
        self.isTransmitter = False

    def probabilityInfection(self, symptomatic):
        if not symptomatic:
            return self.random.choices([True, False], [0.58, 0.42])[0]
        return True

    def updateStatus(self):
        if self.daysContaminated == self.recoveryDay:
            self.isContaminated = False
            self.isTransmitter = False                

        if self.isContaminated:
            self.daysContaminated += 1
        else:
            self.daysContaminated = 0

        if self.daysContaminated == 3:
            self.isTransmitter = True                

    def verifyContact(self, other_agent):

        if self.isTransmitter and not other_agent.isContaminated:
            other_agent.isContaminated = self.probabilityInfection(
                self.isSymptomatic)

        elif other_agent.isTransmitter and not self.isContaminated:
            self.isContaminated = self.probabilityInfection(
                other_agent.isSymptomatic)
            self.isSymptomatic = self.random.choice([True, False])

    def printStatus(self, other_agent):
        contamination_level = "contaminated" if self.isContaminated else "not contaminated"
        # print("Hi, I am agent " + str(self.unique_id) +
        #       " and I'm " + contamination_level)

        print(f"{str(self.unique_id)} => {other_agent.unique_id}")

    def step(self):
        other_agent = self.random.choice(self.model.schedule.agents)

        self.verifyContact(other_agent)
        self.updateStatus()
        self.printStatus(other_agent)
