import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=input_json)
    emotion_dict = response.json()['emotionPredictions'][0]['emotion']
    great = great_emotion(emotion_dict)
    emotion_dict["dominant_emotion"] = great
    return emotion_dict

def great_emotion(emotions: dict):
    string = ""
    num = 0
    for key in emotions.keys():
        if num < emotions[key]:
            num = emotions[key]
            string = key
    return string