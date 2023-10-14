#import numpy


def devoir1(trajets_train, durees_train, ville_depart, durees_voldirect, sacrifice):

    # TO DO

    # Train 
    N = []
    Ns = []
    N_s = []
    directory = {}
    for journey, duration in zip (trajets_train, durees_train):
        cities = tuple(journey.split("-"))
        city1, city2 = cities 
        # checking if city1 is already in directory
        if city1 in directory :
            directory[city1][city2] = duration
        else :
            directory[city1] = {city2: duration}
        # checking if city2 is already in directory
        if city2 in directory :
            directory[city2][city1] = duration
        else :
            directory[city2] = {city1: duration}
    print(directory)       


        

    #return ville, min_distances_train, min_distances_avion, count_train



trajets_train = ["BRU-PAR", "BRU-AMS", "BRU-LON", "BRU-COL", "PAR-BOR", "PAR-LYO", "PAR-FRA", "PAR-LON", "PAR-REN",
                 "AMS-BER", "AMS-COL", "AMS-HAM", "COL-HAM", "COL-FRA", "COL-BER", "LYO-MAR", "LYO-ZUR", "FRA-HAM",
                 "FRA-BER", "FRA-MUN", "FRA-ZUR", "BER-MUN", "BER-HAM", "BER-PRA", "MUN-ZUR", "MIL-LYO", "MIL-ZUR",
                 "LYO-BAR", "BAR-MAR", "BOR-TLS", "TLS-BAR", "TLS-MAR", "LON-BIR", "LON-MAN", "MAN-BIR", "MAN-EDI",
                 "EDI-GLW", "LYO-TLS", "HAM-COP", "PAR-TLS"]

durees_train = [80, 95, 120, 105, 120, 110, 230, 140, 90, 385, 180, 300, 215, 60, 280, 110,
240, 280, 275, 200, 235, 255, 175, 265, 210, 270, 240, 330, 285, 120, 195, 225, 95, 140, 80, 190,
50, 250, 280, 260]

ville_depart = "BRU"

durees_voldirect = [65, 120, 85, 80, 100, 60, 90, 100, 60, 105, 75, 80, 85, 85, 100, 90, 80,
65, 90, 95, 100, 75]

sacrifice = 60

devoir1(trajets_train, durees_train, ville_depart, durees_voldirect, sacrifice)