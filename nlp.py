import os
import tempfile
from spleeter.separator import Separator
from pydub import AudioSegment
from transformers import pipeline
import streamlit as st

# Load Spleeter and Whisper model with caching for faster subsequent processing
@st.cache_resource
def load_separator():
    return Separator('spleeter:2stems')

@st.cache_resource
def load_transcriber():
    return pipeline("automatic-speech-recognition", model="openai/whisper-small")

def process_audio(uploaded_file):
    separator = load_separator()
    transcriber = load_transcriber()
    
    # Display the original uploaded audio file
    st.audio(uploaded_file, format="audio/mp3", start_time=0)
    
    # Create a temporary file for the uploaded audio
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav:
        audio = AudioSegment.from_file(uploaded_file)
        audio.export(temp_wav.name, format="wav")
        wav_path = temp_wav.name

    # Create an output directory for separated files
    output_directory = tempfile.mkdtemp()
    
    # Progress indicator for separation process
    st.write("🎶 **Step 1**: Separating audio into stems...")
    with st.spinner("Processing audio..."):
        separator.separate_to_file(wav_path, output_directory)
    st.success("Audio separated successfully! 🎤 Now processing the vocals...")

    # Path to the separated vocals file
    vocals_path = os.path.join(output_directory, os.path.basename(wav_path).replace(".wav", ""), "vocals.wav")

    # Check if the vocals file exists and is not silent
    if os.path.exists(vocals_path):
        vocal_audio = AudioSegment.from_wav(vocals_path)
        
        # Play the separated vocal track
        st.write("🎧 **Listen to the separated vocals**:")
        st.audio(vocals_path, format="audio/wav", start_time=0)

        if vocal_audio.dBFS > -60:  # Check if the vocal audio is above the silence threshold
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_chunk:
                temp_chunk_path = temp_chunk.name
                vocal_audio.export(temp_chunk_path, format="wav")

            try:
                # Display progress for transcription
                st.write("📝 **Step 2**: Transcribing lyrics...")
                transcription = transcriber(temp_chunk_path, return_timestamps=True)

                # Display the transcription
                st.subheader("🎶 Generated Lyrics:")
                st.markdown(f"```{transcription['text']}```")
                st.success("Lyrics transcription completed!")
            except Exception as e:
                st.error(f"⚠️ Error transcribing audio: {e}. Please ensure the audio quality is good.")
            finally:
                # Remove the temporary chunk file after processing
                os.remove(temp_chunk_path)
        else:
            st.warning("🔇 The vocal track is silent or too quiet to transcribe.")
    else:
        st.error("⚠️ Unable to find the separated vocals. Please try with a different file.")

    # Cleanup: Remove the temporary audio file and display success message
    os.remove(wav_path)
    st.success("✅ All files cleaned up. Thank you for using the Song Lyrics Generator!")

if __name__ == '__main__':
    st.set_page_config(
        page_title="Song Lyrics Generator",
        page_icon="🎵",
        layout="centered",
        initial_sidebar_state="expanded",
    )

    # Display a header image and title
    st.image("https://png.pngtree.com/thumb_back/fh260/background/20230612/pngtree-pair-of-headphones-on-the-water-at-nighttime-image_2931863.jpg", use_column_width=True)
    st.title("🎤 Song Lyrics Generator")
    st.markdown(
        """
        Generate lyrics from your favorite songs! Upload an audio file, and we’ll handle the rest:
        - 🎶 Separate the vocals from the background music
        - 📝 Transcribe the lyrics using advanced AI models
        """
    )

    # Allow user to upload a file
    uploaded_file = st.file_uploader("🎧 Choose a song file...", type=["mp3"])

    # If a file is uploaded, process it
    if uploaded_file is not None:
        process_audio(uploaded_file)
    else:
        st.info("Upload a song file to get started!")
