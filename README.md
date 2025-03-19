# NanoGPT Nietzsche - Bigram Language Model

This project fine-tunes a GPT model on Friedrich Nietzsche’s Thus Spoke Zarathustra, based on Karpathy’s NanoGPT implementation. The goal is to explore philosophical text generation and analyze how well a transformer model can replicate Nietzsche’s writing style.

## Features
- Implementation of a Bigram Transformer-based Language Model.
- Training on Nietzsche's *Thus Spoke Zarathustra*.
- Generation of text with custom prompts.

## Model Overview
The model is a lightweight Transformer-based architecture with:
- Self-attention and feedforward layers.
- Positional embeddings for sequence modeling.
- Token embeddings for vocabulary handling.

## Training Details
- Dataset: *Thus Spoke Zarathustra* (Project Gutenberg)
- Hyperparameters:
  - Embedding size: 384
  - Number of layers: 6
  - Number of heads: 6
  - Context window: 128 tokens
- Training loss after 5000 steps: **1.64**
- Validation loss after 5000 steps: **1.85**

### Example Output
```text
Freeth of ill my from stals!.
It te cast all the reause hates, however...
