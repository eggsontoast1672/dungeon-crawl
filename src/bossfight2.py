# Bossfight redone

# TODO Add burning effect to fire attack

from abc import ABC, abstractmethod
from enum import Enum
from random import randint
from __future__ import annotations

health_boss = 100
health_player = 20

stamina_fire = 5
stamina_ice = 5
stamina_earth = 5

count_serum = 3
count_super_serum = 2
count_stamina_fruit = 1


class Element(Enum):
    FIRE = 0
    ICE = 1
    EARTH = 2

    def __str__(self) -> str:
        fmt: str
        if self.value == self.FIRE:
            fmt = "fire"
        elif self.value == self.ICE:
            fmt = "ice"
        else:
            fmt = "earth"
        return fmt


class Entity(ABC): 
    health: int

    @abstractmethod
    def attack(self, target: Entity, type: Element) -> None:
        pass

    @abstractmethod
    def decrease_health(self, value: int) -> None:
        pass


class Player:
    health: int = 20
    stamina: dict[Element, int] = {
        Element.FIRE: 5,
        Element.ICE: 5,
        Element.EARTH: 5
    }
    inventory: dict[str, int] = {
        "serum": 3,
        "super_serum": 2,
        "stamina_fruit": 1
    }

    def attack(self, target: Entity, attack_type: Element) -> None:
        if attack_type == Element.FIRE:
            if self.stamina[attack_type] > 0:
                print("You use a fire attack. It does 15 damage.")
                target.decrease_health(15)

        # FIXME: Repeat check for other attack types

        self.decrease_stamina(attack_type)

    def decrease_health(self, value: int) -> None:
        self.health -= value
    
    def decrease_stamina(self, stamina_type: Element) -> None:
        stamina = self.stamina[stamina_type]
        if stamina > 0:
            self.stamina[stamina_type] -= 1
        else:
            print(f"Your {stamina_type} attack is out of stamina.")


class Boss:
    pass


def boss_attack() -> None:
    global health_player
    hit_chance = randint(0, 2)    
    if hit_chance == 0:
        print("The dark lord attacks, but misses. You take no damage.")
    else:
        print("The dark lord attacks. It does 10 damage.")
        health_player -= 10
    print("You have", health_player, "health remaining.")


def check_health() -> None:
    if health_player <= 0:
        print("\nYou have died.")
    if health_boss <= 0:
        print("\nCongratulations! You defeated the boss!")
    input("Press any button to quit.")
    quit()


def use_serum() -> None:
    global count_serum 
    if count_serum > 0:
        count_serum -= 1
    else:
        print("You are out of serum.")
    boss_attack()
    check_health()


def use_super_serum() -> None:
    global count_super_serum 
    if count_super_serum > 0:
        count_super_serum -= 1 
    else:
        print("You are out of super serum.")
    boss_attack()
    check_health()


def use_stam_fruit() -> None:
    global count_stamina_fruit 
    if count_stamina_fruit > 0:
        count_stamina_fruit -= 1  
    else:
        print("You are out of stamina fruit.")
    boss_attack()
    check_health()


def fire_attack() -> None:
    global stamina_fire
    global health_boss 
    if stamina_fire > 0:
        health_boss -= 15
        stamina_fire -= 1
        print("You use a fire attack. It does 15 damage.") 
    else:
        print("Your fire attack is out of stamina.")
    boss_attack()
    check_health()


def ice_attack() -> None:
    global stamina_ice
    global health_boss 
    if stamina_ice > 0:
        health_boss -= 5
        stamina_ice -= 1
        print("You use an ice attack. It does 5 damage and freezes the dark lord.") 
    else:
        print("Your ice attack is out of stamina.")


def earth_attack() -> None:
    global stamina_earth
    global health_boss 
    if stamina_earth > 0:
        global health_player
        health_boss -= 5
        health_player += 5
        stamina_earth -= 1
        print("You use an earth attack. It does 5 damage and you heal 5 health.") 
    else:
        print("Your earth attack is out of stamina.")
    boss_attack()
    check_health()


print("You face off against the dark lord.")

loop = True
while loop:
    what_do = input("\nWhat would you like to do? (Attack, Item, Flee): ")
    if what_do.lower() == "attack":
        attack = input("What attack do you want to use? (Fire, Ice, Earth): ")

        if attack.lower() == "fire":
            fire_attack()
        elif attack.lower() == "ice":
            ice_attack()
        elif attack.lower() == "earth":
            earth_attack()
        else:
            print("Please input a valid attack next time. You forfeit your turn.")
            boss_attack()
            check_health()

    elif what_do.lower() == "item":
        item = input("What item do you want to use? (Serum, Super Serum, Stamina Fruit): ")
        if item.lower() == "serum":
            use_serum()
        elif item.lower() == "super serum":
            use_super_serum()
        elif item.lower() == "stamina fruit":
            use_stam_fruit()
        else:
            print("Please input a valid item next time. You forfeit your turn.")
            boss_attack()
            check_health()

    elif what_do.lower() == "flee":
        input("You surrender the battle. Press any key to quit.")
        loop = False

    else:
        print("Please input a valid action next time. You forfeit your turn")
        boss_attack()
        check_health()
