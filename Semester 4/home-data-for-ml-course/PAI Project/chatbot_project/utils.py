import json
import random
import re
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np

lemmatizer = WordNetLemmatizer()

def load_intents(filename):
    """Load intents from a JSON file."""
    with open(filename, 'r') as file:
        intents = json.load(file)
    return intents['intents']

def preprocess_text(text):
    """Convert text to lowercase and remove special characters."""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

def tokenize_and_lemmatize(text):
    """Tokenize and lemmatize text."""
    words = text.split()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return lemmatized_words

def get_words_and_classes(intents):
    """Extract all unique words and classes from intents."""
    words = []
    classes = []
    documents = []
    
    for intent in intents:
        for pattern in intent['patterns']:
            tokens = tokenize_and_lemmatize(preprocess_text(pattern))
            words.extend(tokens)
            documents.append((tokens, intent['tag']))
        
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
    
    words = sorted(set(words))
    classes = sorted(set(classes))
    
    return words, classes, documents

def create_training_data(words, classes, documents):
    """Create training data for the model."""
    X_train = []
    y_train = []
    
    for tokens, tag in documents:
        # Create bag of words
        bag = [1 if word in tokens else 0 for word in words]
        X_train.append(bag)
        
        # Create output
        output = [1 if cls == tag else 0 for cls in classes]
        y_train.append(output)
    
    return np.array(X_train), np.array(y_train)

def find_best_match(user_input, intents, words, classes, model=None):
    """Find the best matching intent for user input."""
    tokens = tokenize_and_lemmatize(preprocess_text(user_input))
    bag = [1 if word in tokens else 0 for word in words]
    
    if model is not None:
        prediction = model.predict([bag])[0]
        intent_index = np.argmax(prediction)
        confidence = np.max(prediction)
        
        if confidence < 0.5:
            return None, None
        
        intent_tag = classes[intent_index]
    else:
        # Simple matching without model
        max_matches = 0
        intent_tag = None
        
        for intent in intents:
            for pattern in intent['patterns']:
                pattern_tokens = tokenize_and_lemmatize(preprocess_text(pattern))
                matches = len(set(tokens) & set(pattern_tokens))
                
                if matches > max_matches:
                    max_matches = matches
                    intent_tag = intent['tag']
        
        if max_matches == 0:
            return None, None
    
    # Find the intent and return a random response
    for intent in intents:
        if intent['tag'] == intent_tag:
            response = random.choice(intent['responses'])
            return intent_tag, response
    
    return None, None

def get_response(user_input, intents, words=None, classes=None, model=None):
    """Get a response from the chatbot.

    This function is backward-compatible: if `words` and `classes` are not
    provided (as is the case when called from `app.py`), it will compute them
    from the provided `intents` data.
    """
    if words is None or classes is None:
        words, classes, _ = get_words_and_classes(intents)

    tag, response = find_best_match(user_input, intents, words, classes, model)

    if response:
        return response
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"
