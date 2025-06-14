import tkinter as tk
import time
import winsound

# Timing constants
DOT_DURATION = 100
DASH_DURATION = DOT_DURATION * 3
FREQ = 800

SYMBOL_GAP = DOT_DURATION / 1000
LETTER_GAP = (DOT_DURATION * 3) / 1000
WORD_GAP = (DOT_DURATION * 7) / 1000


# Morse code dictionary
morse_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----'
}

# Using tkinter to create a morse code chart
def create_cheatsheet():
    root = tk.Tk()
    root.title("Morse Code Chart")

    # Container frame
    container = tk.Frame(root)
    container.pack(fill=tk.BOTH, expand=True)

    # Canvas and scrollbar
    canvas = tk.Canvas(container, width=600, height=600, bg="white")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Frame inside canvas
    scrollable_frame = tk.Frame(canvas, bg="white")
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Add Morse chart rows
    for i, char in enumerate(morse_dict):
        row = tk.Frame(scrollable_frame, bg="white")
        row.pack(fill=tk.X, pady=2, padx=10)

        label = tk.Label(row, text=char, width=3, bg="yellow", font=("Arial", 12))
        label.pack(side=tk.LEFT)

        for symbol in morse_dict[char]:
            if symbol == '.':
                dot = tk.Label(row, text="●", font=("Arial", 14), fg="black", width=2)
                dot.pack(side=tk.LEFT, padx=2)
            elif symbol == '-':
                dash = tk.Label(row, text="▬", font=("Arial", 14), fg="black", width=2)
                dash.pack(side=tk.LEFT, padx=2)

    # Set scroll region
    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    root.mainloop()

# Get a choice from user
def get_decision():
    print("Morse code uses 3 spaces as space between letters and 7 spaces for space between words")
    print("Please select one of the following :- \n" \
    "1. Press 1 to convert English to Morse code \n" \
    "2. Press 2 to convert Morse code to English \n" \
    "3. Press 3 to stop")

    while(True):

        choice = input("")

        if choice == "1":
            ask_sentence_english()
        elif choice == "2":
            ask_sentence_morse()
        elif choice == "3":
            print("Thank you for trying the converter :D")
            break
        else:
            print("You can only select 1, 2 or 3")

        print('')
        print("Please make another choice")

# Converts English to Morse code
def ask_sentence_english():
    converted_text = ""
    sentence = input('Enter sentence to convert to Morse code: ')
    for i, letter in enumerate(sentence.upper()):
        if letter in morse_dict:
            converted_text += morse_dict[letter] + '   '  # 3 spaces between letters
        elif letter == ' ':
            converted_text += '       '  # 7 spaces between words

    print("Morse Code:", converted_text.strip())
    play_morse(converted_text.strip())

# Converts Morse code to English
def ask_sentence_morse():
    morse_code = input('Please enter a sentence or word that you want to convert to English: ')

    # Reverse the morse_dict to get morse -> letter mapping
    reverse_dict = {value: key for key, value in morse_dict.items()}

    # Split the input Morse code into words by 7 spaces (word gap)
    words = morse_code.split('       ')  # 7 spaces between words
    decoded_sentence = ""

    for word in words:
        # Split each word into letters by 3 spaces (letter gap)
        letters = word.split('   ')  # 3 spaces between letters
        for letter in letters:
            decoded_sentence += reverse_dict.get(letter, '?')  # Use '?' for unknown symbols
        
        decoded_sentence += ' '  # Add space between decoded words

    print(decoded_sentence.strip())  # Print final decoded sentence


# Using winsound library to hear thhe Morse code
def play_morse(morse_code):
    i = 0
    while i < len(morse_code):
        symbol = morse_code[i]
        if symbol == '.':
            winsound.Beep(FREQ, DOT_DURATION)
            time.sleep(SYMBOL_GAP)
        elif symbol == '-':
            winsound.Beep(FREQ, DASH_DURATION)
            time.sleep(SYMBOL_GAP)
        elif symbol == ' ':
            # Count how many consecutive spaces
            space_count = 1
            while i + 1 < len(morse_code) and morse_code[i + 1] == ' ':
                space_count += 1
                i += 1
            # Apply proper delay based on space_count
            if space_count == 3:
                time.sleep(LETTER_GAP)  # 3 dots between letters
            elif space_count == 7:
                time.sleep(WORD_GAP)    # 7 dots between words
        i += 1


if __name__ == '__main__':
    create_cheatsheet()
    get_decision()
