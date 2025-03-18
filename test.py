import random

def color(r,g,b):
    return "\033[38;2;{};{};{}m".format(r,g,b)

print("\033[0m")
pixel = "▀"
for i in range(10):
    print("".join([color(random.randint(0,255), random.randint(0,255), random.randint(0,255)) + pixel for x in range(20)]))
print("\033[0m")