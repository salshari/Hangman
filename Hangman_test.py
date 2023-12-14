import unittest
from HangmanComputing import HangmanGame
from HangmanComputing import FruitWordBank
from HangmanComputing import HolidayWordBank
from HangmanComputing import AnimalWordBank

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

    # test if the check_lose function works properly
    def check_lose_function_test(self):
        game = HangmanGame("difficult")
        for letter in "abcde":
            game.guess_letter(letter)
        self.assertTrue(game.check_lose())
        
    # test if the check_win function works properly
    def check_win_function_test(self):
        game = HangmanGame("zebra")
        game.guessed_letters = {'z', 'e', 'b', 'r', 'a'}
        self.assertTrue(game.check_win())

    # test if the is_game_over function works properly
    def is_game_over_function_test(self):
        game = HangmanGame("several")
        for letter in "qwertyuiopasdfghjklzxcvbnm":
            game.guess_letter(letter)
        self.assertTrue(game.is_game_over())

        game = HangmanGame("test")
        for letter in "test":
            game.guess_letter(letter)
        self.assertTrue(game.is_game_over())

class TestWordBanks(unittest.TestCase):
    '''
    class representing the test cases for the subclasses of the Parent class WordBank
    there are three subclasses: one for fruits, one for holidays, and one for animals
    '''
    # the following tests ensure that the word randomly chosen is in the appropriate word bank
    
    # test if the FruitWordBank class works properly 
    def fruit_word_bank_class_test(self):
        fruit_word_bank = FruitWordBank()
        randomly_selected_word = fruit_word_bank.get_word_to_guess()
        # check if the word that was randomly selected is in the FruitWorDBank
        self.assertIn(randomly_selected_word, fruit_word_bank.words)

        # test if the HolidayWordBank class works properly 
    def holiday_word_bank_class_test(self):
        holiday_word_bank = HolidayWordBank()
        randomly_selected_word = holiday_word_bank.get_word_to_guess()
        # check if the word that was randomly selected is in the HolidayWordBank
        self.assertIn(randomly_selected_word, holiday_word_bank.words)

        # test if the AnimalWordBank class works properly 
    def animal_word_bank_class_test(self):
        animal_word_bank = AnimalWordBank()
        randomly_selected_word = animal_word_bank.get_word_to_guess()
        # check if the word that was randomly selected is in the AnimalWOrdBank
        self.assertIn(randomly_selected_word, animal_word_bank.words)


if __name__ == '__main__':
    unittest.main()