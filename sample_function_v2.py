def getHours(Mins, Secs = 7200, MilliSecs = 360000 ):
    hours = Mins/60 + Secs/3600 + MilliSecs/360000
    print(hours)
    #print("Secs - " + str(Secs/3600))
    #print("MilliSecs - " + str(MilliSecs/360000))


getHours(240, MilliSecs= 720000)
