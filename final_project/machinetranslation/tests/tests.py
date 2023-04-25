import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')          
        self.assertNotEqual(english_to_french('Hello'), 'Hello') 
        # self.assertNotEqual(english_to_french(''), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')          
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour') 
        # self.assertNotEqual(french_to_english(''), 'Hello')

unittest.main()