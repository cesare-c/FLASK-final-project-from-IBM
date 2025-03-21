''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app:
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''This code recives the text from the HTML interface and
        runs emotion detections over it using emotion_detector()
        functions.
        The output shows all emotion and its dominant emotion
    '''
    # Retrive the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract all emotions from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # When dominant emotion is None
    if dominant_emotion is None:
        return "Invalid input! Try again"
    # Return a f string with all the emotion
    return (
        f"For the given statement, the system response is:"
        f"'anger': {anger}," 
        f"'disgust': {disgust}," 
        f"'fear': {fear},"
        f"'joy': {joy} and 'sadnes': {sadness}."
        f"The dominant emotion is {dominant_emotion}."
        )
@app.route("/")
def render_index_page():
    '''This function initiates the rendering of the main application
       page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
