#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import tts

def obtain_audio(r):
    with sr.Microphone() as source:
        audio = r.listen(source)
        return audio

def check_for_yes_or_no(audio, r):
    try:
        alternatives = r.recognize_google(audio, show_all=True)['alternative']
        if len(alternatives) == 0:
            return None
        for alternative in alternatives:
            if alternative['transcript'] == 'yes':
                return True
            if alternative['transcript'] == 'no':
                return False
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        return None

def main():
    r = sr.Recognizer()
    tts.askForSelfie()
    audio = obtain_audio(r)
    answer = check_for_yes_or_no(audio, r)
    while answer == None:
        print('I did not hear you, please repeat.')
        audio = obtain_audio(r)
        answer = check_for_yes_or_no(audio, r)
    if answer:
        print('Taking selfie...')
    else:
        print('No selfie :(')

main()