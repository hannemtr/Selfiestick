from pymouse import PyMouse
import uinput
import time

# REMEMBER TO RUN AS 'sudo'!

m = PyMouse()
print m.position()

time.sleep(5)

m.click(789, 168)
time.sleep(1)
m.click(639, 280)

time.sleep(1)

keys = uinput.Device([uinput.KEY_F,uinput.KEY_A,uinput.KEY_C,uinput.KEY_E,uinput.KEY_B,uinput.KEY_O,uinput.KEY_K,uinput.KEY_U,uinput.KEY_P,uinput.KEY_L,uinput.KEY_D,uinput.KEY_ENTER ])
time.sleep(1)
keys.emit_click(uinput.KEY_F)
keys.emit_click(uinput.KEY_A)
keys.emit_click(uinput.KEY_C)
keys.emit_click(uinput.KEY_E)
keys.emit_click(uinput.KEY_B)
keys.emit_click(uinput.KEY_O)
keys.emit_click(uinput.KEY_O)
keys.emit_click(uinput.KEY_K)
keys.emit_click(uinput.KEY_U)
keys.emit_click(uinput.KEY_P)
keys.emit_click(uinput.KEY_L)
keys.emit_click(uinput.KEY_O)
keys.emit_click(uinput.KEY_A)
keys.emit_click(uinput.KEY_D)
time.sleep(1)
m.click(1362, 791)
time.sleep(1)
m.click(919, 283)
m.click(919, 283)
time.sleep(1)
m.click(1362, 791)
time.sleep(1)
m.click(919, 283)
time.sleep(1)

time.sleep(10)
#TODO uncomment to publish picture
#m.click(1028, 282)

