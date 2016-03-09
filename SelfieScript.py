import pyttsx
import pygame
import pygame.camera
import pygame.image
import speech_recognition as sr
from PIL import Image


def takePicture(filename):
	pygame.init()
    pygame.camera.init()
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    cam.start()
    img = cam.get_image()
    pygame.image.save(img, filename + '.bmp')
	cam.stop()
	pygame.camera.quit()
	pygame.quit()


def speak(str):
    print(str)
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + 0.5)
    engine.say(str)
    engine.runAndWait()

def obtain_audio(r):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        return audio

def check_for_yes_or_no(audio, r):
    try:
        recognized = r.recognize_google(audio, show_all=True)
        if len(recognized) == 0:
            return None
        alternatives = recognized['alternative']
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
    speak('Would you like to take a selfie with me?')
    audio = obtain_audio(r)
    answer = check_for_yes_or_no(audio, r)
    while answer == None:
        speak('I did not hear you, please repeat with yes or no.')
        audio = obtain_audio(r)
        answer = check_for_yes_or_no(audio, r)
    if answer:
        speak('Taking selfie...')
        takePicture("picture")
        Image.open('picture.bmp').show()
    else:
        speak('No selfie taken... :(')

main()
