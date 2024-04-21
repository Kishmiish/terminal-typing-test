import curses
import curses.ascii
import time
import stringGen
import math

stdscr = curses.initscr()
stcolor = curses.start_color()

curses.noecho()
curses.cbreak()
stdscr.keypad(True)

curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_BLACK)

stdscr.addstr("WPM: -\n")

testString = stringGen.stringGenerator(40)

stdscr.addstr(testString)
i = 0
stdscr.move(1,0)
global words;
words = 0
correctLetters = 0
wrongLetter = 0
startTime = 0

while i < testString.__len__():
    
    ch = stdscr.getch()

    if(i == 0):
        startTime = time.time()


    if ch == curses.ascii.SP and ord(testString[i]) == curses.ascii.SP:
        correctLetters += 1
        y, x = stdscr.getyx()
        wpm = int((correctLetters * 12) / math.ceil(time.time() - startTime))
        #stdscr.move(0,5)
        stdscr.addstr(0,5,str(wpm))
        stdscr.move(y,x)
        stdscr.addch(testString[i],curses.color_pair(1))
        words += 1
        i += 1
    elif ch == ord(testString[i]):
        stdscr.addch(ch)
        correctLetters += 1
        i += 1
        stdscr.refresh()
    elif ch == curses.KEY_BACKSPACE:
        y, x = stdscr.getyx()
        stdscr.addch(y,x-1,testString[i-1])
        i -= 1
        stdscr.move(y,x-1)
    else:
        stdscr.addch(testString[i],curses.color_pair(1))
        wrongLetter += 1
        i += 1

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
