import unittest
from devoir1 import devoir1

class Test1_Devoir1(unittest.TestCase):
    def setUp(self):
        # Input Data 1 
        self.trajets_train = ["BRU-PAR", "BRU-AMS", "BRU-LON", "BRU-COL", "PAR-BOR", "PAR-LYO", "PAR-FRA",
                              "PAR-LON", "PAR-REN", "AMS-BER", "AMS-COL", "AMS-HAM", "COL-HAM", "COL-FRA",
                              "COL-BER", "LYO-MAR", "LYO-ZUR", "FRA-HAM", "FRA-BER", "FRA-MUN", "FRA-ZUR",
                              "BER-MUN", "BER-HAM", "BER-PRA", "MUN-ZUR", "MIL-LYO", "MIL-ZUR", "LYO-BAR",
                              "BAR-MAR", "BOR-TLS", "TLS-BAR", "TLS-MAR", "LON-BIR", "LON-MAN", "MAN-BIR",
                              "MAN-EDI", "EDI-GLW", "LYO-TLS", "HAM-COP", "PAR-TLS"]
        self.durees_train = [80, 95, 120, 105, 120, 110, 230, 140, 90, 385, 180, 300, 215, 60, 280, 110,
                             240, 280, 275, 200, 235, 255, 175, 265, 210, 270, 240, 330, 285, 120, 195,
                             225, 95, 140, 80, 190, 50, 250, 280, 260]
        self.ville_depart = "BRU"
        self.durees_voldirect = [65, 120, 85, 80, 100, 60, 90, 100, 60, 105, 75, 80, 85, 85, 100, 90, 80,
                                 65, 90, 95, 100, 75]
        self.sacrifice = 60

        # Input Data 2 
        self.expected_ville = ['AMS', 'BAR', 'BER', 'BIR', 'BOR', 'COL', 'COP', 'EDI', 'FRA', 'GLW',
                               'HAM', 'LON', 'LYO', 'MAN', 'MAR', 'MIL', 'MUN', 'PAR', 'PRA', 'REN',
                               'TLS', 'ZUR']
        self.expected_min_distances_train = [125, 580, 430, 260, 245, 135, 660, 510, 210, 575, 365, 150,
                                             235, 305, 360, 520, 425, 110, 710, 215, 380, 460]
        self.expected_min_distances_avion = [245, 300, 265, 260, 280, 240, 270, 280, 240, 285, 255, 260,
                                             265, 265, 280, 270, 260, 245, 270, 275, 280, 255]
        self.expected_count_train = 10

    def test_devoir1(self):
        ville, min_distances_train, min_distances_avion, count_train = devoir1(
            self.trajets_train, self.durees_train, self.ville_depart,
            self.durees_voldirect, self.sacrifice)

        self.assertEqual(ville, self.expected_ville)
        self.assertEqual(min_distances_train, self.expected_min_distances_train)
        self.assertEqual(min_distances_avion, self.expected_min_distances_avion)
        self.assertEqual(count_train, self.expected_count_train)



class Test2_Devoir1(unittest.TestCase):
    def setUp(self):
        # Input Data 2
        self.trajets_train = ["BRU-PAR", "BRU-AMS", "BRU-LON", "BRU-COL", "PAR-BOR", "PAR-LYO", "PAR-FRA", "PAR-LON",
                             "PAR-REN", "AMS-BER", "AMS-COL", "AMS-HAM", "COL-HAM", "COL-FRA", "COL-BER", "LYO-MAR",
                             "LYO-ZUR", "FRA-HAM", "FRA-BER", "FRA-MUN", "FRA-ZUR", "BER-MUN", "BER-HAM", "BER-PRA",
                             "MUN-ZUR", "MIL-LYO", "MIL-ZUR", "LYO-BAR", "BAR-MAR", "BOR-TLS", "TLS-BAR", "TLS-MAR",
                             "LON-BIR", "LON-MAN", "MAN-BIR", "MAN-EDI", "EDI-GLW", "LYO-TLS", "HAM-COP", "PAR-TLS"]

        self.durees_train = [80, 95, 120, 105, 120, 110, 230, 140, 90, 385, 180, 300, 215, 60, 280, 110,
                             240, 280, 275, 200, 235, 255, 175, 265, 210, 270, 240, 330, 285, 120, 195, 225, 95,
                             140, 80, 190, 50, 250, 280, 260]

        self.ville_depart = "FRA"

        self.durees_voldirect = [75, 125, 70, 100, 105, 60, 30, 90, 120, 125, 65, 105, 80, 105, 95, 75, 55,
                                 75, 65, 95, 105, 55]

        self.sacrifice = 120

        # Expected Output 2
        self.expected_ville = ['AMS', 'BAR', 'BER', 'BIR', 'BOR', 'BRU', 'COL', 'COP', 'EDI', 'GLW', 'HAM', 'LON',
                               'LYO', 'MAN', 'MAR', 'MIL', 'MUN', 'PAR', 'PRA', 'REN', 'TLS', 'ZUR']

        self.expected_min_distances_train = [285, 730, 305, 455, 395, 210, 90, 605, 705, 770, 310, 345, 385, 500, 510,
                                            520, 230, 260, 585, 365, 530, 265]

        self.expected_min_distances_avion = [255, 305, 250, 280, 285, 240, 210, 270, 300, 305, 245, 285, 260, 285,
                                            275, 255, 235, 255, 245, 275, 285, 235]

        self.expected_count_train = 11

    def test_devoir1(self):
        ville, min_distances_train, min_distances_avion, count_train = devoir1(
            self.trajets_train, self.durees_train, self.ville_depart,
            self.durees_voldirect, self.sacrifice
        )

        self.assertEqual(ville, self.expected_ville)
        self.assertEqual(min_distances_train, self.expected_min_distances_train)
        self.assertEqual(min_distances_avion, self.expected_min_distances_avion)
        self.assertEqual(count_train, self.expected_count_train)



if __name__ == '__main__':
    unittest.main()



