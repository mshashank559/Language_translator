from googletrans import Translator, LANGUAGES
import speech_recognition as sr
from gtts import gTTS
import pyttsx3

def speak(text):
    """Use text-to-speech to speak the given text."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """Use SpeechRecognition to listen to the user's speech."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        speak("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        speak("Recognizing...")
        text = recognizer.recognize_google(audio)
        speak(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, could not understand audio.")
        return ""

def translate_and_speak(text, source_lang, target_lang):
    """Translate text from source language to target language and speak the output."""
    translator = Translator()

    try:
        # Translate text
        translation = translator.translate(text, src=source_lang, dest=target_lang)
        translated_text = translation.text

        # Speak the translated output
        speak(translated_text)

        return translated_text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Ask user for input language
    speak("In which language do you want the translation?")
    source_lang = listen().lower()

    # Ask user for target language
    speak("To which language do you want the translation?")
    target_lang = listen().lower()

    # Ask user for text to translate
    speak("What do you want to translate?")
    text_to_translate = listen()

    # Notify listening
    speak("Listening...")

    # Translate text and speak
    translated_text = translate_and_speak(text_to_translate, source_lang, target_lang)

    # Display results
    speak("Translation Result:")
    speak(f"From ({source_lang}): {text_to_translate}")
    speak(f"To ({target_lang}): {translated_text}")
