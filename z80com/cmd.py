#!/usr/bin/env python3

import argparse
import serial
import time

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="ph"
    )
    parser.add_argument("--file", "-f", required=True, metavar="FILE", help="ph")
    parser.add_argument("--port", "-p", required=True, help="ph")

    args = parser.parse_args(argv)

    try:
        ser = serial.Serial(args.port, 115200, rtscts=True, write_timeout=1)
    except:
        print("Could not open " + args.port + ".")
        exit()

    with open(args.file, 'rb') as fh:
        ser.write(fh.read())

    time.sleep(0.25)
    ser.close()
    exit()

if __name__ == "__main__":
    main()
