from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from person_model import PersonModel
from utils import height, width

#  Agentes representados no grid como circulos em determinadas cores, onde cada cor representa um estado do agente
def agentPortrayal(agent):
    portrayal = {"Shape": "circle","text": f"{str(agent.unique_id)}", "text_color": "black","Filled": "true","r": 0.75}

    # Agente contaminado = Vermelho
    if agent.isContaminated:
        portrayal["Color"] = "red"
        portrayal["Estado"] = "Contaminado"
        portrayal["Dias Contaminados"] = agent.daysContaminated
        portrayal["Layer"] = 0
    # Agente sáudavel = Vermelho
    else:    
        portrayal["Color"] = "yellow"
        portrayal["Estado"] = "Saudável"
        portrayal["Layer"] = 0

    # Agente recuperado de contaminação = Verde
    if agent.daysContaminated >= 7:
        portrayal["Color"] = "green"
        portrayal["Estado"] = "Recuperado"
        portrayal["Layer"] = 0

    # Agente morto = Cinza
    if not agent.isAlive:
        portrayal["Color"] = "grey"
        portrayal["Estado"] = "Falecido"
        portrayal["Layer"] = 0


    return portrayal


canvas_element = CanvasGrid(agentPortrayal, width, height, 500, 500)

# Parametros mutáveis (em slider) de entrada para simulação
# Número de pessoas (agentes)
# Número de pessoas inicialmente infectadas
# Taxa de mortalidade do vírus
# Taxa de transmissão
params = {
    "persons": UserSettableParameter(
        'slider', "Quantidade de pessoas", 200, 100,400,10
    ),
    "initial_infected": UserSettableParameter("slider", "Quantidade de pessoas infectadas no dia 0", 1, 1, 50,1),
    "tx_death": UserSettableParameter("slider", "Taxa de mortalidade", 0.1, 0, 0.3, 0.1),
    "tx_transmission": UserSettableParameter("slider", "Taxa de transmissão", 0.2, 0.1, 5, 0.01),
}

# Cria o server segundo os parâmetros
server =  ModularServer(
    PersonModel, [canvas_element], "Covid Contamination", params
)

# Porta do server
server.port = 8521

