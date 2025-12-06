#!/usr/bin/env python3
"""
Simple Chatbot Application
This chatbot uses pattern matching to respond to user inputs based on intents defined in intents.json
"""

import os
import sys
from utils import load_intents, get_words_and_classes, get_response

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
intents_file = os.path.join(script_dir, 'intents.json')

def main():
    """Main chatbot loop."""
    print("=" * 60)
    print("CHATBOT - Type 'quit' or 'exit' to end the conversation")
    print("=" * 60)
    print()
    
    # Load intents
    try:
        intents = load_intents(intents_file)
        print("✓ Intents loaded successfully!")
    except FileNotFoundError:
        print(f"✗ Error: Could not find {intents_file}")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error loading intents: {e}")
        sys.exit(1)
    
    # Extract words and classes
    words, classes, documents = get_words_and_classes(intents)
    print(f"✓ Vocabulary: {len(words)} unique words")
    print(f"✓ Intent classes: {len(classes)} categories")
    print()
    
    # Main chatbot loop
    print("Bot: Hello! I'm your chatbot. How can I help you?")
    print()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Bot: Goodbye! Have a great day!")
                break
            
            # Get response from chatbot
            response = get_response(user_input, intents, words, classes)
            print(f"Bot: {response}")
            print()
            
        except KeyboardInterrupt:
            print("\n\nBot: Goodbye! Have a great day!")
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()
