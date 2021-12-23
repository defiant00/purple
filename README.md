# purple

[CircuitPython](https://circuitpython.org/) firmware for one-handed chording keyboards based on the [KB2040](https://learn.adafruit.com/adafruit-kb2040) from [adafruit](https://www.adafruit.com/)!

## Features

* Layers!
* Map chords to key combinations on tap or hold.
* One-shot modifiers.
* Auto Mod for if you want to apply a modifier globally on hold.
* LED layer and modifier state indicators.
    * Layers can specify a color.
    * When modifiers are active, the LED blinks a color for each in turn:
        * Yellow - Shift
        * Red - Control
        * Blue - Alt
        * Pink - GUI
    * Rapid blinking indicates a key is locked.

## Usage

1. Follow the quickstart [here](https://learn.adafruit.com/adafruit-kb2040/circuitpython) to set up your board with CircuitPython.
2. Copy required libraries to your `CIRCUITPY/lib` folder:
    1. `adafruit_hid` (whole folder)
    2. `adafruit_pixelbuf.mpy`
    3. `neopixel.mpy`
3. Edit `code.py` imports to import the keyboard and layout you want to use.
4. Copy `code.py` and the `purple` folder to your `CIRCUITPY` drive. _(if you need to save space, you can copy only your selected keyboard and layout scripts under `purple/keyboard`)_

## Development

### General Customization

`core.py` contains some useful values that can be adjusted:
* `_HOLD_DELAY` - How long to wait in ms before a key is considered held.
* `_MODIFIER_BLINK` - How long to wait between modifier blinks.
* `_MODIFIER_BLINK_ON` - How long to turn on the LED per modifier blink.
* `_MOD_COLORS` - The LED color tuple `(r, g, b)` to use for the modifier. Should be a bright value so it can be seen when on layers.
* `_LOCK_BLINK` - How long to wait between locked key blinks.
* `_LOCK_BLINK_ON` - How long to turn on the LED per locked key blink.
* `_LOCK_COLOR` - The LED color tuple `(r, g, b)` to use when a key is locked.

### Creating a new Keyboard

`purple/keyboard/[kb_name]/[board].py`
* `kb_name` - The name of the keyboard.
* `board` - `keyboard` for a single board. `left` or `right` if it's a split board.

A keyboard defines a list of `purple.key.Key` objects specifying the board pins, eg:
```python
keys = [
    Key(DigitalInOut(board.A0)),
    Key(DigitalInOut(board.A1)),
    Key(DigitalInOut(board.A2)),
]
```

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
        * `chord` - A binary representation of the chord, with `1` being pressed, and `0` released. Digits read left to right correspond with keys 0 to max, so for example `0b1000` is key 0 pressed on a 4-key layout, and `0b0011` is keys 2 and 3 on the same.
        * `Action` - Class defining the action to take for a chord. The `Action(tap, hold=None, repeat=False, auto_mod=True)` constructor has the following parameters:
            * `tap` - The action to take when the key is tapped.
            * `hold` - The action to take when the key is held. The `tap` action is used if `hold` is `None`.
            * `repeat` - Whether the key should repeat when held down.
            * `auto_mod` - Whether Auto Mod should apply to this key when held down.
            * Available actions are:
                * `Press(*keycodes)` - Press the specified keys.
                    * Simple key map: `Action(Press(Keycode.A))`
                    * `z` on tap, `Ctrl+z` on hold: `Action(Press(Keycode.Z), Press(Keycode.CONTROL, Keycode.Z))`
                * `Lock(*keycodes)` - Toggle whether the specified keys are locked or unlocked. Locked keys are added automatically to other presses.
                    * Simple key lock: `Action(Lock(Keycode.SHIFT))`
                    * `z` on tap, lock `Ctrl` on hold: `Action(Press(Keycode.Z), Lock(Keycode.CONTROL))`
                * `ToLayer(index)` - Switch to the specified layer.
                    * Simple layer switch: `Action(ToLayer(1))`
                    * `z` on tap, layer switch on hold: `Action(Press(Keycode.Z), ToLayer(0))`
        * `color` - The LED color tuple `(r, g, b)`. Layer colors should be kept dim (no value exceeding 64) so as not to conflict with the modifier indicator.

## Contributing

Pull requests for bug fixes, new keyboards, and new layouts are all welcome!

## Known Issues

None at this time.

## Release Notes

### 1.1.0 [2021-12-23]

* Added
    * Ability to lock and unlock keys
* Updated
    * ARTSEY
        * Added shift lock
        * Added repeat to the backspace and arrow keys

### 1.0.0 [2021-12-21]

* Initial version
