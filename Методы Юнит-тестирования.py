import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    
    is_frozen = True
    
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.participant_1 = Runner('Усэйн', 10)
        self.participant_2 = Runner('Андрей', 9)
        self.participant_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            print(cls.all_results[key])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn1(self):
        turn_1 = Tournament(90, self.participant_1,
                            self.participant_3)
        results = turn_1.start()
        self.all_results[1] = {1: results[1].name, 2: results[2].name}
        last_time = max(results.keys())
        self.assertTrue(results[last_time] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn2(self):
        turn_2 = Tournament(90, self.participant_2,
                            self.participant_3)
        results = turn_2.start()
        self.all_results[2] = {1: results[1].name, 2: results[2].name}
        last_time = max(results.keys())
        self.assertTrue(results[last_time] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn3(self):
        turn_3 = Tournament(90, self.participant_1,
                            self.participant_2, self.participant_3)
        results = turn_3.start()
        self.all_results[3] = {1: results[1].name, 2: results[2].name, 3: results[3].name}
        last_time = max(results.keys())
        self.assertTrue(results[last_time] == "Ник")

if __name__ == '__main__':
    unittest.main()
