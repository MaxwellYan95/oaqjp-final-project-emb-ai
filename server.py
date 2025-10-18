"""
All import statements
"""
from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

"""
Displays the response on the application
"""
@app.route('/')
def index():
    """emotion_dict a dictionary that represents a request"""
    emotion_dict = emotion_detector("")
    # Format the response as a string similar to the example output in the lab
    response_str = (
        "For the given statement, the system response is "
        f"'anger': {emotion_dict['anger']}, "
        f"'disgust': {emotion_dict['disgust']}, "
        f"'fear': {emotion_dict['fear']}, "
        f"'joy': {emotion_dict['joy']}, "
        f"'sadness': {emotion_dict['sadness']}. "
        f"The dominant emotion is <b>{emotion_dict['dominant_emotion']}</b>."
    )
    if emotion_dict['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return response_str

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
