import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def __init__(self, t):
        self.t = t

    def printString(self, s, current=None):
        print(self.t, s)
        return s + "*"

    def reverseString(self, s, current=None):
        reversed_s = s[::-1]
        print(self.t, f"reverseString({s!r}) -> {reversed_s!r}")
        return reversed_s

    def countChars(self, s, current=None):
        count = len(s)
        print(self.t, f"countChars({s!r}) -> {count}")
        return count

communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
object1 = PrinterI("Object1 says:")
object2 = PrinterI("Object2 says:")
adapter.add(object1, communicator.stringToIdentity("SimplePrinter1"))
adapter.add(object2, communicator.stringToIdentity("SimplePrinter2"))
adapter.activate()

communicator.waitForShutdown()
