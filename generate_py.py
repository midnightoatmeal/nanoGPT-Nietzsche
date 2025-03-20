# -*- coding: utf-8 -*-
"""generate.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OGAdupWyIOzoDJe3NZ4mwzdCoKMBNo78
"""

import torch
import torch.nn as nn
import random
import os

# Load character mappings
chars = sorted(set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,!?'-\n"))
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for ch, i in stoi.items()}
VOCAB_SIZE = len(chars)

# Model Definition (Same as training)
class SimpleGPT(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, vocab_size)

    def forward(self, x, hidden=None):
        x = self.embedding(x)
        x, hidden = self.lstm(x, hidden)
        x = self.fc(x)
        return x, hidden

# Load trained model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = SimpleGPT(VOCAB_SIZE, 256, 512).to(device)

if os.path.exists("nietzsche_gpt.pth"):
    model.load_state_dict(torch.load("nietzsche_gpt.pth", map_location=device))
    model.eval()
    print("Model loaded successfully!")
else:
    print("Model file not found! Please train the model first.")
    exit()

# Function to generate text
def generate_text(prompt, length=200, temperature=1.0):
    model.eval()
    input_seq = torch.tensor([stoi[ch] for ch in prompt if ch in stoi], dtype=torch.long).unsqueeze(0).to(device)
    hidden = None
    output_text = prompt

    for _ in range(length):
        with torch.no_grad():
            logits, hidden = model(input_seq, hidden)
            logits = logits[:, -1, :] / temperature  # Scale logits by temperature
            probs = torch.softmax(logits, dim=-1).cpu().numpy().flatten()
            next_char_index = random.choices(range(VOCAB_SIZE), weights=probs)[0]
            next_char = itos[next_char_index]
            output_text += next_char
            input_seq = torch.tensor([[next_char_index]], dtype=torch.long).to(device)

    return output_text

# Interactive prompt
if __name__ == "__main__":
    prompt = input("Enter a Nietzschean-style prompt: ")
    generated_text = generate_text(prompt, length=500, temperature=0.8)
    print("\n📝 Generated Text:\n")
    print(generated_text)

