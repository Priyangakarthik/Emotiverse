# -*- coding: utf-8 -*-
"""Emotiverse.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VaOxbUc0SwgsV0u16Kq786iwZDzWakIl
"""

# Import basic libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from transformers import pipeline

# Load a sentiment analysis pipeline
emotion_classifier = pipeline('sentiment-analysis')

# Function to classify emotions
def classify_emotion(text):
    emotion = emotion_classifier(text)
    return emotion

# Test the function
text_input = "I feel so stressed and overwhelmed today."
emotion_result = classify_emotion(text_input)
print(emotion_result)

# Store journal entries
journal_entries = []

# Function to add journal entries
def add_journal_entry(entry):
    journal_entries.append(entry)
    print("Journal entry added!")

# Function to show all journal entries
def show_journal():
    return journal_entries

# Example of adding and showing entries
add_journal_entry("I am feeling a bit better after talking to a friend.")
print(show_journal())

# List of self-help tips
self_help_tips = [
    "Take a deep breath and relax your muscles.",
    "Write down 3 things you're grateful for.",
    "Challenge your negative thoughts by finding evidence against them."
]

# Function to suggest a self-help tip
def suggest_self_help():
    tip = np.random.choice(self_help_tips)
    return tip

# Test self-help suggestions
print(suggest_self_help())

# Function to mirror emotions back to the user
def mirror_emotion(text):
    emotion = classify_emotion(text)
    label = emotion[0]['label']

    if label == 'POSITIVE':
        response = "I can sense that you're feeling positive! That's great to hear."
    elif label == 'NEGATIVE':
        response = "It seems like you're feeling down. It's okay to feel this way sometimes."
    else:
        response = "You're experiencing a neutral mood. How about reflecting on what made you feel this way?"

    return response

# Test emotional mirroring
user_input = "I'm not feeling well today, it's been a tough day."
mirrored_response = mirror_emotion(user_input)
print(mirrored_response)

# Micro-task suggestions based on emotions
micro_tasks = {
    'NEGATIVE': [
        "Take 5 minutes to practice deep breathing.",
        "Go for a short walk and get some fresh air.",
        "Write down your thoughts to clear your mind."
    ],
    'POSITIVE': [
        "Take advantage of your good mood and start a new project!",
        "Share your happiness with someone close to you.",
        "Celebrate this moment by rewarding yourself."
    ],
    'NEUTRAL': [
        "How about organizing your workspace for a fresh start?",
        "Read a chapter from a book you’ve been wanting to read.",
        "Take a moment to reflect on your goals for the day."
    ]
}

# Function to suggest micro-tasks based on emotion
def suggest_micro_task(text):
    emotion = classify_emotion(text)
    label = emotion[0]['label']

    if label in micro_tasks:
        task = np.random.choice(micro_tasks[label])
        return task
    else:
        return "I'm not sure how you're feeling, but taking a short break always helps."

# Test micro-task intervention
print(suggest_micro_task("I feel anxious and stressed."))

# Simulate avatar expressions based on emotions
avatar_responses = {
    'POSITIVE': "😊 Your avatar smiles and looks joyful!",
    'NEGATIVE': "😟 Your avatar looks concerned and empathetic.",
    'NEUTRAL': "😐 Your avatar remains calm, reflecting a neutral mood."
}

# Function to reflect avatar's mood
def avatar_reflection(text):
    emotion = classify_emotion(text)
    label = emotion[0]['label']

    if label in avatar_responses:
        return avatar_responses[label]
    else:
        return "🤔 Your avatar looks thoughtful."

# Test avatar-based reflection
print(avatar_reflection("I'm feeling great today!"))

def emotiverse_chatbot(text):
    mirrored_response = mirror_emotion(text)
    task_suggestion = suggest_micro_task(text)
    avatar_feedback = avatar_reflection(text)

    return {
        "Mirrored Emotion": mirrored_response,
        "Micro-task": task_suggestion,
        "Avatar Response": avatar_feedback
    }

# Example conversation
user_input = "I've been feeling really stressed lately, and I don't know what to do."
response = emotiverse_chatbot(user_input)
print(response)

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load pre-trained model and tokenizer for emotion detection
tokenizer = AutoTokenizer.from_pretrained("bhadresh-savani/distilbert-base-uncased-emotion")
model = AutoModelForSequenceClassification.from_pretrained("bhadresh-savani/distilbert-base-uncased-emotion")

