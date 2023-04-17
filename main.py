import streamlit as st
from PIL import Image

# Define function to display the image
def display_image(image_path):
	image = Image.open(image_path)
	left_co, cent_co,last_co = st.columns(3)
	with cent_co:
		st.image(image, caption="", width=300)
    # st.markdown(f'<div style="text-align: center;"><img src="{image_path}" style="max-width: 200px;"></div>', unsafe_allow_html=True)

# Define function to display the app descriptions
def display_app_descriptions():
    st.write("#### Step 1: FastEDA")
    st.write("FastEDA is a tool for quickly exploring and visualizing your data. It offers a variety of features such as automatic data profiling, correlation analysis, and data visualization.")
    st.write("#### Step 2: Calibrate")
    st.write("Calibrate is a tool for calibrating machine learning models. It offers a variety of calibration methods, such as temperature scaling and Platt scaling, to improve the accuracy of your models.")
    st.write("#### Step 3: Predict")
    st.write("Predict is a tool for making predictions with your machine learning models. It offers a variety of features such as batch prediction and model explainability.")

# Main function
def main():
    # Set page title and favicon
    st.set_page_config(page_title="AIrmate", page_icon=":guardsman:")

    # Display the image
    display_image("./head.png")

    # Display the app descriptions
    display_app_descriptions()

if __name__ == "__main__":
    main()
