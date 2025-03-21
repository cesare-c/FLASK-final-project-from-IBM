import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj  = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)
    status_code = response.status_code
    
    if status_code == 400:
        emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            }
    else:
        
        res = json.loads(response.text)
        emotions = res['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion        

    return emotions


    
