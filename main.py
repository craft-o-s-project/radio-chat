def on_button_pressed_a():
    global index
    music.play(music.tone_playable(262, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    index += -1
    if mode == 0:
        basic.show_string(Alphabet.char_at(index))
    elif mode == 1:
        if index == 0:
            basic.show_leds("""
                . . # . .
                . # # # .
                # . # . #
                . . # . .
                # # # # #
                """)
        elif index == 1:
            basic.show_leds("""
                # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
                """)
        elif index == 2:
            basic.show_leds("""
                # # # . #
                # . . # #
                # . . . .
                # . . . #
                # # # # #
                """)
        elif index == 3:
            basic.show_leds("""
                # # . . .
                # # . . .
                . . # . .
                . . . # .
                . . . . #
                """)
    elif mode == 2:
        basic.show_number(index)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    editChannelSettings()
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def editChannelSettings():
    global mode, index
    mode = 2
    index = channel
    basic.show_number(channel)
def SendMessage():
    global message_to_send
    basic.show_leds("""
        . . . . .
        . . . . #
        . . . # .
        # . # . .
        . # . . .
        """)
    basic.show_leds("""
        # . # . #
        . # . # .
        # . # . #
        . # . # .
        # . # . #
        """)
    radio.send_string(message_to_send)
    message_to_send = ""
    basic.show_string(Alphabet.char_at(index))

def on_button_pressed_ab():
    global mode, index
    basic.clear_screen()
    mode = 1
    index = 0
    if index == 0:
        basic.show_leds("""
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            # # # # #
            """)
    elif index == 1:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
    elif index == 2:
        basic.show_leds("""
            # # # . #
            # . . # #
            # . . . .
            # . . . #
            # # # # #
            """)
    elif index == 3:
        basic.show_leds("""
            # # . . .
            # # . . .
            . . # . .
            . . . # .
            . . . . #
            """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.clear_screen()
    music.play(music.string_playable("C5 B A G F E D C ", 1500),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C5 B A G F E D C ", 1500),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C5 B A G F E D C ", 1500),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_string(receivedString)
    basic.pause(1000)
    basic.show_string(Alphabet.char_at(index))
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global index
    music.play(music.tone_playable(262, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    index += 1
    if mode == 0:
        basic.show_string(Alphabet.char_at(index))
    elif mode == 1:
        if index == 0:
            basic.show_leds("""
                . . # . .
                . # # # .
                # . # . #
                . . # . .
                # # # # #
                """)
        elif index == 1:
            basic.show_leds("""
                # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
                """)
        elif index == 2:
            basic.show_leds("""
                # # # . #
                # . . # #
                # . . . .
                # . . . #
                # # # # #
                """)
        elif index == 3:
            basic.show_leds("""
                # # . . .
                # # . . .
                . . # . .
                . . . # .
                . . . . #
                """)
    elif mode == 2:
        basic.show_number(index)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global message_to_send, mode, index, channel
    music.play(music.tone_playable(262, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    if mode == 0:
        message_to_send = "" + message_to_send + Alphabet.char_at(index)
    elif mode == 1:
        basic.clear_screen()
        if index == 0:
            basic.clear_screen()
            SendMessage()
            mode = 0
            index = 0
            basic.show_string(Alphabet.char_at(index))
        elif index == 1:
            basic.clear_screen()
            mode = 0
            index = 0
            basic.show_string(Alphabet.char_at(index))
        elif index == 2:
            message_to_send = ""
            mode = 0
            basic.clear_screen()
            basic.show_icon(IconNames.YES)
            basic.show_icon(IconNames.CHESSBOARD)
            index = 0
            basic.show_string(Alphabet.char_at(index))
        elif index == 3:
            basic.clear_screen()
            basic.show_string(message_to_send)
            basic.show_leds("""
                # # . . .
                # # . . .
                . . # . .
                . . . # .
                . . . . #
                """)
    elif mode == 2:
        radio.set_group(index)
        channel = index
        basic.show_icon(IconNames.YES)
        basic.show_icon(IconNames.CHESSBOARD)
        mode = 0
        index = 0
        basic.show_string(Alphabet.char_at(index))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

mode = 0
index = 0
Alphabet = ""
message_to_send = ""
channel = 0
serial.redirect_to_usb()
channel = 1
radio.set_group(channel)
message_to_send = ""
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-"
index = 0
music.set_volume(255)
basic.show_string(Alphabet.char_at(index))

def on_forever():
    global index
    if mode == 0:
        if index == -1:
            index = 26
            basic.show_string(Alphabet.char_at(index))
        elif index == 27:
            index = 0
            basic.show_string(Alphabet.char_at(index))
    elif mode == 1:
        if index == -1:
            index = 3
            basic.show_leds("""
                # # . . .
                # # . . .
                . . # . .
                . . . # .
                . . . . #
                """)
        elif index == 4:
            index = 0
            basic.show_leds("""
                . . # . .
                . # # # .
                # . # . #
                . . # . .
                # # # # #
                """)
basic.forever(on_forever)
