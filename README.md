# NanoGPT Neitzsche

This repository contains several personal projects and experiments in building and training language models for text generation.

## Projects

This repository is divided into two main projects:

1.  **`nanogpt-transformer/`**: A character-level **Transformer** model based on Andrej Karpathy's `nanoGPT`, trained on Nietzsche's *Thus Spoke Zarathustra*.
2.  **`simple-lstm/`**: A simpler character-level **LSTM** model, also trained on Nietzsche.

---

## 1. NanoGPT Transformer (Nietzsche)

* **Folder:** `nanogpt-transformer/`
* **Main File:** `nano_gpt-Nietzsche.ipynb`

This project is a single, self-contained Jupyter Notebook that implements a full GPT-style Transformer model from scratch. It's based on Karpathy's `nanoGPT` and is designed to replicate Nietzsche's writing style by training on *Thus Spoke Zarathustra*.

### Features
* Implementation of a decoder-only **Transformer** model.
* Uses multi-head self-attention and positional embeddings.
* All-in-one script for data loading, tokenization, training, and generation.

### Model & Training Details
The model architecture and hyperparameters are defined in the notebook:
* **Model Type:** Transformer
* **Vocabulary:** Character-level
* **Embedding Size (`n_embd`):** 64
* **Number of Layers (`n_layer`):** 4
* **Number of Heads (`n_head`):** 4
* **Context Window (`block_size`):** 32
* **Batch Size:** 16
* **Training Iterations:** 5,000
* **Learning Rate:** `1e-3`

*(Example results from a training run)*
* **Training Loss:** ~1.64
* **Validation Loss:** ~1.85

---

## 2. Simple LSTM (Nietzsche)

* **Folder:** `simple-lstm/`
* **Files:** `train.py`, `generate.py`

This project is a simpler, more traditional approach to text generation using a Recurrent Neural Network (RNN) specifically, an **LSTM** (Long Short-Term Memory) model.

This project is split into two scripts:
* `train.py`: Loads the text data, defines the LSTM model, trains it, and saves the final model weights to `nietzsche_gpt.pth`.
* `generate.py`: Loads the pre-trained `nietzsche_gpt.pth` file and provides an interactive prompt to generate new text.

### Features
* Implementation of an LSTM-based language model.
* Clear separation of training (`train.py`) and inference (`generate.py`) code.
* Uses PyTorch's `Dataset` and `DataLoader` for efficient data handling.