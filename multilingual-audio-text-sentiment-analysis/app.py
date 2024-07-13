from flask import Flask, render_template, request, redirect, url_for
from langdetect import detect, DetectorFactory
from googletrans import Translator, LANGUAGES
import speech_recognition as sr
import os
from textblob import TextBlob

app = Flask(__name__)

# Set seed for consistent language detection
DetectorFactory.seed = 0

# Directory to save uploaded files
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize the Google Translator
translator = Translator()

def detect_language_text(text):
    """Detect the language of the input text and return the language code and name."""
    try:
        lang_code = detect(text)
        lang_name = LANGUAGES.get(lang_code, "Unknown Language")
        return lang_code, lang_name
    except Exception as e:
        print(f"Error detecting language: {e}")
        return "unknown", "Could not detect language"

def detect_language_audio(file_path):
    """Detect the language of the audio file and return the language code, name, and transcribed text."""
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, show_all=False)  # Get transcribed text
            lang_code = detect(text)
            lang_name = LANGUAGES.get(lang_code, "Unknown Language")
            return lang_code, lang_name, text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        return "unknown", "Could not detect language", None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "unknown", "Could not detect language", None
    except Exception as e:
        print(f"Error recognizing audio: {e}")
        return "unknown", "Could not detect language", None

def analyze_sentiment(text):
    """Analyze sentiment of the text and return a sentiment description with emojis."""
    try:
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return "Positive 😊"
        elif analysis.sentiment.polarity < 0:
            return "Negative 😠"
        else:
            return "Neutral 😐"
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return "Error in sentiment analysis"

@app.route('/', methods=['GET', 'POST'])
def index():
    """Render the home page with options for text or audio input."""
    if request.method == 'POST':
        choice = request.form['choice']
        if choice == 'text':
            return redirect(url_for('text_input'))
        elif choice == 'audio':
            return redirect(url_for('audio_input'))
    return render_template('index.html')

@app.route('/text', methods=['GET', 'POST'])
def text_input():
    """Handle text input for language detection and sentiment analysis."""
    result = None
    sentiment = None
    if request.method == 'POST':
        text = request.form['text']
        lang_code, lang_name = detect_language_text(text)
        result = f"Language Code: {lang_code}, Language: {lang_name}"
        sentiment = analyze_sentiment(text)
    return render_template('text_input.html', result=result, sentiment=sentiment)

@app.route('/audio', methods=['GET', 'POST'])
def audio_input():
    """Handle audio file upload for language detection, transcription, and sentiment analysis."""
    audio_result = None
    transcribed_text = None
    sentiment = None
    if request.method == 'POST':
        audio_file = request.files['audio']
        if audio_file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
            audio_file.save(file_path)

            # Detect language and transcribe text
            lang_code, lang_name, transcribed_text = detect_language_audio(file_path)
            audio_result = f"Language Code: {lang_code}, Language: {lang_name}"

            # Detect sentiment
            if transcribed_text:
                sentiment = analyze_sentiment(transcribed_text)

    return render_template('audio_input.html', audio_result=audio_result, transcribed_text=transcribed_text, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
