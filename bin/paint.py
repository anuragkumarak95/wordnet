from colorama import Fore, Style

'''
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''
switcher = {
    'r':Fore.RED,
    'bk':Fore.BLACK,
    'b':Fore.BLUE,
    'g':Fore.GREEN,
    'y':Fore.YELLOW,
    'm':Fore.MAGENTA,
    'c':Fore.CYAN,
    'w':Fore.WHITE
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
        str = switcher[color]+str+Style.RESET_ALL
    return str