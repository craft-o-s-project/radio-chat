input.onButtonPressed(Button.A, function () {
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    index += -1
    if (mode == 0) {
        basic.showString(Alphabet.charAt(index))
    } else if (mode == 1) {
        if (index == 0) {
            basic.showLeds(`
                . . # . .
                . # # # .
                # . # . #
                . . # . .
                # # # # #
                `)
        } else if (index == 1) {
            basic.showLeds(`
                # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
                `)
        } else if (index == 2) {
            basic.showLeds(`
                # # # . #
                # . . # #
                # . . . .
                # . . . #
                # # # # #
                `)
        } else if (index == 3) {
            basic.showLeds(`
                # # . . .
                # # . . .
                . . # . .
                . . . # .
                . . . . #
                `)
        }
    } else if (mode == 2) {
        basic.showNumber(index)
    }
})
input.onGesture(Gesture.TiltLeft, function () {
    editChannelSettings()
})
function editChannelSettings () {
    mode = 2
    index = channel
    basic.showNumber(channel)
}
function SendMessage () {
    basic.showLeds(`
        . . . . .
        . . . . #
        . . . # .
        # . # . .
        . # . . .
        `)
    basic.showLeds(`
        # . # . #
        . # . # .
        # . # . #
        . # . # .
        # . # . #
        `)
    radio.sendString(message_to_send)
    message_to_send = ""
    basic.showString(Alphabet.charAt(index))
}
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
    mode = 1
    index = 0
    if (index == 0) {
        basic.showLeds(`
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            # # # # #
            `)
    } else if (index == 1) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    } else if (index == 2) {
        basic.showLeds(`
            # # # . #
            # . . # #
            # . . . .
            # . . . #
            # # # # #
            `)
    } else if (index == 3) {
        basic.showLeds(`
            # # . . .
            # # . . .
            . . # . .
            . . . # .
            . . . . #
            `)
    }
})
radio.onReceivedString(function (receivedString) {
    basic.clearScreen()
    music.play(music.stringPlayable("C5 B A G F E D C ", 1500), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("C5 B A G F E D C ", 1500), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("C5 B A G F E D C ", 1500), music.PlaybackMode.UntilDone)
    basic.showString(receivedString)
    basic.pause(1000)
    basic.showString(Alphabet.charAt(index))
})
input.onButtonPressed(Button.B, function () {
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    index += 1
    if (mode == 0) {
        basic.showString(Alphabet.charAt(index))
    } else if (mode == 1) {
        if (index == 0) {
            basic.showLeds(`
                . . # . .
                . # # # .
                # . # . #
                . . # . .
                # # # # #
                `)
        } else if (index == 1) {
            basic.showLeds(`
                # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
                `)
        } else if (index == 2) {
            basic.showLeds(`
                # # # . #
                # . . # #
                # . . . .
                # . . . #
                # # # # #
                `)
        } else if (index == 3) {
            basic.showLeds(`
                # # . . .
                # # . . .
                . . # . .
                . . . # .
                . . . . #
                `)
        }
    } else if (mode == 2) {
        basic.showNumber(index)
    }
})
input.onGesture(Gesture.Shake, function () {
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    if (mode == 0) {
        message_to_send = "" + message_to_send + Alphabet.charAt(index)
    } else if (mode == 1) {
        basic.clearScreen()
        if (index == 0) {
            basic.clearScreen()
            SendMessage()
            mode = 0
            index = 0
            basic.showString(Alphabet.charAt(index))
        } else if (index == 1) {
            basic.clearScreen()
            mode = 0
            index = 0
            basic.showString(Alphabet.charAt(index))
        } else if (index == 2) {
            message_to_send = ""
            mode = 0
            basic.clearScreen()
            basic.showIcon(IconNames.Yes)
            basic.showIcon(IconNames.Chessboard)
            index = 0
            basic.showString(Alphabet.charAt(index))
        } else if (index == 3) {
            basic.clearScreen()
            basic.showString(message_to_send)
            basic.showLeds(`
                # # . . .
                # # . . .
                . . # . .
                . . . # .
                . . . . #
                `)
        }
    } else if (mode == 2) {
        radio.setGroup(index)
        channel = index
        basic.showIcon(IconNames.Yes)
        basic.showIcon(IconNames.Chessboard)
        mode = 0
        index = 0
        basic.showString(Alphabet.charAt(index))
    }
})
let mode = 0
let index = 0
let Alphabet = ""
let message_to_send = ""
let channel = 0
serial.redirectToUSB()
channel = 1
radio.setGroup(channel)
message_to_send = ""
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-"
index = 0
music.setVolume(255)
basic.showString(Alphabet.charAt(index))
basic.forever(function () {
    if (mode == 0) {
        if (index == -1) {
            index = 26
            basic.showString(Alphabet.charAt(index))
        } else if (index == 27) {
            index = 0
            basic.showString(Alphabet.charAt(index))
        }
    } else if (mode == 1) {
        if (index == -1) {
            index = 3
            basic.showLeds(`
                # # . . .
                # # . . .
                . . # . .
                . . . # .
                . . . . #
                `)
        } else if (index == 4) {
            index = 0
            basic.showLeds(`
                . . # . .
                . # # # .
                # . # . #
                . . # . .
                # # # # #
                `)
        }
    }
})
