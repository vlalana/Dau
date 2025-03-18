nombre = 0

def on_gesture_shake():
    global nombre
    basic.clear_screen()
    nombre = randint(0, 6)
    if nombre == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    if nombre == 2:
        basic.show_leds("""
            . . . . .
            . . . . .
            . # . # .
            . . . . .
            . . . . .
            """)
    if nombre == 3:
        basic.show_leds("""
            . . . . .
            . # . . .
            . . # . .
            . . . # .
            . . . . .
            """)
    if nombre == 4:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            """)
    if nombre == 5:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . # . .
            . # . # .
            . . . . .
            """)
    if nombre == 6:
        basic.show_leds("""
            . . . . .
            . # . # .
            . # . # .
            . # . # .
            . . . . .
            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