# Function to classify emotions using the advanced model
def advanced_emotion_detection(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    predictions = torch.softmax(outputs.logits, dim=-1)

    # Get the predicted emotion
    emotions = ["anger", "disgust", "fear", "joy", "neutral", "sadness", "surprise"] # Changed this line! Added all labels
    predicted_emotion_index = torch.argmax(predictions).item() # Use .item() for a pure python number

    # Handling index error with a check
    if 0 <= predicted_emotion_index < len(emotions):
        predicted_emotion = emotions[predicted_emotion_index]
    else:
        predicted_emotion = "unknown"  # Default to "unknown" if index is invalid

    return predicted_emotion

# Test the advanced emotion detection
print(advanced_emotion_detection("I am feeling anxious and nervous."))

# Simple text-based interaction loop
def emotiverse_ui():
    print("Welcome to EmotiVerse! Let's talk about how you're feeling today.")
    while True:
        user_input = input("You: ")

        if user_input.lower() in ['quit', 'exit']:
            print("Thank you for sharing. Take care!")
            break

        # Chatbot response
        response = emotiverse_chatbot(user_input)
        print("\nEmotiVerse:")
        print(f"Mirrored Emotion: {response['Mirrored Emotion']}")
        print(f"Suggested Micro-task: {response['Micro-task']}")
        print(f"Avatar Response: {response['Avatar Response']}")
        print("\n")

# Test the EmotiVerse UI
emotiverse_ui()

# Install Streamlit if needed
import streamlit as st

def streamlit_emotiverse():
    st.title("EmotiVerse - Your Mental Health Companion")

    user_input = st.text_input("How are you feeling today?")

    if user_input:
        response = emotiverse_chatbot(user_input)

        st.write("**Mirrored Emotion**: ", response['Mirrored Emotion'])
        st.write("**Micro-task Suggestion**: ", response['Micro-task'])
        st.write("**Avatar Response**: ", response['Avatar Response'])

import streamlit as st

# Streamlit app function
def emotiverse_streamlit():
    st.title("EmotiVerse - Your Mental Health Companion")

    st.markdown("Welcome to **EmotiVerse**. Here you can share how you're feeling, and we'll suggest some tasks and reflective feedback based on your emotions.")

    # Get user input
    user_input = st.text_area("How are you feeling today?", placeholder="Describe your emotions...")

    if user_input:
        # Get chatbot responses
        response = emotiverse_chatbot(user_input)

        # Display the chatbot responses
        st.subheader("EmotiVerse Responses:")
        st.write("**Mirrored Emotion:** ", response['Mirrored Emotion'])
        st.write("**Micro-task Suggestion:** ", response['Micro-task'])
        st.write("**Avatar Response:** ", response['Avatar Response'])

    st.write("**Tip:** Type 'exit' to end the conversation.")

# Run the Streamlit app
if __name__ == '__main__':
    emotiverse_streamlit()

# Writing the code to a file in Google Colab
code = """
import streamlit as st
from transformers import pipeline

# Pre-trained sentiment analysis model for emotions
emotion_classifier = pipeline('sentiment-analysis')

# Function to classify emotions
def classify_emotion(text):
    emotion = emotion_classifier(text)
    return emotion

# Function to mirror emotions back to the user
def mirror_emotion(text):
    emotion = classify_emotion(text)
    label = emotion[0]['label']

    if label == 'POSITIVE':
        response = "I can sense that you're feeling positive! That's great to hear."
    elif label == 'NEGATIVE':
        response = "It seems like you're feeling down. It's okay to feel this way sometimes."
    else:
        response = "You're experiencing a neutral mood. How about reflecting on what made you feel this way?"

    return response

# Function to suggest micro-tasks based on emotion
def suggest_micro_task(text):
    micro_tasks = {
        'NEGATIVE': [
            "Take 5 minutes to practice deep breathing.",
            "Go for a short walk and get some fresh air.",
            "Write down your thoughts to clear your mind."
        ],
        'POSITIVE': [
            "Take advantage of your good mood and start a new project!",
            "Share your happiness with someone close to you.",
            "Celebrate this moment by rewarding yourself."
        ],
        'NEUTRAL': [
            "How about organizing your workspace for a fresh start?",
            "Read a chapter from a book you’ve been wanting to read.",
            "Take a moment to reflect on your goals for the day."
        ]
    }

    emotion = classify_emotion(text)
    label = emotion[0]['label']

    if label in micro_tasks:
        task = np.random.choice(micro_tasks[label])
        return task
    else:
        return "I'm not sure how you're feeling, but taking a short break always helps."

# Avatar responses
avatar_responses = {
    'POSITIVE': "😊 Your avatar smiles and looks joyful!",
    'NEGATIVE': "😟 Your avatar looks concerned and empathetic.",
    'NEUTRAL': "😐 Your avatar remains calm, reflecting a neutral mood."
}

# Function to reflect avatar's mood
def avatar_reflection(text):
    emotion = classify_emotion(text)
    label = emotion[0]['label']

    if label in avatar_responses:
        return avatar_responses[label]
    else:
        return "🤔 Your avatar looks thoughtful."

# Combine all functions for EmotiVerse chatbot
def emotiverse_chatbot(text):
    mirrored_response = mirror_emotion(text)
    task_suggestion = suggest_micro_task(text)
    avatar_feedback = avatar_reflection(text)

    return {
        "Mirrored Emotion": mirrored_response,
        "Micro-task": task_suggestion,
        "Avatar Response": avatar_feedback
    }

# Streamlit app function
def emotiverse_streamlit():
    st.title("EmotiVerse - Your Mental Health Companion")

    st.markdown("Welcome to **EmotiVerse**. Share your thoughts, and we'll provide tasks and reflections based on your emotions.")

    # Get user input
    user_input = st.text_area("How are you feeling today?", placeholder="Describe your emotions...")

    if user_input:
        # Get chatbot responses
        response = emotiverse_chatbot(user_input)

        # Display the chatbot responses
        st.subheader("EmotiVerse Responses:")
        st.write("**Mirrored Emotion:** ", response['Mirrored Emotion'])
        st.write("**Micro-task Suggestion:** ", response['Micro-task'])
        st.write("**Avatar Response:** ", response['Avatar Response'])

    st.write("**Tip:** Type 'exit' to end the conversation.")

# Run the Streamlit app
if __name__ == '__main__':
    emotiverse_streamlit()
"""

# Write the code to a file named 'emotiverse_chatbot.py'
with open("emotiverse_chatbot.py", "w") as file:
    file.write(code)

# Adding avatar images based on emotions (you can use emoji as placeholders for now)
avatar_images = {
    'POSITIVE': "😊",
    'NEGATIVE': "😟",
    'NEUTRAL': "😐"
}

def emotiverse_streamlit_with_avatars():
    st.title("EmotiVerse - Your Mental Health Companion")

    user_input = st.text_area("How are you feeling today?", placeholder="Describe your emotions...")

    if user_input:
        # Get chatbot responses
        response = emotiverse_chatbot(user_input)

        # Display the chatbot responses
        st.subheader("EmotiVerse Responses:")
        st.write("**Mirrored Emotion:** ", response['Mirrored Emotion'])
        st.write("**Micro-task Suggestion:** ", response['Micro-task'])
        st.write("**Avatar Response:** ", avatar_images.get(response['Mirrored Emotion'].split()[0], "🤔"))

    st.write("**Tip:** Type 'exit' to end the conversation.")

# To run the updated app with avatars
emotiverse_streamlit_with_avatars()

import pandas as pd
from datetime import datetime

# Function to store chatbot data
def store_data(user_input, mirrored_emotion, micro_task, avatar_response):
    # Create a dictionary for the data
    data = {
        'Timestamp': [datetime.now()],
        'User Input': [user_input],
        'Mirrored Emotion': [mirrored_emotion],
        'Micro-task': [micro_task],
        'Avatar Response': [avatar_response]
    }

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Append the data to a CSV file
    df.to_csv('emotiverse_data.csv', mode='a', header=False, index=False)

# Call this function in the chatbot after generating responses
store_data(user_input, response['Mirrored Emotion'], response['Micro-task'], response['Avatar Response'])

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load pre-trained model and tokenizer for emotion detection
tokenizer = AutoTokenizer.from_pretrained("bhadresh-savani/distilbert-base-uncased-emotion")
model = AutoModelForSequenceClassification.from_pretrained("bhadresh-savani/distilbert-base-uncased-emotion")

# Function to classify emotions using the advanced model
def advanced_emotion_detection(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    predictions = torch.softmax(outputs.logits, dim=-1)

    # Get the predicted emotion
    emotions = ["anger", "joy", "optimism", "sadness"]
    predicted_emotion = emotions[torch.argmax(predictions)]
    return predicted_emotion

# Use this model for more accurate emotion detection
print(advanced_emotion_detection("I'm feeling so happy and excited!"))

# Example: Ask the user for their name
user_name = st.text_input("What's your name?", placeholder="Enter your name")

if user_name:
    st.write(f"Hi {user_name}, how are you feeling today?")

avatar_images = {
    'POSITIVE': "positive_avatar.png",
    'NEGATIVE': "negative_avatar.png",
    'NEUTRAL': "neutral_avatar.png"
}

def avatar_reflection(text):
    emotion = classify_emotion(text)
    label = emotion[0]['label']

    if label in avatar_images:
        st.image(avatar_images[label], width=100)
    else:
        st.write("🤔")

import matplotlib.pyplot as plt

def plot_emotion_trend():
    try:
        df = pd.read_csv('emotiverse_data.csv')
        # Assuming the first column contains the timestamp, and it's unnamed
        df.columns = ['Timestamp', 'User Input', 'Mirrored Emotion', 'Micro-task', 'Avatar Response']
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    except KeyError as e:
          print(f"Error: Column '{e}' not found in the CSV. Check your CSV file.")
          return # or handle the error in a way that makes sense for your application

# ... rest of the function remains the same ...

