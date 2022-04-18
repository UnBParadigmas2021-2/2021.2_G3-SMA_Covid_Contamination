from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from person_model import PersonModel
from utils import height, width

def agentPortrayal(agent):
    portrayal = {"Shape": "circle","text": f"{str(agent.unique_id)}", "text_color": "black","Filled": "true","r": 0.75}

    if agent.isContaminated:
        portrayal["Color"] = "red"
        portrayal["Estado"] = "Contaminado"
        portrayal["Dias Contaminados"] = agent.daysContaminated
        portrayal["Layer"] = 0
    else:    
        portrayal["Color"] = "yellow"
        portrayal["Estado"] = "Saudável"
        portrayal["Dias Contaminados"] = 0
        portrayal["Layer"] = 0

    if agent.daysContaminated >= 7:
        portrayal["Color"] = "green"
        portrayal["Estado"] = "Recuperado"
        portrayal["Layer"] = 0

    if not agent.isAlive:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 0

    return portrayal


canvas_element = CanvasGrid(agentPortrayal, width, height, 500, 500)

params = {
    "persons": UserSettableParameter(
        'slider', "Quantidade de pessoas", 200, 100,400,10
    ),
    "initial_infected": UserSettableParameter("slider", "Quantidade de pessoas infectadas no dia 0", 1, 1, 50,1),
    "tx_death": UserSettableParameter("slider", "Taxa de mortalidade", 0.1, 0, 0.3, 0.1),
    "tx_transmission": UserSettableParameter("slider", "Taxa de transmissão", 0.2, 0.1, 5, 0.01),
}

server =  ModularServer(
    PersonModel, [canvas_element], "Covid Contamination", params
)


server.port = 8521

