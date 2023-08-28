class Nursery:
    def __init__(self):

        self.Name = input('Enter Your Name: ' )
        self.Age= int(input('Enter your age: '))
        self.conditions = False
    def admission (self):
        print
        conditions = input('Do you accept The Conditions above: ')
        if self.Age >= 4 and conditions == 'Yes':
            print(f'Congratulations {self.Name} you have offered admission to Nursery 1')
        else:
            print(f'Sorry {self.Name} you do not fulfil the requirement for admission please try next time')
nursery1= Nursery()
print(nursery1.admission())
