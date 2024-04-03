# import streamlit as st

# st.set_page_config(page_icon="🚀", layout='wide')

# # Setup the sidebar
# with st.sidebar:
#     st.image('https://art.pixilart.com/sr21acacf391faws3.gif')
#     st.header('LIPSYNC')
#     st.info(
#         'This application is originally developed from the LipNet deep learning model.')
  

# st.title("🛠️ Setting up the project structure and environment")
# st.write("""
#   - Setting up the project in VS Code.
#   - Explanation of the project folder structure.
#   - Loading pre-trained model checkpoints and helper files.
# """)

# st.header("🤖 Understanding the model structure and utility functions")
# st.write("""
#   - Explanation of the model structure in the project.
#   - Overview of utility functions included in the project.
#   - Clarification on the character-based nature of the LipSync model.
# """)

# st.header("⚙️ Importance of integrating machine learning models into full-stack applications")
# st.write("""
#   - Advantages of integrating machine learning models into full-stack applications.
#   - Importance of transitioning from model development to deployment.
#   - Emphasis on the significance of practical application and user interaction.
# """)

# st.header("📚 Importing necessary libraries and modules")
# st.write("""
#   - Importing essential libraries such as Streamlit, TensorFlow, and imageio.
#   - Explanation of the purpose of each imported library/module.
#   - Mention of potential alternatives like PyTorch and reasons for sticking with TensorFlow.
# """)

# st.header("🖼️ Structuring the Streamlit app and adding basic components")
# st.write("""
#   - Setting the layout configuration to wide.
#   - Adding a sidebar with an image and information.
#   - Initializing columns for structuring the app layout.
# """)

# st.header("📊 Setting up layout and columns for app display")
# st.write("""
#   - Checking for selected options before proceeding.
#   - Creating two columns for organizing app content.
#   - Adding placeholder text to each column for initial setup.
# """)

# st.header("🎥 Setting up video display helper function")
# st.write("""
#   - Using `streamlit.video_display` to render video inside the application.
#   - Obtaining the full file path for the selected video using `os.path.join`.
#   - Utilizing `ffmpeg` to convert the selected video file from MPG to MP4 format.
# """)

# st.header("📹 Rendering the video inside the application")
# st.write("""
#   - Opening and reading the video file as binary to render it.
#   - Displaying the video using `St.video`.
#   - Adding a header and information box to the application interface.
# """)

# st.header("🔄 Pre-processing the video data")
# st.write("""
#   - Loading the video data using the `load_data` function.
#   - Converting the video into a GIF using `imageio.mimsave`.
#   - Rendering the GIF inside the application with `St.image`.
# """)

# st.header("🧠 Making predictions with the loaded model")
# st.write("""
#   - Loading the trained deep learning model using the `load_model` function.
#   - Generating predictions using the model's `predict` method.
#   - Utilizing the CTC decoder to process predictions and condense duplicate outputs.
# """)

# st.header("📝 Decoding the raw output of the machine learning model")
# st.write("""
#   - Decoding raw output of the machine learning model,
#   - Taking the raw output tokens and converting them into words using the `num_to_char` function.
#   - Concatenating the words into a single sentence using `tf.strings.reduce_join`.
#   - Decoding the raw tokens into words and displaying the result.
# """)

# st.header("📽️ Testing the model's predictions with various videos")
# st.write("""
#   - Testing model predictions with various videos,
#   - Demonstrating the model's accuracy in predicting spoken words from videos.
#   - Showing examples of the model's predictions with different videos, including handling different accents.
#   - Highlighting the model's ability to generate accurate predictions based solely on raw video input.
# """)

# st.header("🏁 Completing the application and overview of the development process")
# st.write("""
#   - Completing the application and overview of development process,
#   - Summarizing the steps involved in building the application, from setting up Streamlit to processing video inputs.
#   - Reviewing challenges encountered during development, such as handling file formats and layout setup.
#   - Encouraging viewers to access the code on GitHub and share their experiences with the application, while hinting at future tutorial topics.
# """)
