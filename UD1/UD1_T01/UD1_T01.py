# Conversor de temperaturas

temperatura = int(input("Introduce una temperatura en grados Celsius"))

tempF = (temperatura * 9/5) +32
tempK = temperatura + 273.15

print(f"La temperaura en Fahrenheit es {tempF} ºF")
print(f"La temperaura en Keelvin es {tempK} K")