###############################################################
# Imports
###############################################################
from Deadline.Events import *
from Deadline.Scripting import *
from Deadline.Jobs import *
from datetime import datetime
from System import DateTime , TimeSpan



def GetDeadlineEventListener():
    return ArtfxDynamicMachineLimit()


def CleanupDeadlineEventListener(eventListener):
    eventListener.Cleanup()


###############################################################
# The event listener class.
###############################################################
class ArtfxDynamicMachineLimit(DeadlineEventListener):
    def __init__(self):
       pass
    
    def Cleanup(self):
        pass


