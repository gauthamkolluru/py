WIDTH = 20

STAR = "*"
SPACE = " "
CRLF = "\n"


SP = STAR
RP = SPACE + STAR
EP = CRLF

def pyramid(n):
    return ''.join(aLine(n) for n in range(n))

def aLine(n):
    return leadSpace(n) + startPattern(n) + repeatPattern(n) + endPattern(n)

def leadSpace(n):
    return (WIDTH - n) * SPACE

def startPattern(n):
    return SP

def repeatPattern(n):
    return RP * n

def endPattern(n):
    return EP

print(pyramid(10))