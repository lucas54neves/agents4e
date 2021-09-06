import random
from time import sleep

class Environment(object):
    def __init__(self):
        # state: limpo, pouco sujo, muito sujo
        self.locations = [
            {
                'direction': 'norte',
                'state': 'limpo',
                'visited': False
            },
            {
                'direction': 'sul',
                'state': 'limpo',
                'visited': False
            },
            {
                'direction': 'leste',
                'state': 'limpo',
                'visited': False
            },
            {
                'direction': 'oeste',
                'state': 'limpo',
                'visited': False
            },
            {
                'direction': 'centro',
                'state': 'limpo',
                'visited': True
            }
        ]

        for index, location in enumerate(self.locations):
            """
                Escolhe aleatoriamente o estado de cada localizacao
                    - Se for 1, sera limpo que ja foi definido anteriormente
                    - Se for 2, sera pouco sujo
                    - Se for 3, sera muito sujo
            """
            state = random.randint(1,3)

            if state == 2 and index < 4:
                location['state'] = 'pouco sujo'
            elif state == 3 and index < 4:
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
        positions = [index for index, element in enumerate(self.locations) if element['state'] != 'limpo' and not element['visited']]

        if len(positions) < 2:
            index = 0
        else:
            index = random.randint(0,len(positions) - 1)

        self.agent_location = positions[index]

        self.locations[positions[index]]['visited'] = True
    
    def run(self):
        print('O agente esta no centro.')
        print()

        while not self.all_clean():
            self.print_environment()
            print()

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

            self.print_environment()
            print()

            sleep(2)

            self.agent_location = 4
            print('O agente voltou para o centro.')
            print()
        
        self.print_environment()
        print()

        print('Tudo limpo.')
    
    def print_environment(self):
        print('[X] - Agente')
        print('[1] - Ambiente limpo')
        print('[2] - Ambiente pouco sujo')
        print('[3] - Ambiente muito sujo')

        prints = []

        for index, location in enumerate(self.locations):
            if index == self.agent_location:
                prints.append('X')
            elif location['state'] == 'limpo':
                prints.append('1')
            elif location['state'] == 'pouco sujo':
                prints.append('2')
            elif location['state'] == 'muito sujo':
                prints.append('3')
        
        print()
        print(f'\t|{prints[0]}|\t')
        print(f'|{prints[3]}|\t|{prints[4]}|\t|{prints[2]}|')
        print(f'\t|{prints[1]}|\t')

def main():
    number_of_environments = int(input('Quantas vezes deseja executar? '))

    for i in range(number_of_environments):
        print(f'Rodada {i + 1}:')
        print()

        ambiente = Environment()
        ambiente.run()

        print()
        print('Rodada finalizada')
        print()

        sleep(2)

main()