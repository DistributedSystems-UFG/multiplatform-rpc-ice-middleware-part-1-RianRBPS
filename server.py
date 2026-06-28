import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)
        return s + "*"

    def reverseString(self, s, current=None):
        reversed_s = s[::-1]
        print(f"reverseString({s!r}) -> {reversed_s!r}")
        return reversed_s

    def countChars(self, s, current=None):
        count = len(s)
        print(f"countChars({s!r}) -> {count}")
        return count

communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
object = PrinterI()
adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
adapter.activate()

communicator.waitForShutdown()
