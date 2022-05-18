from pynput.keyboard import Listener, Key


def handleRelease(key):
    print('Released: {}'.format(key))

    if key == Key.f1:
        TX = '$L#1#ON#100'
        RX = '$L#1#ON#100#OK'
        return False
    elif key == Key.f2:
        TX = '$L#2#ON#100'
        RX = '$L#2#ON#100#OK'
        return False


with Listener(on_release=handleRelease) as listener:
    listener.join()