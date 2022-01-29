import serial.tools.list_ports

rate = None
root = None
port = None

def init(irate, iroot) :
    global rate, root
    # store port data in global scope
    root = iroot
    rate = irate

def wait() :
    global rate, port, root
    # wait for a response from any com port
    while port == None :
        # check for available port if an arduino board is connected
        for name in serial.tools.list_ports.comports() :
            try :
                # check port name
                if(str(name).split(' ')[2] == 'Arduino') :
                    # create port object
                    number = str(name).split(' ')[0]
                    srport = serial.Serial(port = number, baudrate = rate)
                    port = srport
                    # clear previous console lines
                    root.clear()
                    # print found board on console
                    root.load('Found @ ' + str(name), True)
                    # stop when port is found
                    break
            except :
                # continue if any error
                continue
        root.update()

def read() :
    global port, root
    data = None
    try :
        if port.isOpen() :
            if port.in_waiting :
                # read line and strip string 
                data = port.readline().decode().rstrip().lstrip()
        else :
            # wait again if port went offline
            root.load('Communication Ended', True)
            wait()
    except :
        # wait again if any error
        root.load('Communication Ended', True)
        port = None
        wait()
    return data

def send(data) :
    global port, root
    try :
        if port.isOpen() :
            port.write(str.encode(data))
            root.load(' >>> ' + data)
        else :
            # wait again if port went offline
            root.load('Communication Ended', True)
            wait()
    except :
        # wait again if any error
        root.load('Communication Ended', True)
        port = None
        wait()