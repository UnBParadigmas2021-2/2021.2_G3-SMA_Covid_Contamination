from mesa import Agent
from utils import width, height, get_tx

# Agente Pessoa
# Cada pessoa tem caracteristicas como ser ou não transmissor
# estar ou não infectado e ser ou não um infectado sintomático,
# além de um contador de dias contaminados
# Um agente pessoa se move pelo grid e pode se contaminar caso esteja em contato
# com outro agente infectado
class PersonAgent(Agent):
    recoveryDay = 7

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.isContaminated = False
        self.isSymptomatic = False
        self.daysContaminated = 0
        self.isTransmitter = False
        self.isAlive = True
    
    # Simula se houve o contágio do agente por meio de probabilidade
    # Se o agente for assintomático, a probabilidade irá se basear em
    # um dado estatístico. Se for sintomático, vai se basear na taxa de transmissão
    # definida pelo usuário 
    def probabilityInfection(self, symptomatic):
        tx_transmission, _ =   get_tx()
        if not symptomatic:
            return self.random.choices([True, False], [0.58, 0.42])[0]
        return self.random.choices([True, False], [tx_transmission, 1-tx_transmission])[0]

    # Cria uma lista de posições válidas vizinhas ao agente para que ele possa se locomover
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

    # Move o agente (apenas agentes vivos) dentro do grid    
    def move(self):
        if self.isAlive:
            neighborhood = self.our_neighborhood()
            move_to = self.random.choice(neighborhood)
            self.model.grid.move_agent(self, move_to)
    
    # Atualiza o status do agente podendo ser
    # Recuperado: Após 7 dias do contágio
    # Contaminado: Após entrar em contato com algum agente com caracteristica transmissora, atualiza os dias de contágio
    # Não contaminado: Representa pessoa sem o vírus no corpo
    # Transmissora: Representa a pessoa que foi contaminada a 3 dias
    def updateStatus(self):
        if self.daysContaminated == self.recoveryDay:
            self.isContaminated = False
            self.isTransmitter = False                

        if self.isContaminated:
            self.daysContaminated += 1
            # Define a partir da taxa de mortalidade se um sintomático irá falecer
            if self.isSymptomatic:
                _, tx_death = get_tx()
                self.isAlive = self.random.choices([True, False], [ 1 - tx_death, tx_death ])[0]
        else:
            self.daysContaminated = 0

        if self.daysContaminated == 3:
            self.isTransmitter = True                

    # Verifica o contato entre 2 agentes
    # No caso de 1 dos agentes ser um transmissor em potencial é calculada a propabilidade de contágio
    # além de definir se o contaminado é sintomatico ou assimtomatico
    def verifyContact(self):
        contact = self.model.grid.get_cell_list_contents([self.pos])

        for agent in contact:
            if self.isTransmitter and not agent.isContaminated and agent.isAlive:
                agent.isContaminated = self.probabilityInfection(
                    self.isSymptomatic)
                    
            elif agent.isTransmitter and not self.isContaminated and agent.isAlive:
                self.isContaminated = self.probabilityInfection(
                    agent.isSymptomatic)
                if self.isContaminated:
                    self.isSymptomatic = self.random.choices([True, False],[0.7, 0.3])[0]


    def step(self):

        # Determina que as ações são realizadas apenas por agentes vivos 
        if self.isAlive:
            self.move()
            self.verifyContact()
            self.updateStatus()
