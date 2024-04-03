import streamlit as st

st.set_page_config(page_icon="🚀", layout='wide')

# Setup the sidebar
with st.sidebar:
    st.image('https://art.pixilart.com/sr21acacf391faws3.gif')
    st.header('LIPSYNC')
    st.info(
        'This application is originally developed from the LipNet deep learning model.')

st.header("🤖 Introduction to Lip Reading Model")

st.write("""
        - Building a machine learning model for lip reading.
        - Introducing the purpose and significance of creating a lip reading model for accessibility and societal benefit.
        - Overview of the technologies to be used: OpenCV for video processing, TensorFlow for deep learning model building, and integration of components for testing.
         """)

st.header("🗣️ Client Conversation: Lip Reading Request")

st.write("""
   - Discuss the need for a lip reading model with the client.
   - Exploring the significance of lip reading in improving accessibility.
   - Agreement to proceed with the project and acknowledgment of potential future extensions.
         """)


st.header("📦 Installing Dependencies")

st.write("""
   - Installing necessary libraries such as OpenCV, Matplotlib, ImageIO, Gdown, and TensorFlow.
   - Verifying the installed versions of the libraries.
   - Providing information on accessing the code repository for future reference.
         """)


st.header("📊 Importing Dependencies and Memory Configuration")

st.write("""
   - Importing essential Python libraries, including OS, CV2, TensorFlow, NumPy, and Matplotlib.
   - Setting up memory configuration to prevent exponential memory growth, especially when using GPUs for training.
         """)

st.header("📥 Data Loading: Downloading and Preparing Dataset")

st.write("""
   - Downloading the dataset using the Gdown library from Google Drive.
   - Unzipping the downloaded data file and preparing it for loading.
   - Explanation of the dataset structure and the annotations associated with the videos.
         """)

st.header("🎥 Video Data Loading Function")

st.write("""
   - Implementing a function to load video data from the dataset path.
   - Processing each video frame, including grayscale conversion and mouth region isolation.
   - Standardizing the video frames for consistency in model training.
         """)


st.header("🔠 Vocabulary Definition")

st.write("""
   - Defining the vocabulary for the lip reading model, including characters and numbers.
   - Utilizing Keras string lookup functionality to convert characters to numbers and vice versa.
         """)

st.header("📝 Preprocessing text data for lip reading")

st.write("""
    - Functions for character-to-number conversion and vice versa.
    - Tokenization and encoding of text data.
    - Vocabulary definition for the model.
""")

st.header("🛠️ Loading and preprocessing alignments data")

st.write("""
    - Parsing alignment data from files.
    - Filtering out unnecessary data.
    - Loading alignments and videos simultaneously.
""")

st.header("📂 Building a data-loading function")

st.write("""
    - Creating a function to load video and alignment data.
    - Processing file paths for data loading.
    - Testing the data loading function with sample data.
""")

st.header("🚀 Setting up the data pipeline")

st.write("""
    - Importing necessary libraries.
    - Creating a TensorFlow data pipeline for training.
    - Preprocessing and batching data for model training.
""")

st.header("📊 Visualizing preprocessed data")

st.write("""
    - Previewing frames and alignment data.
    - Converting data to GIF format for visualization.
    - Demonstrating how the model will interpret input data.
""")

st.header("📊 Data Pipeline Preparation")

st.write("""
    - Setting up a TensorFlow dataset and testing it using the numpy iterator method.
    - Utilizing imageio.mimsave to convert numpy arrays into gifs.
    - Reviewing pre-processed images and annotations.
""")

st.header("🧠 Model Building Preparation")

st.write("""
    - Introducing the use of 3D convolutions for passing videos and a classification dense layer for predicting characters.
    - Explaining the adoption of CTC loss function for handling non-aligned word transcriptions.
    - Discussing the readiness of the model for handling non-aligned data in the future.
""")

st.header("🛠️ Neural Network Design")

st.write("""
    - Importing necessary dependencies including model classes and layers.
    - Defining the deep neural network architecture using sequential layers, convolutions, LSTMs, and dense layers.
    - Describing the purpose of each layer and its parameters in the neural network architecture.
""")

st.header("📈 Model Summary and Reference")

st.write("""
    - Summarizing the constructed deep neural network architecture.
    - Providing resources for further exploration and comparison with other models, including GitHub repositories and research papers.
""")

st.header("📉 Loss Function and Callback Definition")

st.write("""
    - Defining the learning rate scheduler and CTC loss function for model training.
    - Implementing a callback to save model checkpoints and another callback for making predictions after each epoch during training.
""")

st.header("🚀 Model Training Initiation")

st.write("""
    - Preparing for model training by setting up the fit function with data input and defining the number of epochs.
    - Specifying callbacks to be utilized during the training process, including checkpoint saving and prediction output.
""")

