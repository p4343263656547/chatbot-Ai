# Nepali Kancha AI Assistant - Created by Prashanta Sir

import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import openai

# Replace with your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"


# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print(f"AI: {text}")
    engine.say(text)
    engine.runAndWait()

def greet():
    speak("Hello! I am Nepali Kancha, your AI assistant.")
    speak("I was created by Prashanta Sir.")
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I help you today?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
    except:
        speak("Sorry, I didn't catch that.")
        return ""
    return command.lower()

def ask_gpt(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Nepali Kancha, a helpful assistant created by Prashanta Sir."},
                {"role": "user", "content": question}
            ]
        )
        answer = response['choices'][0]['message']['content']
        return answer.strip()
    except Exception as e:
        return "Sorry, I couldn't connect to the AI right now."

def run_ai():
    greet()
    while True:
        command = take_command()

        if "open youtube" in command:
            speak("Opening YouTube...")
            webbrowser.open("https://youtube.com")
            
        if "open facebook" in command:
            speak("opening Facebook...")
            webbrowser.open("https://facebook.com")

        if "open google" in command:
            speak("opening Google...")
            webbrowser.open("https://google.com")

        if "open instagram" in command:
           speak("opening Instagram...")
           webbrowser.open("https://instagram.com")
        if "open whatsapp" in command:
            speak("opening WhatsApp...")
            webbrowser.open("https://web.whatsapp.com")
            
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        elif "exit" in command or "stop" in command:
            speak("Goodbye! Have a nice day.")
            break

        elif command:
            speak("Let me think...")
            ai_reply = ask_gpt(command)
            speak(ai_reply)

if __name__ == "__main__":
    run_ai()
