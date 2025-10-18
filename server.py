from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route('/')
def index():
    emotionDict = emotion_detector("I think I am having fun")
    if request.status_code == 400:
        emotionDict = emptyDict();
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
    return response_str

def emptyDict():
    return {'anger': None, 'disgust': None, 'fear': None, 'sadness': None, 'dominant_emotion': None}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)