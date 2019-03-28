from ptrace.linux_proc import searchProcessByName
from ptrace.debugger import PtraceDebugger
from ptrace.debugger.process import PtraceProcess
from struct import unpack
from signal import SIGCONT, SIGSTOP


class Process:
    def __init__(self):
        self.pid = searchProcessByName('wow.exe')
        self.name = ""
        print("Attach the running process %s" % self.pid)
        self.__tracer = PtraceProcess(PtraceDebugger(), self.pid, False)

    def freeze(self):
        self.__tracer.processSignal(SIGSTOP)

    def cont(self):
        self.__tracer.detach()

    def read(self, address, size=None):
        if not size:
            return self.__tracer.readWord(address)
        return self.__tracer.readBytes(address, size)

    def readuint4(self, address):
        return unpack("I", self.read(address, 4))[0]

    def readlong(self, address):
        return unpack('l', self.read(address, 8))[0]

    def readfloat(self, address):
        return unpack('d', self.read(address, 8))[0]
