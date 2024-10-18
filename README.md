# Nlp Miniproject
Song Lyrics Generator
Overview: The Song Lyrics Generator is a Streamlit-based web application designed to process audio files, separate vocal tracks from instrumental parts, and generate a transcription of the vocals using automatic speech recognition (ASR). This application is particularly useful for extracting lyrics from songs by focusing solely on the vocal components.

Key Functionalities:
1. Audio Separation:
Uses the Spleeter library to split the audio file into two stems: vocals and accompaniment.
Processes the vocal track for further analysis.

2. Speech Recognition:
Uses the Whisper model from the transformers library to transcribe the lyrics from the separated vocals.
Outputs the text of the transcription, effectively generating the song lyrics.

3. User Interface:
Built using Streamlit, offering an easy-to-use file uploader for users to input their audio files.
Displays progress, results, and any errors during the processing in real-time.

Libraries and Platforms Used:
1. Streamlit (streamlit):
Provides an interactive web interface for the application.
Allows users to upload audio files and view the progress of audio separation and transcription.
Displays the results such as transcribed lyrics and any warnings or errors.

2. Spleeter (spleeter):
A music source separation library developed by Deezer.
Separates an audio file into different components (stems) like vocals and accompaniment.
In this project, it is used to isolate the vocal track from a song, making it easier to extract the lyrics.

3. pydub (pydub):
A Python library for audio file manipulation.
Converts audio files to .wav format for further processing.
Ensures compatibility with the spleeter and transformers models by handling audio export and conversions.

4. Transformers (transformers):
A library developed by Hugging Face, providing access to state-of-the-art models for various natural language processing tasks.
The Whisper model from OpenAI is used here for automatic speech recognition (ASR) to transcribe the lyrics from the processed vocal audio.
Allows transcription with timestamp support, providing a more detailed and accurate transcription output.

5. Tempfile (tempfile):
A Python module for creating temporary files and directories.
Used here for handling intermediate audio files during processing, ensuring a clean and organized file management process.

6. OS (os):
Python's built-in module for interacting with the file system.
Manages file paths and handles cleanup of temporary files after processing.

Platform:
1. Development Platform: The project is designed for local or cloud-based deployment using Streamlit. It can be run on a local development machine or hosted on platforms that support Python and Streamlit, such as Heroku, Streamlit Community Cloud, or any cloud service provider with Python runtime support.

2. Model Hosting: The ASR model is hosted through the transformers library, which pulls the Whisper model directly. This allows for efficient access without needing a custom model deployment setup.

Some Images:
![image](https://github.com/user-attachments/assets/7195562d-35f5-45f3-9812-ad5d6c61edf1)
![image](https://github.com/user-attachments/assets/8385359a-be42-47ae-8315-060d36d546c6)
![image](https://github.com/user-attachments/assets/0657d96f-d640-494f-beeb-3006046a0a05)
![image](https://github.com/user-attachments/assets/132c05aa-4ad2-4fed-9167-1db54eeac1f5)


