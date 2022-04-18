width = 20
height = 20
general_tx_death = -1
general_tx_transmission = -1


def update_tx(new_tx_death, new_tx_transmission):
    global general_tx_death
    global general_tx_transmission
    general_tx_death  = new_tx_death
    general_tx_transmission = new_tx_transmission
    print(f"{general_tx_transmission}: GENERAL")

def get_tx():
    global general_tx_death
    global general_tx_transmission
    return general_tx_transmission, general_tx_death