#!/usr/bin/env python3

import argparse
import serial
import time

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="ph"
    )
    parser.add_argument("--port", "-p", required=True, help="Serial port, e.g. COM1, /dev/ttyS1, /dev/ttyUSB1.")
    parser.add_argument("--timeout", "-t", required=False, help="Time to wait in seconds for reads/writes or for device to assert RTS.", type=int, default=3)
    parser.add_argument("--file", "-f", required=False, metavar="FILE", help="Path to file to send to device.")
    parser.add_argument("--dump", "-d", required=False, help="Wait for CTS and dump received serial data to binary file.", action='store_true')
    parser.add_argument("--output", "-o", required=False, help="Desired name of output dump file.", default="dump.bin")
    parser.add_argument("--length", "-l", required=False, help="Maximum amount of bytes to dump.", type=int, default=512)

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
        buffer = [args.length]
        buffer = ser.read(args.length)
        with open(args.output, 'wb') as fh:
            fh.write(buffer)
            print("Wrote " + str(len(buffer)) + " bytes to " + args.output + ".")
        ser.close()

# Open serial port specified by argument
def openPort():
    global ser
    try:
        ser = serial.Serial(args.port, 115200, rtscts=True, timeout=args.timeout, write_timeout=args.timeout)

        # Wait for ZF to assert RTS, exit if timeout
        t = args.timeout
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
