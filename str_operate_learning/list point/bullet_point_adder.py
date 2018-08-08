#! python3
# bullet_point_adder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip

text = pyperclip.paste()

# Separate lines and add starts.
lines = text.split('\n')
# loop through all indexes in the "lines" list
for i in range(len(lines)):
    # add star to each string in "lines" list
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)
