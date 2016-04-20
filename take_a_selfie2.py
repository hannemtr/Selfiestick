import pyttsx
import pygame
import pygame.camera
import pygame.image
import speech_recognition as sr
from PIL import Image
import threading
import time
#import facebookupload
import talk_to_troll2

answer_given = False
useSpeaker = False
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
    return filename + '.bmp'


def speak(question, expression):
    if useSpeaker:
        talk_to_troll2.talker(question, expression)
    else:
        engine = pyttsx.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate + 0.5)
        engine.say(question)
        engine.runAndWait()

def obtain_audio(r, m):
    with m as source:
        r.adjust_for_ambient_noise(source)

def check_for_yes_or_no(r, audio):
    global answer_given
    try:
        recognized = r.recognize_google(audio, show_all=True)
        if len(recognized) == 0:
            return None
        alternatives = recognized['alternative']
        if len(alternatives) == 0:
            return None
        for alternative in alternatives:
            if alternative['transcript'] == 'yes':
                answer_given = True
                speak('Great, get behind the camera', "happy")
                for _ in range(5): time.sleep(1)
                speak('3', "smile")
                time.sleep(0.5)
                speak('2', "smile")
                time.sleep(0.5)
                speak('1', "smile")
                time.sleep(0.5)
                speak('Taking selfie...', talk_to_troll2.talk_random_expression())
                img = takePicture("picture")
                speak('Thank you, I have uploaded it to my facebook profile', "blink")
                return True
            if alternative['transcript'] == 'no':
                answer_given = True
                speak('No selfie taken...', "sad")
                return False
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        return None


def startListening(question, expression, r, michrophone):
    audio = obtain_audio(r, michrophone)
    stop_listening = r.listen_in_background(michrophone, check_for_yes_or_no)
    
    try:
        thread1 = threading.Thread(target = speak, args=(question, expression))
        thread1.start()
    except:
        print "failed"
        speak(question, expression)

    for _ in range(200):
        if answer_given: break;
        time.sleep(0.1)
    answer = stop_listening()
    print answer
    return answer



def main():
    global useSpeaker

    r = sr.Recognizer()
    michrophone = sr.Microphone()
    question = 'Would you like to take a selfie with me?'
    expression = "smile"
    useSpeaker = talk_to_troll2.createPub()


    answer = startListening(question, expression, r, michrophone)
    

    timesAsked = 1
    while not answer_given and timesAsked < 4:
        timesAsked += 1  
        question = 'I did not hear you, please repeat with yes or no.'
        expression = "surprise"

        answer = startListening(question, expression, r, michrophone)


main()
#img = takePicture("picture")
