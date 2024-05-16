# AuTranscribe Transcription-App
AuTranscribe is a simple web application built with Streamlit for transcribing audio to text. It allows users to upload an audio file or record audio using their microphone.

## Usage

1. **Select audio input option:**
   - Choose between uploading an audio file or recording audio.

2. **Upload audio file:**
   - Click on the "Upload audio file" option and select an audio file in either MP3 or WAV format.

3. **Record audio:**
   - Click on the "Record audio" option and press the "Start Recording" button. Speak into your microphone and the app will transcribe your speech.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Elilora/transcription_app.git
    cd transcription_app
    ```

2. **Install the required libraries:**

    ```bash
    pip install streamlit speech_recognition
    ```

## Run the App

```bash
streamlit run transcription_app.py
