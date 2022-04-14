class PersonModel(Model):
    def __init__(self, N):
        self.number_of_agents = N

        for i in range(self.number_of_agents):
            agent = PersonAgent(i, self)