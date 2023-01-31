import math

assert type(9/5) == float

assert math.sqrt(2) == 1.4142135623730950488

temperature = 30

# Old version
if(temperature > 25):
    print("Turning on AC...")

if(temperature < 18):
    print("Turning on heater...")

if((temperature >= 18) and (temperature <= 25)):
    print("It's comfortable!")


# New version
if((temperature >= 18) and (temperature <= 25)):
    print("It's comfortable!")
elif(temperature > 25):
    print("Turning on AC...")
else:
    print("Turning on heater...")

if(temperature < 18):
    print("Turning on heater...")
elif(temperature > 25):
    print("Turning on AC...")
else:
    print("It's comfortable!")
