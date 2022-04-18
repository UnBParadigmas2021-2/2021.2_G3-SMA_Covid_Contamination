from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from person_model import PersonModel
from utils import height, width, persons

def agentPortrayal(agent):
    portrayal = {"Shape": "circle","text": f"{str(agent.unique_id)}", "text_color": "black","Filled": "true","r": 0.75}
    if agent.isContaminated:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    else:    
        portrayal["Color"] = "yellow"
        portrayal["Layer"] = 0

    if agent.daysContaminated >= 7:
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0
        # portrayal["r"] = 0.2

    return portrayal


canvasElement = CanvasGrid(agentPortrayal, width, height, 500, 500)

server =  ModularServer(
    PersonModel, [canvasElement], "Covid Contamination", {"N":persons}
)

server.port = 8521
server.launch()