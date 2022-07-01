morse = {'a': '.-',
         'b': '-...',
         'c': '-.-.',
         'd': '-..',
         'e': '.',
         'f': '..-.',
         'g': '--.',
         'h': '....',
         'i': '..',
         'j': '.---',
         'k': '-.-',
         'l': '.-..',
         'm': '--',
         'n': '-.',
         'o': '---',
         'p': '.--.',
         'q': '--.-',
         'r': '.-.',
         's': '...',
         't': '-',
         'u': '..-',
         'v': '...-',
         'w': '.--',
         'x': '-..-',
         'y': '-.--',
         'z': '--..',
         ' ': '/'}


def text_to_morse(message):
    message = str(message).lower()
    message_list = []
    ind = 0
    for i in range(len(message)):
        message_list.append(morse.get(message[ind]))
        ind = ind + 1
    new_message = ' '.join(message_list)
    return new_message


print(text_to_morse(input()))
