from flask import Flask, jsonify
from EmotionDetection.emotion_detection import emotion_detector
import json
app = Flask(__name__)

@app.route('/')
def index():
    emotionDict = emotion_detector("I think I am having fun")
    result1 = "For the given statement, the system response is "
    result2 = json.dumps(emotionDict)
    return result1 + "" + result2[1:len(result2)-1]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)