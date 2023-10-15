#import numpy


def devoir1(trajets_train, durees_train, ville_depart, durees_voldirect, sacrifice):

    # TO DO

    # Train 
    ville = "bxl"
    N = []
    Ns = [ville_depart]
    N_s = []
    graph = {}
    smallest_dist_train = {}
    smallest_dist_plane = {}
    count_train = 0
    for journey, duration in zip (trajets_train, durees_train):
        cities = tuple(journey.split("-"))
        city1, city2 = cities 
        if city1 not in smallest_dist_train :
            smallest_dist_train[city1] = float("infinity")
        if city2 not in smallest_dist_train :
            smallest_dist_train[city2] = float("infinity")
        if city1 not in N:
            N.append(city1)
        if city2 not in N:
            N.append(city2)
        # checking if city1 is already in graph
        if city1 in graph :
            graph[city1][city2] = duration
        else :
            graph[city1] = {city2: duration}
        # checking if city2 is already in graph
        if city2 in graph :
            graph[city2][city1] = duration
        else :
            graph[city2] = {city1: duration}
    #print(graph) 
    smallest_dist_train[ville_depart] = 0
    N_s = [x for x in N if x not in Ns]
    #initialazing s-d-t
    for city, cost in graph[ville_depart].items():
        smallest_dist_train[city] = cost + 30
    while N_s != []:
        for city in N_s:
            for connexion, cost in graph[city].items():
                if smallest_dist_train[connexion] > smallest_dist_train[city] + 15 + cost:
                    smallest_dist_train[connexion] = smallest_dist_train[city] + 15 + cost
        Ns.append(city)
        N_s.remove(city)
    print(smallest_dist_train)
        

    return ville, smallest_dist_train, smallest_dist_plane, count_train



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