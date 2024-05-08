import streamlit as st
import openai

# Get the OpenAI API key from Streamlit secrets
api_key = st.secrets["OPENAI_API_KEY"]

# Create a simple Streamlit app
st.title("Name Extractor using OpenAI GPT")

# Get the text input from the user
text_input = st.text_area("Enter your text here:")

# Button to trigger the name extraction
if st.button("Extract Names"):
    # If text input is not empty, make an API call
    if text_input:
        openai.api_key = api_key

        # Define the prompt for name extraction
        prompt = f"Extract all the names from the following text: {text_input}"

        # Make a request to the OpenAI model
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )

        # Extract the output from the response
        extracted_names = response["choices"][0]["text"]

        # Display the extracted names
        st.write("The names present in the text you provided are:")
        st.write(extracted_names.strip())  # Remove leading/trailing whitespace
    else:
        st.warning("Please enter some text to extract names.")
