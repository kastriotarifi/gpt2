import streamlit as st
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the model and tokenizer
model_name = "gpt2"  # You can use "gpt2-medium" or other versions if needed
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Set the title of the app
st.title("GPT-2 Chatbot")

# Chat history
chat_history = []

# User input
user_input = st.text_input("Type your message here:")

if st.button("Send"):
    # Encode the input and generate a response
    input_ids = tokenizer.encode(user_input, return_tensors='pt')
    response_ids = model.generate(input_ids, max_length=50, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    response_text = tokenizer.decode(response_ids[0], skip_special_tokens=True)

    # Store messages in chat history
    chat_history.append(("User", user_input))
    chat_history.append(("GPT-2", response_text))

# Display chat history
for speaker, message in chat_history:
    st.markdown(f"**{speaker}:** {message}")

