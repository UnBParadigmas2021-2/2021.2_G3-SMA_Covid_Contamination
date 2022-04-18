width = 20
height = 20
general_tx_death = -1
general_tx_transmission = -1


# Atualiza o valor das taxas de mortalidade e transmissão.
# Essa função é chamada em person_model.py, no momento da
# criação da Model

def update_tx(new_tx_death, new_tx_transmission):
    global general_tx_death
    global general_tx_transmission
    general_tx_death  = new_tx_death
    general_tx_transmission = new_tx_transmission
    print(f"{general_tx_transmission}: GENERAL")


# Retorna uma tupla com as configurações: taxa de mortalidade e taxa de transmissão.
# Essa função é chamada em person_agent.py, em dois momentos diferentes. Primeiro,
# para se calcular a probabilidade de transmissão. Segundo, para verificar se o agente
# morreu 

def get_tx():
    global general_tx_death
    global general_tx_transmission
    return general_tx_transmission, general_tx_death