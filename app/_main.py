# Import all of the dependencies
import streamlit as st
import os
import imageio
from moviepy.editor import VideoFileClip

import tensorflow as tf
from utils import load_data, num_to_char
from modelutil import load_model
from st_pages import Page, show_pages, add_page_title, Section
st.set_page_config(page_icon="🚀", layout='wide')


show_pages(
    [
        Page("_main.py", "Home", "🏠"),
        Page("pages\\streamlitapp.py", "Lip Sync", "👄"),
        Page("pages\\sign.py", "Sign Language", "🤟🏻"),
        Page("pages\\readme.py", "Readme", "📖"),
        Page("pages\\about.py", "About", "❔"),
        # Page("pages\\about2.py", "About 2", "❔"),
        # Page("pages\\about3.py", "About 3", "❔"),
    ]
)
# Setup the sidebar
with st.sidebar:
    st.title('LIPSYNC')
    st.image('https://art.pixilart.com/sr21acacf391faws3.gif')
    st.info(
        'STILL WIP, PLEASE IGNORE THE ERRORS AND INCONSISTENCIES. THANK YOU! 🙂')


def main():
    # st.markdown("---")

    st.error("*NOTE THIS MODEL WORKS ONLY WITH THE TRAINED DATASET FOR NOW, LATER VERSIONS WILL BE ABLE TO WORK WITH ANY VIDEO FILES AND REAL-TIME FOOTAGE AS WELL... 🙂*")
    st.title("👄 LipSync Overview")
    st.markdown("---")

    st.header("Overview:")
    st.write("The LipSync is a machine learning-powered application that synchronizes lip movements with predicted text in video streams.")

    st.header("Features:")
    st.write("""
    🎯 Real-time Lip Movement Analysis\n
    📝 Text Prediction\n
    🎯 Sync Accuracy\n
    🖥️ User-Friendly Interface\n
    🔒 Privacy and Security\n
    ☁️ Cloud-based Processing\n
    """)

    st.header("Usage:")
    st.write("""
    1. **Start Application:** Launch the app on your device.
    2. **Begin Analysis:** Start lip movement analysis from the dataset.
    3. **View Predicted Tokens:** See tokens synchronized with lip movements.
    3. **View Predicted Text:** See text synchronized with lip movements.
    4. **End Session:** Terminate the session.
    """)

    st.header("System Requirements:")
    st.write("""
    - Operating System: Windows, macOS, Linux
    - Hardware: Device with camera
    - Software Dependencies: Computer vision, ML, video processing libraries
    """)

    st.header("Future Enhancements:")
    st.write("""
    🌟 Improved Accuracy\n
    🌍 Multilingual Support\n
    🎙️ Integration with Speech Recognition\n
    📝 Feedback Mechanism
    """)

    st.header("Conclusion:")
    st.write("The LipSync Text Predictor app revolutionizes video content interaction by synchronizing lip movements with predicted text. It enhances accessibility and inclusivity in communication.")

if __name__ == "__main__":
    main()
