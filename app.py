import streamlit as st
import openai

# Set up OpenAI API key (ensure you have set up your OpenAI API key)
api_key = "sk-proj-P8f4FiSWVBJ1p787qJacT3BlbkFJmV0QcY73lt53ICD01aw2"

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
            max_tokens=50  # Adjust max_tokens according to your needs
        )

        # Extract the output from the response
        extracted_names = response["choices"][0]["text"]

        # Display the extracted names
        st.write("The names present in the text you provided are:")
        st.write(extracted_names.strip())  # Use strip() to remove extra whitespace
    else:
        st.warning("Please enter some text to extract names.")
