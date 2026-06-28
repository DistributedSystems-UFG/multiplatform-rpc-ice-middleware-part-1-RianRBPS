import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base1 = communicator.stringToProxy("SimplePrinter1:tcp -h 98.90.53.6 -p 11000")
base2 = communicator.stringToProxy("SimplePrinter2:tcp -h 98.90.53.6 -p 11000")
printer1 = Demo.PrinterPrx.checkedCast(base1)
printer2 = Demo.PrinterPrx.checkedCast(base2)
if (not printer1) or (not printer2):
    raise RuntimeError("Invalid proxy")

rep = printer1.printString("Hello World from printer1!")
print(rep)
rep = printer2.printString("Hello World from printer2!")
print(rep)

rev1 = printer1.reverseString("Hello World from printer1!")
print(f"Reversed by printer1: {rev1}")
rev2 = printer2.reverseString("Hello World from printer2!")
print(f"Reversed by printer2: {rev2}")

count1 = printer1.countChars("Hello World from printer1!")
print(f"Char count from printer1: {count1}")
count2 = printer2.countChars("Hello World from printer2!")
print(f"Char count from printer2: {count2}")

communicator.waitForShutdown()
