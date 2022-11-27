import unittest
import dev.update_ball


class MyTestCase(unittest.TestCase):
    """
    Test the direction and current state of the ball
        update_ball_info(ball_x_y: tuple, ball_direction: tuple, SCREEN_WIDTH: int, SCREEN_HEIGHT: int)
        ball_direction = (x_direction, y_direction)
    """
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    def test_ball_reaching_the_window_bottom(self):
        ball_x_y = (310, 600)
        ball_direction = (1, 1)
        results = dev.update_ball.update_ball_info(ball_x_y, ball_direction, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        expected_results = ((311, 600), (1, -1))

        self.assertEqual(results, expected_results)  # add assertion here

    def test_ball_exceeding_the_window_bottom(self):
        ball_x_y = (310, 601)
        ball_direction = (1, 1)
        results = dev.update_ball.update_ball_info(ball_x_y, ball_direction, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        expected_results = ((311, 600), (1, -1))

        self.assertEqual(results, expected_results)  # add assertion here

    def test_ball_reaching_the_window_top(self):
        ball_x_y = (310, 0)
        ball_direction = (1, -1)
        results = dev.update_ball.update_ball_info(ball_x_y, ball_direction, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        expected_results = ((311, 0), (1, 1))

        self.assertEqual(results, expected_results)  # add assertion here

    def test_ball_exceeding_the_window_top(self):
        ball_x_y = (310, -1)
        ball_direction = (1, -1)
        results = dev.update_ball.update_ball_info(ball_x_y, ball_direction, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        expected_results = ((311, 0), (1, 1))

        self.assertEqual(results, expected_results)  # add assertion here

if __name__ == '__main__':
    unittest.main()
