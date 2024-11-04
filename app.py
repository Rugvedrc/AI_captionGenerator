import streamlit as st
import google.generativeai as genai
import PIL.Image
import io

# Function to generate captions
def generate_captions(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    response = model.generate_content([prompt,img], stream=False)
    
    # Extract only the captions (assuming they come after the introductory text)
    captions = response.text.split('\n', 1)[1]  # Split by newline and get the captions part
    return captions

# Streamlit GUI
st.title("Creative Caption Generator")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    img = PIL.Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)
    
    # Input prompt for generating captions
    st.write("Suggest creative captions for the uploaded image:")
    if st.button("Generate Captions"):
        prompt = "Suggest 3 short and creative captions for a picture"
        captions = generate_captions(prompt)
        st.write("Generated Captions:")
        st.write(captions)

# Directly configure API key for testing
genai.configure(api_key="YOUR_API_KEY")
