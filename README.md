# Markov Chain Text Generator

This project implements a simple Markov Chain model for text generation. It builds a model from an input text corpus and generates new text based on the probabilistic transition of words using n-grams.

## Features

- **Markov Chain Model**: Uses n-grams to model word transitions.
- **Customizable**: You can specify the order of the Markov chain (n-grams) and the length of generated text.
- **Simple and Lightweight**: No external dependencies, purely built using Python's standard libraries.

## How It Works

1. **Build Markov Chain**: The `build_markov_chain` function processes a given text corpus and creates a Markov Chain model. You can adjust the order `n` for n-grams.
2. **Generate Text**: The `generate_text` function generates random text using the created Markov Chain, given a starting seed and desired output length.

## Prerequisites

- Python 3.x
- No additional external libraries are required, as only Python's built-in libraries are used (`random`, `re`, `collections`).

## Installation

1. Clone the repository:

```bash
git clone https://github.com/thedivyanshpant/Prodigy_GA_03.git
