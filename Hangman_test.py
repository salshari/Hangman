import unittest
from HangmanComputing import HangmanGame

class TestHangmanGameClass(unittest.TestCase):
    '''
    class representing the test cses for the functions in thr HangmanGame class
    '''

    # test if the display_word_to_guess fucntion works properly
    def display_word_to_guess_function_test(self):
        game = HangmanGame("apple")
        game.guessed_letters = {'a', 'p'}
        self.assertEqual(game.display_word_to_guess(), "a p p _ _ ")

    # test if the guess_letter function works properly
    def guess_letter_function_test(self):
        game = HangmanGame("banana")
        game.guess_letter('b')
        self.assertIn('b', game.guessed_letters)

    # test if the check_win function works properly
    def check_win_function_test(self):
        game = HangmanGame("zebra")
        game.guessed_letters = {'z', 'e', 'b', 'r', 'a'}
        self.assertTrue(game.check_win())


if __name__ == '__main__':
    unittest.main()