from person_model import PersonModel
from canvas import server

if __name__ == "__main__":
    personModel = PersonModel(50)

    server.launch()