from flask import Flask, jsonify
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route('/')
def index():
    emotionDict = emotion_detector("I think I am having fun")
    return jsonify(emotionDict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)