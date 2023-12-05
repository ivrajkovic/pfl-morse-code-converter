MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


# Morse code converter
def to_morse_code(message):
    morse_code_message = ""
    success = True
    for letter in message:
        try:
            if letter != ' ':
                morse_code_message += MORSE_CODE_DICT[letter] + ' '
            else:
                morse_code_message += ' '
        except KeyError:
            return "Wrong symbol detected. Use only letters, numbers, and following symbols: (),.?/-"
    return morse_code_message


# Get user input
user_input = input('Enter message: ').upper()

# Run Morse code converter
print(to_morse_code(user_input))


