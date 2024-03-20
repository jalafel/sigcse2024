import unittest
from unittest.mock import patch
import ass1_sol
import io
import sys

class TestGame(unittest.TestCase):
  @patch('builtins.input', side_effect=['John', 'left', 'yes', 'right', 'no'])
  def test_game_loop(self, mock_input):
      # Redirect stdout to a buffer
      capturedOutput = io.StringIO()
      sys.stdout = capturedOutput

      # Call the function that contains the game loop
      ass1_sol.main()

      # Reset stdout
      sys.stdout = sys.__stdout__

      # Check the output
      expected_output = 'John, you have chosen the left path.\nYou encounter a dragon!\nJohn, you have chosen the right path.\nYou find a treasure chest!\nThanks for playing!\n'

      print(capturedOutput.getvalue())

      self.assertEqual(capturedOutput.getvalue(), expected_output)

if __name__ == '__main__':
  unittest.main()