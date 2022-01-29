from bin import connection
from bin import interface

rate = 9600 # serial port baudrate

# config connection with settings
connection.init(rate, interface)

# wait for response from any com port
connection.wait()

# main loop of the program
while True :
    # read line
    line = connection.read()
    # do chnages if available
    if(line != None) :
        interface.load(line)
    # interface frame update
    interface.update()