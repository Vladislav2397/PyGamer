from common.tools import MyColor
from pySnake.eat import Eat
from unittest import TestCase, main

BASE_X = 20
BASE_Y = 20


class EatTest(TestCase):

	def setUp(self) -> None:
		self.eat = Eat([BASE_X, BASE_Y], MyColor.RED)
		return super().setUp()
	
	def test_equal_list(self):
		self.assertEqual(self.eat.get_pos, [BASE_X, BASE_Y])

if __name__ == "__main__":
	main()
