import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import streamlit as st
import matplotlib.pyplot as plt
import time

st.set_page_config(layout='wide')

# Setup the sidebar
with st.sidebar: 
    st.image('https://media1.tenor.com/m/m-2XXQuq-OwAAAAd/peace-out.gif')
    st.title('Hand Speaks')
    st.info('This application is originally developed from the LipNet deep learning model.')

# Load saved model
model_path = 'C:\\Users\\banik\\OneDrive\\Documents\\CHRIST UNIVERSITY\\Third_Tri_Semester\\Advanced_Python_Programming\\Sign-Language-Recognition\\new_model_20ep3.h5'
model = tf.keras.models.load_model(model_path)
model.summary()

# Define labels
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Nothing']

# Function to make prediction
def predict(image):
    image = cv2.resize(image, (50, 50))
    image = image / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)[0]
    char_index = np.argmax(prediction)
    confidence = round(prediction[char_index] * 100, 1)
    predicted_char = labels[char_index]
    return predicted_char, confidence

# Main Streamlit app
st.title("Sign Language Recognition")

# Create history box
st.subheader("Prediction History")
prediction_history = st.empty()

# Create live line graph
st.status("```Live Confidence Graph```")
# progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
chart = st.line_chart(np.random.randn(1, 1))

cap = cv2.VideoCapture(0)

stframe = st.empty()

history_list = []

data = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    roi = frame[100:500, 100:500]  # Adjust the coordinates to increase ROI size
    
    predicted_char, confidence = predict(roi)
    cv2.rectangle(frame, (100, 100), (500, 500), (0, 0, 255), 5)  # Adjust the rectangle size accordingly
    cv2.putText(frame, f"{predicted_char}, Conf: {confidence}%", (80, 80), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 255), 2)

    stframe.image(frame, channels="BGR")

    # Update prediction history
    history_list.append(f"{predicted_char}, Conf: {confidence}%")
    if len(history_list) > 10:  # Limit the history to the last 10 predictions
        history_list.pop(0)
    history_text = "\n".join(history_list)
    prediction_history.text(history_text)

    # Update live line chart
    data.append([confidence])
    if len(data) > 100:  # Limit the data points to 100 frames
        data.pop(0)
    chart.line_chart(data)
    # progress_bar.progress(min(len(data), 100))  # Cap progress bar value at 100%
    status_text.text("%i Frames Processed" % len(data))
    time.sleep(0.05)

cap.release()
cv2.destroyAllWindows()

# Clear progress bar and status text
# progress_bar.empty()
status_text.empty()
