import pyttsx


def askForSelfie():
	engine = pyttsx.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate+0.5)
	engine.say('Will you take a selfie with me?')
	engine.runAndWait()

