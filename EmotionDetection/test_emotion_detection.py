import unittest

from emotion_detection import emotion_detector
class TestEmotionDetection(unittest.TestCase):
    def test1(self):
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"], "joy")