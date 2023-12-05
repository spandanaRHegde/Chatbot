import nltk

# Define the patterns and responses for the chatbot
pairs = [
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi, how can I help you?"]
    ],
    [
        r"what is your name?",
        ["You can call me ChatBot.", "I'm ChatBot, nice to meet you!"]
    ],
    [
        r"how are you?",
        ["I'm good, thank you!", "I'm doing great, how about you?"]
    ],
    [
        r"(.*) your name?",
        ["My name is ChatBot.", "You can call me ChatBot."]
    ],
    [
        r"(.*) (age|old) ?",
        ["I'm a computer program, so I don't have an age."]
    ],
    [
        r"(.*) (location|located) ?",
        ["I'm a virtual friend, so I don't have a physical location."]
    ],
    [
        r"(.*) (weather|temperature) ?",
        ["Sorry, I don't have access to real-time weather information."]
    ],
    [
        r"quit",
        ["It was nice talking to you. Goodbye!", "Goodbye! Have a great day!"]
    ]
]

# Create the chatbot

# Start the conversation
chatbot.converse()