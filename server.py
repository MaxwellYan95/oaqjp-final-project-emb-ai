from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route('/')
def index():
    emotionDict = emotion_detector("")
    # Format the response as a string similar to the example output in the lab
    response_str = (
        "For the given statement, the system response is "
        f"'anger': {emotionDict['anger']}, "
        f"'disgust': {emotionDict['disgust']}, "
        f"'fear': {emotionDict['fear']}, "
        f"'joy': {emotionDict['joy']}, "
        f"'sadness': {emotionDict['sadness']}. "
        f"The dominant emotion is <b>{emotionDict['dominant_emotion']}</b>."
    )
    if emotionDict['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return response_str

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)