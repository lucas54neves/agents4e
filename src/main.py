import random
from time import sleep

class Environment(object):
    def __init__(self):
        # state: limpo, pouco sujo, muito sujo
        self.locations = [
            {
                'direction': 'norte',
                'state': 'limpo'
            },
            {
                'direction': 'sul',
                'state': 'limpo'
            },
            {
                'direction': 'leste',
                'state': 'limpo'
            },
            {
                'direction': 'oeste',
                'state': 'limpo'
            }
        ]

        for location in self.locations:
            """
                Escolhe aleatoriamente o estado de cada localizacao
                    - Se for 1, sera limpo que ja foi definido anteriormente
                    - Se for 2, sera pouco sujo
                    - Se for 3, sera muito sujo
            """
            state = random.randint(1,3)

            if state == 2:
                location['state'] = 'pouco sujo'
            elif state == 3:
                location['state'] = 'muito sujo'
        
        """
            O agente pode estar em 5 localizacoes
                0 norte
                1 sul
                2 leste
                3 oeste
                4 centro
        """
        self.agent_location = 4
    
    def all_clean(self):
        for location in self.locations:
            if location['state'] != 'limpo':
                return False
        
        return True
    
    def next_location(self):
        self.agent_location = random.randint(0,3)
    
    def run(self):
        print('O agente esta no centro.')
        print()

        while not self.all_clean():
            sleep(2)
            self.next_location()
            print(f"O agente se moveu para o {self.locations[self.agent_location]['direction']}.")
            if self.locations[self.agent_location]['state'] == 'limpo':
                print(f"O ambiente {self.locations[self.agent_location]['direction']} esta limpo.")
            elif self.locations[self.agent_location]['state'] == 'pouco sujo':
                print(f"O ambiente {self.locations[self.agent_location]['direction']} esta pouco sujo, aspirando...")
                self.locations[self.agent_location]['state'] = 'limpo'
            elif self.locations[self.agent_location]['state'] == 'muito sujo':
                print(f"O ambiente {self.locations[self.agent_location]['direction']} esta muito sujo, lavando...")
                self.locations[self.agent_location]['state'] = 'limpo'
            sleep(2)
            self.agent_location = 4
            print('O agente voltou para o centro.')
            print()

        print('Tudo limpo.')

ambiente = Environment()
ambiente.run()