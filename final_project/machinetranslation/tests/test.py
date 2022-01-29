import unittest
from translator import english_to_french, french_to_english


class TestEnglishtofrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Five"), "Trois")
        self.assertIsNotNone(english_to_french("Two"), "Deux")
        self.assertIsNone(english_to_french(None))

class TestFrenchtoEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("bonne"), "bad")
        self.assertIsNotNone(english_to_french("Sept"), "Seven")
        self.assertIsNone(french_to_english(None))

if __name__ == '__main__':
    unittest.main()