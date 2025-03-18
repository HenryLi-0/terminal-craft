from subsystems.display import *

displayData = DisplayData.generateRandom()
display = Display()
while True:
    time.sleep(0.03)
    display.render(displayData)