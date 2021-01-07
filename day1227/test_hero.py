from unittest import TestCase

from day1227.chenyaojing import ChenYaoJing
from day1227.libai import Libai


class TestHero(TestCase):
    def test_fight(self):
        chenYaoJing = ChenYaoJing()
        liba = Libai()
        assert chenYaoJing.fight(liba) == True
        assert liba.fight(chenYaoJing) == False
