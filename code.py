from purple.core import Core

from purple.keyboard.sweep.left import keys
from purple.keyboard.sweep.layout.soar import Layout

from purple.extras.performance_counter import PerformanceCounter
from purple.extras.hardware.led import LED

Core(keys, Layout, LED(), PerformanceCounter()).run()
