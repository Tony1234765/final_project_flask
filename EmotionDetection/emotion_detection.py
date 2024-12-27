import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } } 

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json = myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 400, extract the emotions
    if response.status_code == 200:
        anger = formatted_response['emotionPredictions'][0]["emotion"]["anger"]
        disgust = formatted_response['emotionPredictions'][0]["emotion"]["disgust"]
        fear = formatted_response['emotionPredictions'][0]["emotion"]["fear"]
        joy = formatted_response['emotionPredictions'][0]["emotion"]["joy"]
        sadness = formatted_response['emotionPredictions'][0]["emotion"]["sadness"]

        #Creating a dictionary with the emotions
        emotions = {"anger":anger, "disgust":disgust, "fear":fear,"joy":joy, "sadness": sadness}

        #Find the highest key
        max_key = max(emotions, key=emotions.get)

        #Append the dominant emotion
        emotions["dominant_emotion"] = max_key
        
    # If the response status code is 400, set emotions to none
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        max_key = None
        #Creating a dictionary with the emotions
        emotions = {"anger":anger, "disgust":disgust, "fear":fear,"joy":joy, "sadness": sadness, "dominant_emotion": max_key}

    return emotions