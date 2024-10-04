class Person:
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def calculate_damage(self, attack_damage):
        effective_damage = attack_damage - (attack_damage * (self.armor / 100))
        return max(0, effective_damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0


class Player(Person):
    def attack(self, enemy):
        damage_done = self.calculate_damage(self.damage)
        enemy.take_damage(damage_done)
        print("Player наносит ", damage_done, "урона!( ", enemy.health, "HP осталось)")


class Enemy(Person):
    def attack(self, player):
        damage_done = self.calculate_damage(self.damage)
        player.take_damage(damage_done)
        print(
            "Enemy наносит ",
            damage_done,
            " урона! (",
            player.health,
            " HP осталось)",
        )


class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        turn = 0
        while self.player.is_alive() and self.enemy.is_alive():
            if turn == 0:
                self.player.attack(self.enemy)
                turn = 1
            else:
                self.enemy.attack(self.player)
                turn = 0

        if self.player.is_alive():
            print("Игрок победил!")
        else:
            print("Враг победил!")


hero = Player(100, 50, 40)
villain = Enemy(80, 30, 20)

game = Game(hero, villain)
game.start_battle()