st.header("🧠 Training the Model and Adding Testing Data")

st.write("""
    - Training the model on an RTX 3060 super GPU.
    - Each Epoch takes around 4-5 minutes to complete depending on the hardwares used.
    - Adding testing data to the data pipeline to ensure proper evaluation.
    - Demonstrating the addition of testing data through code modifications.
""")

st.header("Evaluating Model Performance and Providing Model Checkpoints")

st.write("""
    - Examining the loss metrics for training and validation data after multiple epochs.
    - Noting improvements in model performance as epochs increase.
    - Making model checkpoints available for download and future use.
""")

st.header("📊 Making Predictions with the Trained Model")

st.write("""
    - Downloading and loading model checkpoints for prediction.
    - Making predictions on new data samples using the loaded model.
    - Evaluating the model's predictions against actual text annotations.
""")

st.header("📹 Testing the Model with External Videos")

st.write("""
    - Demonstrating how to use the model to transcribe speech from external videos.
    - Showing the model's accuracy in transcribing text from various video samples.
    - Discussing the potential for further development, such as building an application around the model.
""")

st.markdown("---")

############################################################################################
#######                            END OF ONE PAGE                                   ######
############################################################################################
st.title("🛠️ Setting up the project structure and environment")
st.write("""
  - Setting up the project in VS Code.
  - Explanation of the project folder structure.
  - Loading pre-trained model checkpoints and helper files.
""")

st.header("🤖 Understanding the model structure and utility functions")
st.write("""
  - Explanation of the model structure in the project.
  - Overview of utility functions included in the project.
  - Clarification on the character-based nature of the LipSync model.
""")

st.header("⚙️ Importance of integrating machine learning models into full-stack applications")
st.write("""
  - Advantages of integrating machine learning models into full-stack applications.
  - Importance of transitioning from model development to deployment.
  - Emphasis on the significance of practical application and user interaction.
""")

st.header("📚 Importing necessary libraries and modules")
st.write("""
  - Importing essential libraries such as Streamlit, TensorFlow, and imageio.
  - Explanation of the purpose of each imported library/module.
  - Mention of potential alternatives like PyTorch and reasons for sticking with TensorFlow.
""")

st.header("🖼️ Structuring the Streamlit app and adding basic components")
st.write("""
  - Setting the layout configuration to wide.
  - Adding a sidebar with an image and information.
  - Initializing columns for structuring the app layout.
""")

st.header("📊 Setting up layout and columns for app display")
st.write("""
  - Checking for selected options before proceeding.
  - Creating two columns for organizing app content.
  - Adding placeholder text to each column for initial setup.
""")

st.header("🎥 Setting up video display helper function")
st.write("""
  - Using `streamlit.video_display` to render video inside the application.
  - Obtaining the full file path for the selected video using `os.path.join`.
  - Utilizing `ffmpeg` to convert the selected video file from MPG to MP4 format.
""")

st.header("📹 Rendering the video inside the application")
st.write("""
  - Opening and reading the video file as binary to render it.
  - Displaying the video using `St.video`.
  - Adding a header and information box to the application interface.
""")

st.header("🔄 Pre-processing the video data")
st.write("""
  - Loading the video data using the `load_data` function.
  - Converting the video into a GIF using `imageio.mimsave`.
  - Rendering the GIF inside the application with `St.image`.
""")

st.header("🧠 Making predictions with the loaded model")
st.write("""
  - Loading the trained deep learning model using the `load_model` function.
  - Generating predictions using the model's `predict` method.
  - Utilizing the CTC decoder to process predictions and condense duplicate outputs.
""")

st.header("📝 Decoding the raw output of the machine learning model")
st.write("""
  - Decoding raw output of the machine learning model,
  - Taking the raw output tokens and converting them into words using the `num_to_char` function.
  - Concatenating the words into a single sentence using `tf.strings.reduce_join`.
  - Decoding the raw tokens into words and displaying the result.
""")

st.header("📽️ Testing the model's predictions with various videos")
st.write("""
  - Testing model predictions with various videos,
  - Demonstrating the model's accuracy in predicting spoken words from videos.
  - Showing examples of the model's predictions with different videos, including handling different accents.
  - Highlighting the model's ability to generate accurate predictions based solely on raw video input.
""")

st.header("🏁 Completing the application and overview of the development process")
st.write("""
  - Completing the application and overview of development process,
  - Summarizing the steps involved in building the application, from setting up Streamlit to processing video inputs.
  - Reviewing challenges encountered during development, such as handling file formats and layout setup.
  - Encouraging viewers to access the code on GitHub and share their experiences with the application, while hinting at future tutorial topics.
""")
