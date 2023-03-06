import streamlit as st
import speech_recognition as sr

# App Title
st.title("AuTranscribe")

# Create a radio button to let users choose whether to upload a file or record a file
file_option = st.sidebar.radio("Select audio input option:", ('Upload audio file', 'Record audio'))

# Create a text area to display the transcribed text
transcribed_text = st.empty()

# Define a function to get the audio
def transcribe(file_option):

      # Create a new recognizer instance
      recognizer = sr.Recognizer()

      # Initialize audio variable to None
      audio = None

      # If the user chooses to upload a file
      if file_option == 'Upload audio file':
        
        # Upload the audio file
        audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

        if audio_file is not None:
          #get audio data
          audio_data = sr.AudioFile(audio_file)

          # Use the uploaded file as the audio source
          with audio_data as source:

            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source)
            
            #get audio
            audio = recognizer.record(source)


      # If the user chooses to record a file 
      elif file_option == 'Record audio': 
        
        # Create a button to start recording
        st.text("Press button to record")
        is_recording = st.button("Start Recording")
        if is_recording:
          # Use the default microphone as the audio source
          with sr.Microphone() as source:

              # Adjust for ambient noise
              recognizer.adjust_for_ambient_noise(source)

              # Prompt the user to record
              st.write("Speak now...")

              # get audio
              audio = recognizer.listen(source)
      text=None
      if audio is not None:
          # Transcribe the speech to text
          try:
              text = recognizer.recognize_google(audio)
          except sr.UnknownValueError:
              text = "Could not understand audio"
          except sr.RequestError as e:
              text = "Error: {}".format(e)

      # Return the transcribed text
      return text

# display results
transcribed_text.text(transcribe(file_option))