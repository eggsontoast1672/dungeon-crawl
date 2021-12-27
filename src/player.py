from element import Element
from entity import Entity


class Player(Entity):
    max_health: int = 20
    max_stamina: int = 3
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

    def __init__(self):
        self.health = self.max_health

    def attack(self, target: Entity, attack_type: Element) -> None:
        if self.stamina[attack_type] <= 0:
            print(f"Your {attack_type} attack is out of stamina.")
            return

        match attack_type:
            case Element.FIRE:
                print("You use a fire attack. It does 15 damage.")
                target.decrease_health(15)
            case Element.ICE:
                print("You use an ice attack. \
It does 5 damage and freezes the dark lord.")
                target.decrease_health(5)
                target.freeze()
            case Element.EARTH:
                print("You use an earth attack. \
It does 5 damage and you heal 5 health.")
                target.decrease_health(5)


        # FIXME: Repeat check for other attack types

        self.decrease_stamina(attack_type, 1)

    def increase_health(self, amount: int) -> None:
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def decrease_health(self, value: int) -> None:
        self.health -= value

    def increase_stamina(self, stamina_type: Element, amount: int) -> None:
        self.stamina[stamina_type] += amount
        if self.stamina[stamina_type] > self.max_stamina:
            self.stamina[stamina_type] = self.max_stamina

    def decrease_stamina(self, stamina_type: Element, amount: int) -> None:
        self.stamina[stamina_type] -= amount
        if self.stamina[stamina_type] < 0:
            self.stamina[stamina_type] = 0

    def freeze(self) -> None:
        self.frozen = True

    def unfreeze(self) -> None:
        self.frozen = False

