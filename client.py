import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base = communicator.stringToProxy("SimplePrinter:tcp -h 98.90.53.6 -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

printer.printString("Hello World!")

reversed_s = printer.reverseString("Hello World!")
print(f"Reversed: {reversed_s}")

count = printer.countChars("Hello World!")
print(f"Character count: {count}")
