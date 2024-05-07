import streamlit as st
from PIL import Image
import io

def main():
    st.title("Image Snipping Tool")

    # File uploader allows user to add their own image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Convert the file to an image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # User input for cropping coordinates
        st.subheader("Specify cropping coordinates (left, top, right, bottom):")
        col1, col2, col3, col4 = st.columns(4)
        left = col1.number_input("Left", min_value=0, max_value=image.width, value=0)
        top = col2.number_input("Top", min_value=0, max_value=image.height, value=0)
        right = col3.number_input("Right", min_value=0, max_value=image.width, value=image.width)
        bottom = col4.number_input("Bottom", min_value=0, max_value=image.height, value=image.height)

        # Button to crop the image
        if st.button("Crop Image"):
            # Crop and display the image
            cropped_img = image.crop((left, top, right, bottom))
            st.image(cropped_img, use_column_width=True)

if __name__ == "__main__":
    main()
