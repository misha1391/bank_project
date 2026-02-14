from datetime import datetime

def GetCurrentTime() -> str:
    time = datetime.now()
    return str(time.year)+"-"+str(time.month)+"-"+str(time.day)+" "+str(time.hour)+":"+str(time.minute)+":"+str(time.second)