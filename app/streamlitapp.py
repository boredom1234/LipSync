# # Import all of the dependencies
# import streamlit as st
# import os 
# import imageio 
# from moviepy.editor import VideoFileClip

# import tensorflow as tf 
# from utils import load_data, num_to_char
# from modelutil import load_model
# from st_pages import Page, show_pages, add_page_title


# # show_pages(
# #     [
# #         Page("pages\\home.py", "HOME", "🏠"),
# #         Page("streamlitapp.py", "APP", "📱"),
# #         Page("pages\\about.py", "ABOUT", "❔"),
# #     ]
# # )

# # Set the layout to the streamlit app as wide 
# # st.set_page_config(layout='wide')

# # Setup the sidebar
# # with st.sidebar: 
# #     st.image('https://cdn.dribbble.com/users/2009763/screenshots/4222740/media/290a0653a38454114dd4ca04c60b7891.gif')
# #     st.title('LIPSYNC')
# #     st.info('This application is originally developed from the LipNet deep learning model.')

# st.title('LIPSYNC') 
# # Generating a list of options or videos 
# options = os.listdir(os.path.join('..', 'data', 's1'))
# selected_video = st.selectbox('Choose a video from the dataset', options)

# # Generate two columns 
# col1, col2 = st.columns(2)

# if options: 
#     # Rendering the video 
#     with col1: 
#         st.info('The video below displays the converted video in MP4 format')
#         file_path = os.path.join('..', 'data', 's1', selected_video)

#         # Convert the video from MPEG to MP4 format using moviepy
#         output_path = 'video.mp4'
#         video = VideoFileClip(file_path)
#         video.write_videofile(output_path, codec='libx264', audio_codec='aac')
#         video.close()

#         # Display the video with audio using st.video
#         st.video(output_path, format='video/mp4', start_time=0)


#     with col2: 
#         st.error('This is all the machine learning model sees when making a prediction')
#         video, annotations = load_data(tf.convert_to_tensor(file_path))
#         imageio.mimsave('animation.gif', video, fps=10)
#         st.image('animation.gif', width=400) 

#         st.success('This is the output of the machine learning model as tokens')
#         model = load_model()
#         yhat = model.predict(tf.expand_dims(video, axis=0))
#         decoder = tf.keras.backend.ctc_decode(yhat, [75], greedy=True)[0][0].numpy()
#         st.text(decoder)

#         # Convert prediction to text
#         st.warning('Decode the raw tokens into words')
#         converted_prediction = tf.strings.reduce_join(num_to_char(decoder)).numpy().decode('utf-8')
#         st.text(converted_prediction)
        
