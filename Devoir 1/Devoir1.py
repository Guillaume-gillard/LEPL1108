# 15/10/2023 Guillaume Gillard

def devoir1(trajets_train, durees_train, ville_depart, durees_voldirect, sacrifice):
   #---- Train ----#
    N = []
    Ns = [ville_depart]
    N_s = []
    graph = {}
    smallest_dist_train = {}
    for journey, duration in zip (trajets_train, durees_train):
        city1, city2 = tuple(journey.split("-"))
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
    smallest_dist_train[ville_depart] = 0
    N_s = [x for x in N if x not in Ns]
    #initialazing smallest_dist_train
    for city, cost in graph[ville_depart].items():
        smallest_dist_train[city] = cost + 30
    while N_s != []:
        for city in N_s:
            for connexion, cost in graph[city].items():
                if smallest_dist_train[connexion] > smallest_dist_train[city] + 15 + cost:
                    smallest_dist_train[connexion] = smallest_dist_train[city] + 15 + cost
        Ns.append(city)
        N_s.remove(city)
    del smallest_dist_train[ville_depart]
    smallest_dist_train = {key: smallest_dist_train[key] for key in sorted(smallest_dist_train)}
    ville = list(smallest_dist_train.keys())
    min_distances_train = list(smallest_dist_train.values())
    min_distances_avion = [x + 180 for x in durees_voldirect]
    #---- checking plane vs train ----#
    count_train = 0
    for x, y in zip(min_distances_train, min_distances_avion):
        if x <= y + sacrifice:
            count_train += 1      
    return ville, min_distances_train, min_distances_avion, count_train
