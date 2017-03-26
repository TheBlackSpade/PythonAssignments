def Celcius_fahrenheit_converter(Cel_Val):
    fah_val = float(Cel_Val*1.8) + 32
    return fah_val


def Fahrenheit_Celcius_converter(Fah_Val):
    Cel_val = (float(Fah_Val)- 32)/1.8
    return Cel_val

print(Celcius_fahrenheit_converter(36.5))
print(round(Fahrenheit_Celcius_converter(98.6),3))
