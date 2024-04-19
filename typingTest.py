import curses
import curses.ascii
import time
import stringGen

stdscr = curses.initscr()
stcolor = curses.start_color()

curses.noecho()
curses.cbreak()
stdscr.keypad(True)

curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_BLACK)

str = stringGen.stringGenerator(30)

stdscr.addstr(str)
i = 0
stdscr.move(0,0)

while i < str.__len__():
    ch = stdscr.getch()
    if ch == ord(str[i]):
        stdscr.addch(0,i,ch)
        i += 1
        stdscr.refresh()
    elif ch == curses.KEY_BACKSPACE:
        stdscr.addch(0,i-1,str[i-1])
        i -= 1
        stdscr.move(0,i)
    elif ch == curses.ascii.SP:
        stdscr.addch(0,i,str[i],curses.color_pair(1))
        i += 1
    else:
        stdscr.addch(0,i,ch,curses.color_pair(1))
        i += 1

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
