from purple.core import Core

from purple.keyboard.mist.keyboard import keys
from purple.keyboard.mist.layout.soar_left import Layout

from purple.extras.performance_counter import PerformanceCounter
from purple.extras.hardware.led import LED

Core(keys, Layout, LED(), PerformanceCounter()).run()
