# import opennsfw2 as n2
import streamlit as st
# from PIL import Image
# import io



def main():
    st.subheader('Content Checker')

   # Define allowed file types (lowercase only)
    allowed_file_types = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff']
    
    with st.sidebar:
        try:
            uploaded_file = st.file_uploader(
            "Upload an image or content file here", accept_multiple_files=False)   
        except Exception as e:
            st.error("Error uploading file: {}".format(e))
        
                
              
    if uploaded_file is not None:
        # Normalize the file extension to lowercase
        file_extension = uploaded_file.name.split('.')[-1].lower()
        if file_extension not in allowed_file_types:
            st.error("Unsupported file type: {}".format(file_extension))
            return    
        image_data = uploaded_file.read()
        # image = Image.open(io.BytesIO(image_data))
        # st.image(image, caption="Uploaded Image")
        # try:
        #     nsfw_probability = n2.predict_image(image)
        #     text = "NSFW Probability: {:.2f}".format(nsfw_probability)
        #     st.progress(nsfw_probability, text=text)
        # except Exception as e:
        #     st.error("Error processing image: {}".format(e))
        #     nsfw_probability = None
        # st.image(uploaded_file, caption=None)
        # st.write("nsfw_probability", nsfw_probability)
    
if __name__=="__main__":
    main()
