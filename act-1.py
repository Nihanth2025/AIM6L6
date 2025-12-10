import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import asyncio

def speak(text, language='en'):
    print("\n Welcome to SPEAK function!!!!!!!!!!")
    engine=pyttsx3.init()
    engine.setProperty('rate', 150)
    voices=engine.getProperty('voices')
    if language=='es':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
def speech_to_text():
    recogniser=sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak in now english...")
        audio=recogniser.listen(source)
    try:
        print("Recognising speech...")
        text=recogniser.recognize_google(audio, language='en-US')
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio")
    except sr.RequestError as e:
        print("Api error:{e}")
    return ""
async def translate_text(text, target_language='es'):
    translator=Translator()
    translation=translator.translate(text, dest=target_language)
    print(f"Translated text: {translation}")
    return translation
def display_language_options():
    print("Available translation languages:")
    print("1.hindi (hi)")
    print("2.tamil (ta)")
    print("3.telugu (te)")
    print("4.bengali (be)")
    print("5.marathi (ma)")
    print("6.gujarati (gu)")
    print("7.malyalam (ma)")
    print("8.punjabi (pu)")
    choice=input("Select your language (1-8): ")
    language_dict={
        '1': 'hi',
        '2': 'ta',
        '3': 'te',
        '4': 'be',
        '5': 'ma',
        '6': 'gu',
        '7': 'ma',
        '8': 'pu'
    }
    return language_dict.get(choice, 'es')
async def main():
    target_language=display_language_options()
    original_text=speech_to_text()
    if original_text:
        translated_text=await translate_text(original_text, target_language)
        speak(translated_text, target_language)
        print("Translation completed successfully")
if __name__=="__main__":
    asyncio.run(main())
