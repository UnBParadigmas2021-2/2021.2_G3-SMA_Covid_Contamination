from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from person_model import PersonModel

def agentPortrayal(agent):
    portrayal = {"Shape": "circle","Label": f"agente {str(agent.unique_id)}","Filled": "true","r": 0.75}
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


canvasElement = CanvasGrid(agentPortrayal, 20,20, 500, 500)

server =  ModularServer(
    PersonModel, [canvasElement], "Covid Contamination", {"N":100}
)

server.port = 8521