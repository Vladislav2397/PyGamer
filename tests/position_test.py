from common.position import Position
from unittest import TestCase, main

BASE_X = 20
BASE_Y = 20
BASE_STEP = 20


class PositionTest(TestCase):

	def setUp(self) -> None:
		self.pos = Position([BASE_X, BASE_Y], BASE_STEP)
		return super().setUp()

	def test_equal_list(self):
		self.assertEqual(self.pos, [BASE_X, BASE_Y])


if __name__ == "__main__":
	main()
