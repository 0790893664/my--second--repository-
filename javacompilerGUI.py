import tkinter as tk
from tkinter import filedialog

HEIGHT = 500
WIDTH = 600
BLUE = '#80c1ff'
SMALL_FONT = ('Arial', 10)
LARGE_FONT = ('Arial', 20, 'bold')


def check_nesting(program):
    """
    Checks nesting of a java program
    input:
    program(str): Java program
    returns: None
    """
    programSymbols = []
    symbols = ['{', '}', '(', ')', '[', ']']
    symbolTuples = [('{', '}'), ('(', ')'), ('[', ']'), ('<', '>')]
    for letter in program:
        if letter in symbols:
            programSymbols.append(letter)
        elif letter == '<' and programSymbols[-1] != '(':
            programSymbols.append(letter)
        elif letter == '>' and programSymbols[-1] == '<':
            programSymbols.append(letter)
        elif letter == '>' and programSymbols[-1] != '<':
            lower_frame_label['text'] = 'Wrong Syntax'
            return
    for symbolTuple in symbolTuples:
        if programSymbols.count(symbolTuple[0]) != programSymbols.count(symbolTuple[1]):
            lower_frame_label['text'] = f"""Missing: {symbolTuple[0] if
            programSymbols.count(symbolTuple[0]) < programSymbols.count(symbolTuple[1]) else symbolTuple[1]}"""
            break
    else:
        lower_frame_label['text'] = 'Correct Nesting'


def browse_files():
    """
    Implements file browsing functionality
    returns: None
    """
    try:
        filename = filedialog.askopenfilename(initialdir='/', title='Select a file',
                                              filetypes=(('Text files', '*.txt'), ('all files', '*.*')))
        upper_frame_label['text'] = f'Opened {filename}'
        lower_frame_label['text'] = ''
    except FileNotFoundError:
        lower_frame_label['text'] = 'NO FILE SELECTED!!!'

    java_program = ''
    lines = []
    try:
        file = open(filename)
        for line in file.readlines():
            lines.append(line.strip())
        java_program = java_program.join(lines)
    except FileNotFoundError:
        lower_frame_label['text'] = 'NO FILE SELECTED!!!'
    finally:
        file.close()

    check_nesting(java_program)


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

back_image = tk.PhotoImage(file='background.jpg')
back_label = tk.Label(root, image=back_image)
back_label.place(relheight=1, relwidth=1)

upper_frame = tk.Frame(root, bg=BLUE, bd=5)
upper_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

upper_frame_label = tk.Label(upper_frame, font=SMALL_FONT)
upper_frame_label.place(relwidth=0.70, relheight=1)

browse_file_button = tk.Button(upper_frame, text='Open File', font=SMALL_FONT, command=browse_files)
browse_file_button.place(relx=0.72, relwidth=0.28, relheight=1)

lower_frame = tk.Frame(root, bg=BLUE, bd=10)
lower_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)

lower_frame_label = tk.Label(lower_frame, font=LARGE_FONT)
lower_frame_label.place(relwidth=1, relheight=1)

root.mainloop()
