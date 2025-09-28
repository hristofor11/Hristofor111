from random import randint
import requests
import random
from datetime import datetime, timedelta

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        # self.attack = self.get_attack()
        self.power = random.randint(10, 100)
        self.hp = random.randint(1, 100)
        Pokemon.pokemons[pokemon_trainer] = self
       
        power = random.randint(1, 100)


    def attack(self, enemy):
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
           

    # Метод для получения картинки покемона через API
    def get_img(self):
            url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return (data['sprites']['other']['official-artwork']['front_default'])

        
        # Метод для получения имени покемона через API
    def get_name(self):
            url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return (data['forms'][0]['name'])
            else:
                return "Pikachu"


            # Метод класса для получения информации
    def info(self):
                hp = random.randint(10, 100)
                return f"Имя: {self.name}"
                return f"Здоровье: {self.hp}"
               

            # Метод класса для получения картинки покемона
    def show_img(self):
                return self.img


class Wizard(Pokemon):
    pass 
class Fighter(Pokemon):
      def attack(self, enemy):
            super_power = random.randint(5, 15)
            self.power += super_power 
            result = super().attack(enemy)
            self.power -= super_power
            return result + f"\nБоец применил супер атаку силой: {super.power}"


# Кормление покемона
def feed(self, feed_interval = 20, hp_increase = 10 ):
    current_time = datetime.current()  
    delta_time = timedelete(hours=feed_interval)  
    if (current_time - self.last_feed_time) > delta_time:
        self.hp += hp_increase
        self.last_feed_time = current_time
        return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
    else:
        return f"Следующее время кормления покемона: {current_time-delta_time}"