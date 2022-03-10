
import unittest
import sys
sys.path.append('/home/project/xzceb-flask_eng_fr/final_project/machinetranslation/')    
from translator import englishtofrench, frenchtoenglish


class TestEnFr(unittest.TestCase):
    def testEnglish(self):
        self.assertEqual(englishtofrench("Hello"),"Bonjour")

    def testEnglish2(self):
        self.assertNotEqual(englishtofrench(""),"Bonjour")


class TestFrEn(unittest.TestCase):
    def testFrench(self):
        self.assertEqual(frenchtoenglish("Bonjour"),"Hello")
    def testEnglish2(self):
        self.assertNotEqual(frenchtoenglish(""),"Hello")

unittest.main()
