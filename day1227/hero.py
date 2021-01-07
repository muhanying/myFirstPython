from day1227 import log

def log_decorator(func):
    def wrapper(*args, **kwargs):
        log.debug(f'{func.__name__}')
        return func(*args, **kwargs)
    return wrapper

class Hero:
    hp = 100
    power = 10
    magic_hp = 200
    speed = 1

    @log_decorator
    def fight(self, hero: 'Hero'):
        while True:
            hero.hp -= self.power
            if self.winner(self, hero):
                return False
            if self.winner(hero, self):
                return True

    @log_decorator
    def winner(self, hero1, hero2):
        logging.info(f'{hero1} vs {hero2}')
        if hero1.hp <= 0:
            return False
        if hero2.hp <= 0:
            return True

    def fight_many(self, heros: list['Hero']):
        pass
