import colorama

'''
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''
switcher = {
    'r':colorama.Fore.RED,
    'bk':colorama.Fore.BLACK,
    'b':colorama.Fore.BLUE,
    'g':colorama.Fore.GREEN,
    'y':colorama.Fore.YELLOW,
    'm':colorama.Fore.MAGENTA,
    'c':colorama.Fore.CYAN,
    'w':colorama.Fore.WHITE
}
def paint(str,color='r'):
    '''Utility func, for printing colorful logs in console...

    @args:
    --
    str : String to be modified.
    color : color code to which the string will be formed. default is 'r'=RED

    @returns:
    --
    str : final modified string with foreground color as per parameters.

    '''
    if color in switcher:
        str = switcher[color]+str+colorama.Style.RESET_ALL
    return str