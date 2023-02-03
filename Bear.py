import random

class Animal:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.satiety = 50
        self.energy = 80
        self.fat = 50
        self.alive = True
        self.food = 15

    def to_hunts(self):
        print('Search food ')
        self.energy -= 26
        self.gladness -= 10
        self.satiety -= 10
        self.fat -= 16
        self.food += 15

    def to_eat(self):
        print('I am eating')
        self.satiety += 12
        self.gladness += 15
        self.energy += 7
        self.fat += 30
        self.food -= 15

    def to_sleep(self):
        print('I will sleep')
        self.satiety -= 3
        self.gladness += 5
        self.energy += 10
        self.fat -= 3

    def to_chill(self):
        print('I will chill')
        self.energy += 8
        self.satiety -= 0.50
        self.gladness += 3
        self.fat -= 4



    def is_alive(self):
        if self.gladness <= 0:
            print('I am sad')
            self.alive = True
            self.energy -= 5
        #если счастье < или = 0 и он жив
        elif self.fat <= 5 and self.food >= 5:
            print('My fat is appears')
            while self.fat > 0:
                self.food -= 5
            while self.fat > 0:
                self.fat += 10
            self.alive = True
        #если жир < или = 5 и еда > или = 0 то запускается цикл где отнимается по 5 еды и добавляется 10 жира пока жира не станет больше чем 0 и он жив
        elif self.energy <= 5 and self.food >= 5:
            print('I am tired')
            while self.energy <= 0:
                self.food -= 5
            while self.energy <= 0:
                self.energy += 5
            self.alive = True
        #если энергия < или = 0 и еда > или = 5 то запускается цикл где отнимается по 5 еды и добавляется по 5 энергии пока энергия < или = 0 и он жив
        elif self.energy <= 0 and self.food <= 0 and self.fat <= 0:
            self.alive = False
        #
        elif self.energy <= 5 and self.fat >= 5:
            print('My fat is dissapear')
            while self.energy <= 0:
                self.fat -= 5
            while self.energy <= 0:
                self.energy += 2,5
            self.alive = True
        #
        elif self.fat >= 5 and self.satiety <= 5:
            print('My fat dissapear')
            while self.satiety <= -2:
                self.fat -= 5
            while self.satiety <= -2:
                self.satiety += 2,5
            self.alive = True
        #
        elif self.fat <= 0 and self.food < 0 and self.satiety <= 0:
            print('I havent got any fat and food')
            self.alive = False
        #
        elif self.fat <= 5 and self.food <= 5 and self.satiety > 10:
            print('I havent got any fat and food')
            self.alive = True
        #если жир < или = -5 и еда < 0 и сытность > 10 то он жив
        elif self.food <= 5 and self.satiety > 5 or self.fat > 5:
            print('I must find some food')
            self.alive = True
        #если еда < 0 и сытность > 5 или жира > 5 и он жив
    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Satiety = {self.satiety}')
        print(f'Energy = {self.energy}')
        print(f'Fat = {self.fat}')
        print(f'Food = {self.food}')

    def live(self, day):
        day = " Day " + str(day) + " of " + self.name + "Life"
        print(f'{day:=^50}')
        Live_cube = random.randint(1,4)
        if Live_cube == 1:
            self.to_hunts()
        elif Live_cube == 2:
            self.to_sleep()
        elif Live_cube == 3:
            self.to_chill()
        elif Live_cube == 4:
            self.to_eat()
        self.end_of_day()
        self.is_alive()

Bear = Animal(name = "Bear's Jack " )
for day in range(365):
    if Bear.alive == False:
       break
    Bear.live(day)





