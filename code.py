from purple.core import Core

#from purple.keyboard.mist.keyboard import keys
#from purple.keyboard.calc.keyboard import keys
import purple.keyboard.calc.keyboard as kbd
keys = kbd.keys
use_led = kbd.use_led
from purple.keyboard.calc.layout.simple_alphabet import Layout

from purple.extras.performance_counter import PerformanceCounter
if use_led:
    from purple.extras.hardware.led import LED
    led = LED()
else:
    led = False

Core(keys, Layout, led, PerformanceCounter()).run()
