#!/usr/bin/env python3

import argparse
import serial
import time

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="ph"
    )
    parser.add_argument("--port", "-p", required=True, help="ph")
    parser.add_argument("--file", "-f", required=False, metavar="FILE", help="ph")
    parser.add_argument("--dump", "-d", required=False, help="ph", action='store_true')
    parser.add_argument("--output", "-o", required=False, help="ph", default="dump.bin")

    global args
    args = parser.parse_args(argv)

    # Open port and transfer contents of file
    if args.file != None:
        openPort()
        with open(args.file, 'rb') as fh:
            try:
                ser.write(fh.read())
                # Allow serial device time to finish writing!
                time.sleep(1)
                print("Transfer complete.")
            except:
                print("Transfer failed.")
        ser.close()

    # Open port and dump received data to file
    if args.dump == True:
        openPort()
        buffer = []
        buffer = ser.read(65536)
        with open(args.output, 'wb') as fh:
            fh.write(buffer)
            print("Wrote " + str(len(buffer)) + " bytes to " + args.output + ".")
        ser.close()

# Open serial port specified by argument
def openPort():
    global ser
    try:
        ser = serial.Serial(args.port, 115200, rtscts=True, timeout=1, write_timeout=1)

        # Wait for ZF to assert RTS, exit if timeout
        t = 3
        while (ser.cts != True):
            time.sleep(1)
            t -= 1
            if (t <= 0):
                print("Request timed out. Device did not assert RTS.")
                exit()

    except serial.SerialException:
        print("Could not open " + args.port + ".")
        exit()

if __name__ == "__main__":
    main()
