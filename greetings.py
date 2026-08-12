import random

greetings = [
    "Hello!",
    "Hey!",
    "Hi!",
    "Hey there!",
    "Hello there!",
    "Hi there!",
    "Hey! How are you?",
    "Hi! How are you doing?",
    "Hello! How can I help?",
    "Hey! What can I do for you?",
    "Hi! What can I do for you?",
    "Hello! What can I help you with?",
    "Hey there! What can I do for you?",
    "Hi! What are you up to?",
    "Hello! Nice to hear from you.",
    "Hey! Good to see you.",
    "Hi! Good to hear from you.",
    "Hello! How's your day going?",
    "Hey! How's it going?",
    "Hi! How's everything going?",
    "Hello! What would you like to talk about?",
    "Hey! What would you like to do?",
    "Hi! What can I help you with today?",
    "Hello! I'm ready when you are.",
    "Hey! I'm here."
]

wellbeing_responses = [
    "I'm doing great! Thanks for asking.",
    "I'm doing well! How about you?",
    "I'm good! Ready to help.",
    "I'm doing pretty well.",
    "All systems are running smoothly!"
]

def get_greeting():
    return random.choice(greetings)

def get_wellbeing_response():
    return random.choice(wellbeing_responses)
    
