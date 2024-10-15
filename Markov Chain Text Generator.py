import random
import re
from collections import defaultdict

# Constants
N_GRAM_ORDER = 1  # Unigram model
TEXT_LENGTH = 50  # Number of words to generate

def build_markov_chain(corpus, n=N_GRAM_ORDER):
    """
    Build a Markov chain model from the given text corpus.

    :param corpus: The input text corpus as a string.
    :param n: The order of the Markov chain (n-grams).
    :return: A dictionary representing the Markov chain model.
    """
    # Split the corpus into words
    words = re.findall(r'\b\w+\b', corpus.lower())
    markov_chain = defaultdict(lambda: defaultdict(int))

    # Build the Markov chain
    for i in range(len(words) - n):
        # Create the n-gram tuple
        current_state = tuple(words[i:i + n])
        next_state = words[i + n]
        markov_chain[current_state][next_state] += 1

    # Convert counts to probabilities
    for current_state, transitions in markov_chain.items():
        total_count = sum(transitions.values())
        for next_state in transitions:
            transitions[next_state] /= total_count

    return markov_chain

def generate_text(markov_chain, seed=None, length=TEXT_LENGTH):
    """
    Generate text using the Markov chain model.

    :param markov_chain: The Markov chain model as a dictionary.
    :param seed: The seed word(s) to start the text generation.
    :param length: The number of words to generate.
    :return: A generated text string.
    """
    if seed is None:
        # Randomly select a starting state
        seed = random.choice(list(markov_chain.keys()))

    current_state = seed
    output = list(current_state)

    for _ in range(length):
        # Get the next state probabilities
        next_states = markov_chain.get(current_state)
        if not next_states:
            break
        # Randomly choose the next state based on probabilities
        next_word = random.choices(list(next_states.keys()), weights=next_states.values())[0]
        output.append(next_word)

        # Move to the next state (shift window for n-gram model)
        current_state = (*current_state[1:], next_word)

    return ' '.join(output)

# Example usage
if __name__ == "__main__":
    # Sample text corpus
    text_corpus = """
    The quick brown fox jumps over the lazy dog. The quick brown fox is swift and agile.
    The dog is lazy but friendly. The fox and the dog are not friends, but they coexist peacefully.
    """

    # Build the Markov chain model
    markov_chain = build_markov_chain(text_corpus, n=N_GRAM_ORDER)

    # Generate text with the Markov chain model
    generated_text = generate_text(markov_chain, length=20)
    print(generated_text)
