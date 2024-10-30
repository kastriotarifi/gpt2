from flask import Flask, render_template, request, jsonify
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)

# Load GPT-2 model and tokenizer
model_name = "gpt2"  # You can use "gpt2-medium" or other versions if needed
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.json.get('message', '')
    
    # Encode the input and generate a response
    input_ids = tokenizer.encode(user_input, return_tensors='pt')
    response_ids = model.generate(input_ids, max_length=50, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    response_text = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    
    return jsonify(response=response_text)

if __name__ == '__main__':
    app.run(debug=True)
