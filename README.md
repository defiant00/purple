# purple

[CircuitPython](https://circuitpython.org/) firmware for one-handed chording keyboards based on the [KB2040](https://learn.adafruit.com/adafruit-kb2040) and other RP2040-based boards from [adafruit](https://www.adafruit.com/)!

## Features

* Layers!
* Map chords to key combinations on tap or hold.
* Map normal keys, media keys, and the mouse.
* One-shot modifiers.
* Auto Mod for if you want to apply a modifier globally on hold.
* LED layer and modifier state indicators.
    * Layers have a color.
    * When modifiers are active, the LED blinks a color for each in turn:
        * Yellow - Shift
        * Red - Control
        * Blue - Alt
        * Pink - GUI
    * On locked keys the LED pulses.

## Usage

1. Follow the quickstart [here](https://learn.adafruit.com/adafruit-kb2040/circuitpython) to set up your board with CircuitPython.
2. Copy required libraries to your `CIRCUITPY/lib` folder:
    1. `adafruit_hid` (whole folder)
    2. `adafruit_debouncer.mpy`
    3. `adafruit_pixelbuf.mpy`
    4. `neopixel.mpy`
3. Edit `code.py` imports to import the keyboard, layout, and any extras you want to use.
4. Copy `code.py` and the `purple` folder to your `CIRCUITPY` drive.

### Extras

The core engine handles basic input and state management. All extra functionality and optional hardware is broken out into extras so that it can be enabled or disabled at will. Extras can be added after the keyboard and layout in `code.py`.

## Development

### General Customization

`core.py` contains some useful values that can be adjusted:
* `_HOLD_DELAY` - How long to wait in ms before a key is considered held.
* `_MOUSE_REPEAT_RATE` - How long to wait in ms before repeating a mouse movement when the key is held.

`extras/hardware/led.py` contains values for using the built-in LED to indicate status:
* `_MODIFIER_BLINK` - How long to wait between modifier blinks.
* `_MODIFIER_BLINK_ON` - How long to turn on the LED per modifier blink.
* `_MOD_COLORS` - The LED color tuple `(r, g, b)` to use for the modifier. Should be a bright value so it can be seen when on layers.
* `_LOCK_FADE` - How long the LED takes to fade in or out to indicate locked keys.
* `_LOCK_FADE_MIN` - The minimum brightness multiple when keys are locked.
* `_LOCK_FADE_NO_COLOR` - The LED color tuple `(r, g, b)` to use when a key is locked and the current color would otherwise be black.

### Creating a new Keyboard

`purple/keyboard/[kb_name]/[board].py`
* `kb_name` - The name of the keyboard.
* `board` - `keyboard` for a single board. `left` or `right` if it's a split board.

A keyboard defines a list of `Key` objects specifying the board pins, eg:
```python
keys = [
    Key(DigitalInOut(board.A0)),
    Key(DigitalInOut(board.A1)),
    Key(DigitalInOut(board.A2)),
]
```

Default import is `from purple.key import Key`. You can also use `from purple.key_debounce import Key` if you are getting duplicate keypresses.

Keys are specified from left to right and top to bottom. For example, the Sweep's key order looks like this:
```
 0  1  2  3  4
 5  6  7  8  9
10 11 12 13 14
           15 16
```

For split boards, the **left** side is specified this way. The **right** side should be mirrored. The right side for the above Sweep looks like this:
```
   4  3  2  1  0
   9  8  7  6  5
  14 13 12 11 10
16 15
```

### Creating a new Layout

`purple/keyboard/[kb_name]/layout/[layout_name].py`
* `kb_name` - The name of the keyboard.
* `layout_name` - The name of the layout.

A layout defines what happens when a chord is pressed or held. It contains:
* `auto_mod` - A list of modifier keycodes to apply on hold.
* `layers` - A list of layers. Chord resolution starts on the current layer and works its way back to 0 until it finds a layer that can handle the chord.
    * `Layer` - A class containing a dictionary of chords and actions, and the layer color.
        * `chord` - A binary representation of the chord, with `1` being pressed, and `0` released. The bit location corresponds with the key, so for example `0b0001` is key 0 pressed on a 4-key layout, and `0b1100` is keys 2 and 3 on the same.
        * `Action` - Class defining the action to take for a chord. The `Action(tap_action, hold_action=None, hold=False, auto_mod=True)` constructor has the following parameters:
            * `tap_action` - The action to take when the key is tapped.
            * `hold_action` - The action to take when the key is held. `tap_action` is used if `hold_action` is `None`.
            * `hold` - Whether separate hold and release messages should be sent when the key is held down. Used for modifiers like `Shift` or keys you want to repeat.
            * `auto_mod` - Whether Auto Mod should apply to this key when held down.
            * Available actions are:
                * `Press(*keycodes)` - Press the specified keys.
                    * Simple key map: `Action(Press(Keycode.A))`
                    * `z` on tap, `Ctrl+z` on hold: `Action(Press(Keycode.Z), Press(Keycode.CONTROL, Keycode.Z))`
                * `OneShot(*keycodes)` - Add or remove the specified keys to the next normal keypress.
                    * Shift the next key: `Action(OneShot(Keycode.SHIFT))`
                * `Lock(*keycodes)` - Toggle whether the specified keys are locked or unlocked. Locked keys are added automatically to other presses.
                    * Simple key lock: `Action(Lock(Keycode.SHIFT))`
                    * `z` on tap, lock `Ctrl` on hold: `Action(Press(Keycode.Z), Lock(Keycode.CONTROL))`
                * `MediaPress(consumer_control_code)` - Press the specified media key, such a `PLAY_PAUSE` or `MUTE`.
                * `MousePress(mouse_button)` - Press the specified mouse button.
                * `MouseMove(x, y, wheel=0)` - Move the mouse.
                    * Move the mouse to the right: `Action(MouseMove(8, 0))`
                    * Scroll the mouse wheel: `Action(MouseMove(0, 0, 1))`
                * `ToLayer(index)` - Switch to the specified layer.
                    * Simple layer switch: `Action(ToLayer(1))`
                    * `z` on tap, layer switch on hold: `Action(Press(Keycode.Z), ToLayer(0))`
        * `color` - The LED color tuple `(r, g, b)`. Layer colors should be kept dim (no value exceeding 64) so as not to conflict with the modifier indicator.

## Contributing

Pull requests for bug fixes, new keyboards, and new layouts are all welcome!

## Known Issues

None at this time.

## Release Notes

### 0.5.0 [2022-01-08]

* Added
    * `Status` class and extras framework
    * `OneShot` action
    * Optional `Key` debounce
    * `PerformanceCounter` extra
    * [Soar](https://github.com/defiant00/soar) layout
* Updated
    * Renamed `repeat` to `hold` in `Action`
    * Reworked `Key` to match debounced version
    * Split `LED` extra from `Core`
* Removed
    * Placeholder _purple_ layout

### 0.4.0 [2021-12-27]

* Added
    * Media and mouse actions
* Updated
    * Modifier key list now contains both left and right modifier keys
    * Unified modifier key list
    * ARTSEY
        * Added media keys
        * Added mouse controls

### 0.3.0 [2021-12-26]

* Added
    * LED pulsing to indicate locked keys
* Updated
    * Bit order for chords
    * Version numbering

### 0.2.0 [2021-12-23]

* Added
    * Ability to lock and unlock keys
* Updated
    * ARTSEY
        * Added shift lock
        * Added repeat to the backspace and arrow keys

### 0.1.0 [2021-12-21]

* Initial version
