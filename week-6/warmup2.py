def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f-32)* 5/9


print(f'0°C = {round(celsius_to_fahrenheit(0), 1)}°F')

print(f'100°C = {round(celsius_to_fahrenheit(100), 1)}°F')


print(f'72°F = {round(fahrenheit_to_celsius(72), 1)}°C')