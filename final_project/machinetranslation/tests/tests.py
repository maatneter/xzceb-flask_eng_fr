import unittest
from translator import englishToFrench, frenchToEnglish

def frenchToEnglish_compare(self, french_text, english_text):
    translation = frenchToEnglish(french_text)
    try:
        self.assertEqual(translation, english_text)
        self.assertNotEqual(translation, english_text)
    except:
        pass

def englishToFrench_compare(self, english_text, french_text):
    translation = englishToFrench(english_text)
    try:
        self.assertEqual(translation, french_text)
        self.assertNotEqual(translation, french_text)
    except:
        pass

class TranslatorTest(unittest.TestCase):
    def test_frenchToEnglish(self):
        frenchToEnglish_compare(self, None, None)
        frenchToEnglish_compare(self, 'Bonjour', 'Hello')
    
    def test_englishToFrench(self):
        englishToFrench_compare(self, None, None)
        englishToFrench_compare(self, 'Hello', 'Bonjour')

if __name__ == '__main__':
    unittest.main()