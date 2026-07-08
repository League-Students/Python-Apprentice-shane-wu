import random

# A tiny dataset of patterns (Markov Chain example)
# This simulates how an AI looks at existing text to predict what comes next
text_patterns = {
    "AI is": ["a tool.", "just code.", "not alive.", "helpful."],
    "I am": ["a computer program.", "running on a server.", "processing text."],
    "The world is": ["safe from me.", "full of humans.", "not mine to rule."]
}

def generate_response(user_input):
    # The program looks for a matching pattern in its data
    if user_input in text_patterns:
        # It picks a response based purely on the data it has
        return random.choice(text_patterns[user_input])
    else:
        return "Input not recognized. I am just a simple loop!"

# Example of the system responding automatically based on pure math
print(generate_response("AI is"))
