# Predict temperature using hardcoded coefficients
a = 0.5
b = -3
c = 28
t = 5  # e.g., 5th hour or 5th day

T = a * t**2 + b * t + c
print(f"Hardcoded Values - Predicted temperature at t={t}: {T:.2f}°C")

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
t = float(input("Enter time t (hour/day): "))
T = a * t**2 + b * t + c
print(f"Input Values - Predicted temperature at t={t}: {T:.2f}°C")

with open("inputs_single.txt", "r") as f:
    lines = f.readlines()

a = float(lines[0])
b = float(lines[1])
c = float(lines[2])
t = float(lines[3])

T = a * t**2 + b * t + c
print(f"File Single Input - Predicted temperature at t={t}: {T:.2f}°C")

with open("inputs_multiple.txt", "r") as f:
    for line in f:
        a, b, c, t = map(float, line.strip().split())
        T = a * t**2 + b * t + c
        print(f"File Multiple Output - a={a}, b={b}, c={c}, t={t} -> T={T:.2f}°C")
