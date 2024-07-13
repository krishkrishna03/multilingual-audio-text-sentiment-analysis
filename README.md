
# Multilingual Audio and Text Sentiment Analysis

## 📜 Overview

**Multilingual Audio and Text Sentiment Analysis** is a web application built with Flask that allows users to detect the language of text or audio files and analyze the sentiment of the text. The app supports various languages and provides sentiment analysis with a visual representation of the results.

**Features:**

- **Text Input:** Detect the language of the text and perform sentiment analysis.
- **Audio Input:** Upload audio files to detect the spoken language, transcribe the audio to text, and analyze the sentiment of the transcribed text.
- **Interactive User Interface:** Enhanced with 3D animations and modern CSS design.

## 🚀 Features

- **Language Detection**: Automatically detects the language of the input text or transcribed audio.
- **Sentiment Analysis**: Analyzes sentiment as Positive, Negative, or Neutral with emojis.
- **Audio Support**: Accepts various audio formats and performs speech-to-text conversion.
- **Responsive Design**: Mobile-friendly design with 3D animations and effects.

## 🔧 Installation

To get started with this project, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/krishkrishna03/multilingual-audio-text-sentiment-analysis.git
cd multilingual-audio-text-sentiment-analysis
```

### 2. Install the Dependencies

Make sure you have Python installed on your system. You can then install the required packages using the following command:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Start the Flask application using:

```bash
python app.py
```

Open your browser and navigate to `http://127.0.0.1:5000/` to access the application.

## 🛠️ Dependencies

This project requires the following Python packages:

- Flask
- langdetect
- googletrans==4.0.0-rc1
- SpeechRecognition
- textblob
- PyAudio (For audio file processing)

You can install these packages using the `requirements.txt` file provided:

```plaintext
Flask
langdetect
googletrans==4.0.0-rc1
SpeechRecognition
textblob
PyAudio
```

## 🧩 Usage

### Home Page

- Choose between **Text Input** or **Audio Input**.

### Text Input

- Enter text to detect its language and analyze its sentiment.

### Audio Input

- Upload an audio file to detect the language, transcribe the audio, and analyze the sentiment of the transcribed text.

## 🌟 Contributing

Feel free to open issues, submit pull requests, or suggest improvements. Contributions are welcome!

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👥 Author

- **Your Name** - [Your GitHub](https://github.com/krishkrishna03)


