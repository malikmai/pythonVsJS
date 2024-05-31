# Lab 2: Hangman

import random

def get_random_word():
    words = ["python", "hangman", "challenge", "terminal", "computer", "programming", "code", "developer", "software", "engineer", "debugging", "syntax", "error", "keyboard", "monitor", "mouse", "screen", "internet", "website", "server", "database", "algorithm", "function", "variable", "loop", "conditional", "statement", "object", "class", "method",]
    return random.choice(words)

print(get_random_word())
