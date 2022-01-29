import tkinter
from tkinter import *
from bin import connection

# create root window
root = Tk()
# set window size
root.geometry("650x513")
# set window to fixed mode
root.resizable = False
# set window icon
root.iconbitmap("bin/icon.ico")
# set window title
root.title('arduino-py-client')

# create console text label
cons = Label(
    root,
    text = '',
    bg = '#222',
    foreground = '#999',
    font = "Consolas 8",
    anchor = tkinter.NW,
    height = 30,
    padx = 10,
    pady = 10,
    justify = tkinter.LEFT
)
# attach console text label to root
cons.pack(fill = tkinter.BOTH, side = tkinter.TOP)

# create inputbox
text = Entry(
    root,
    bg = '#333',
    foreground = '#999',
    font = "Consolas 10",
    highlightthickness=10,
    highlightcolor='#333',
    highlightbackground='#333',
    borderwidth=0,
    insertbackground='#999',
    selectbackground='#666'
)
# bind inputbox event
text.bind('<Return>', (lambda _: send()))
# attach inputbox to root
text.pack(fill = tkinter.BOTH, side = tkinter.TOP)
# focus on inputbox
text.focus()

def send() :
    global text
    if(text.get() == '') :
        # ignore empty messages
        return
    else :
        # send message
        connection.send(text.get())
        # clear inputbox text
        text.delete(0, 'end')

def update() :
    global root
    try :
        # update gui
        root.update()
    except :
        # exit if gui is destroyed
        exit()

def load(line, sprt = False) :
    # add separator string if sprt is true
    if(sprt) :
        line = ' ' + line + ' '
        size = 50 - len(line)
        for n in range(0, size) :
            if(n < size / 2) :
                line = line + '='
            else :
                line = '=' + line
    global cons
    # create cons line array and append
    arry = cons.cget('text').split('\n')
    # remove empty line
    if(arry[0] == '') : arry.remove('')
    arry.append(line)
    # slice for last five lines
    leng = len(arry)
    #max lines count on console
    maxl = 30
    if(leng > maxl) :
        # splice array
        arry = arry[leng - maxl :]
    # generate cons text
    leng = len(arry)
    text = ''
    for i in range(0, leng) :
        text += arry[i].rstrip().lstrip()
        if(i < leng - 1) : text += '\n'
    # update cons
    cons.config(text = text)

def clear() :
    global cons
    # clear console lines
    cons.config(text = '')