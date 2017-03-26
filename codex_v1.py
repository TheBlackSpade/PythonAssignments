def Celcius_Fahrenheit_converter(Temp_Val, ConvType):
    if ConvType == "C2F":
        Calc_Temp =  (Temp_Val*1.8) + 32
    else:
        Calc_Temp =  ((Temp_Val)- 32)/1.8

    return Calc_Temp


User_Temp = float(input("Oi, Mate...What's your anal Temp? "))
UserInputtype = input("Is it in Celcius? (Y/N) ").upper()
if UserInputtype == "Y":
    if User_Temp < -272:
        print("Oi, Mate..Have you gone bonkers")
    else:
        print(Celcius_Fahrenheit_converter(User_Temp ,"C2F"))
else:
    if Celcius_Fahrenheit_converter(User_Temp ,"F2C") < -272:
        print("Oi, Mate..Have you gone bonkers")
    else:
        print(Celcius_Fahrenheit_converter(User_Temp ,"F2C"))
