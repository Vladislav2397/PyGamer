from common.position import Position
from unittest import TestCase, main

BASE_X = 20
BASE_Y = 20
BASE_STEP = 20

NEW_X = 60
NEW_Y = 100


class PositionTest(TestCase):

	def setUp(self) -> None:
		self.pos = Position([BASE_X, BASE_Y], BASE_STEP)
		return super().setUp()

	def test_equal_list(self):
		self.assertEqual(self.pos, [BASE_X, BASE_Y])

	def test_equal_tuple(self):
		self.assertEqual(tuple(self.pos), (BASE_X, BASE_Y))

	def test_set_pos(self):
		self.pos.set_position([NEW_X, NEW_Y])
		self.assertEqual(self.pos, [NEW_X, NEW_Y])

	def test_move_obj(self):
		self.pos.move_bottom()
		self.assertEqual(
			self.pos, [BASE_X, BASE_Y + BASE_STEP]
		)
		self.pos.move_right()
		self.assertEqual(
			self.pos, [BASE_X + BASE_STEP, BASE_Y + BASE_STEP]
		)
		self.pos.move_top()
		self.assertEqual(
			self.pos, [BASE_X + BASE_STEP, BASE_Y]
		)
		self.pos.move_left()
		self.assertEqual(
			self.pos, [BASE_X, BASE_Y]
		)

	def test_get_pos(self):
		self.assertEqual(self.pos.get_bottom, (BASE_X, BASE_Y + BASE_STEP))
		self.assertEqual(self.pos.get_right, (BASE_X + BASE_STEP, BASE_Y))
		self.assertEqual(self.pos.get_top, (BASE_X, BASE_Y - BASE_STEP))
		self.assertEqual(self.pos.get_left, (BASE_X - BASE_STEP, BASE_Y))


if __name__ == "__main__":
	main()
