# ANSI escape codes

# style / text color / background color

# style:
'''
0 - none
1 - bold
4 - underline
7 - negative
'''

# text color:
'''
30 - white
31 - red
32 - green
33 - yellow
34 - blue
35 - purple
36 - cyan
37 - gray
'''

# background color:
'''
30 - white
31 - red
32 - green
33 - yellow
34 - blue
35 - purple
36 - cyan
37 - gray
'''

# Exemple: of bold yellow text on blue background
RED_WHITE = '\033[0:30:41m'

print(f'{RED_WHITE}This text is red on white background.{RED_WHITE}')
