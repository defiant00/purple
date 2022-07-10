import board

# Handles the display on the adafruit macropad
class AdaMacroDisplay:

    # For correct display rotation with left hand 
    # artsey layout, add AdaMacroDisplay(270) as an extra
    def __init__(self, rotation):
        display = board.DISPLAY
        display.rotation=rotation
    
    def update(self, status):
        return