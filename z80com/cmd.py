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
        ser = serial.Serial(args.port, 115200, rtscts=True, timeout=5, write_timeout=5)
    except:
        print("Could not open " + args.port + ".")
        end()

    with open(args.file, 'rb') as fh:
        try:
            ser.write(fh.read())
        except:
            print("Transfer failed.")
            end()
        print("Transfer complete.")
        end()

def end():
    time.sleep(0.25)
    try:
        ser.close()
    except:
        pass
    exit()

if __name__ == "__main__":
    main()
