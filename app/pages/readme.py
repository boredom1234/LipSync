import streamlit as st

st.set_page_config(page_icon="🚀", layout='wide')

# Setup the sidebar
with st.sidebar: 
    st.image('https://art.pixilart.com/sr21acacf391faws3.gif')
    st.title('LIPSYNC')
    st.info('This application is originally developed from the LipNet deep learning model.')

def main():
    st.title("LipSync")

    st.write("The LipSync is a machine learning-powered application that synchronizes lip movements with predicted text in real-time video streams. This project utilizes Streamlit, computer vision, and deep learning techniques to analyze lip movements and predict corresponding text.")

    st.markdown("## Installation")

    st.write("""
    1. Clone the repository:
       ```bash
       git clone https://github.com/boredom1234/lipsync.git
       ```

    2. Install dependencies:
       ```bash
       pip install -r requirements.txt
       ```
    """)

    st.markdown("## Usage")

    st.write("""
    1. Run the ```ipynb``` file to generate the model.
    2. If you don't have a GPU to support the hardware capabilities then you can use the pre-trained model. You can download it from the cell in the notebook. 
   [```96 epochs model has the best accuracy.```]
    1. Run the Streamlit app:
       ```bash
       streamlit run _main.py
       ```

    2. Follow the instructions in the app to:
       - Select the input sourcefrom the dataset.
       - Begin lip movement analysis and view predicted text.
    """)

    st.markdown("## Streamlit App Structure")

    st.code("""
    lipsync/
    │
    ├── app.py             # Main Streamlit application
    ├── requirements.txt   # Python dependencies
    ├── utils.py           # Utility functions for data processing
    ├── modelutil.py       # Functions to load and use the ML model
    ├── st_pages.py        # Streamlit page definitions
    ├── models/            # Directory for trained ML models
    │   └── checkpoint     # Trained ML model file
    ├── static/            # Directory for static files (e.g., images)
    │   └── lipsync_logo.png # Project logo image
    └── README.md          # Project documentation
    """)

    st.markdown("## Streamlit App Pages")

    st.write("""
    The Streamlit app consists of multiple pages for user interaction. These pages include:

    - **Home Page**: Displays project overview and usage instructions.
    - **Analysis Page**: Initiates lip movement analysis and displays predicted text synchronized with lip movements.
    """)

    st.markdown("## Contributing")

    st.write("Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request.")

    st.markdown("## License")

    st.write("This project is licensed under the MIT License.")

if __name__ == "__main__":
    main()
