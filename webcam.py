import pygame.camera
import pygame.image

def takePicture(filename):
	pygame.camera.init()
	cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
	cam.start()
	img = cam.get_image()
	pygame.image.save(img, filename + '.bmp')
	pygame.camera.quit()

def main():
	takePicture('test')

main()