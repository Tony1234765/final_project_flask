'''
Executing this function initiates the application of emotion
detection to be executed over the Flask channel and deployed on
localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
# Initiate the Flask app
app = Flask("Emotion Detection")
@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions and the 
        highest one.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the emotions and the highest key
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response['dominant_emotion']
    # Check if the response is None, indicating an error or invalid input
    if anger is None:
        return "Invalid input! Try again."
    # Return a formatted string with the emotions
    return (
        f"For the given statement, the system response is anger: {anger}, "
        f"disgust: {disgust}, fear: {fear}, joy: {joy} and sadness: {sadness}. "
        f"The dominant emotion is {dominant_emotion}"
    )
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")
if __name__ == "__main__":
    # This function executes the Flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
    