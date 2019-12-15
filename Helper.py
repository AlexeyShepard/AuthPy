import random

class Helper:
    def randomPin(self):
        pincode = str()
        for i in range(6):
            digit = random.randint(0, 9)
            pincode += str(digit)
        return pincode
