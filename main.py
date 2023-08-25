import time

BRIGHTNESS_PATH = "/sys/class/leds/tpacpi::lid_logo_dot/brightness"

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '
}

def encode_to_morse(message):
    encoded_message = ''
    for char in message.upper():
        if char in morse_code_dict:
            encoded_message += morse_code_dict[char] + ' '
        else:
            print("Unsupported char...")
            quit()
    return encoded_message

def turn_led_on():
    with open(BRIGHTNESS_PATH, "w") as brightness_file:
        brightness_file.write("1")

def turn_led_off():
    with open(BRIGHTNESS_PATH, "w") as brightness_file:
        brightness_file.write("0")

def turn_led_on_for(seconds):
    turn_led_on()
    time.sleep(seconds)
    turn_led_off()

def run(usr_string):
    morse = encode_to_morse(usr_string)
    for c in morse:
        if c == ".":
            turn_led_on_for(0.3)

        if c == "-":
            turn_led_on_for(0.9)

        if c == " ":
            time.sleep(2)

        time.sleep(0.3)

if __name__ == "__main__":
    usr_string = input("Enter text: ")
    run(usr_string)