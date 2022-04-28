def gray2binary(gray):
    binary = gray
    while gray > 0:
        gray >>= 1
        binary ^= gray
        
    return binary


def read16Position(p1State, p2State, p3State, p4State):
    gray = int(str(p4State) + str(p3State) + str(p2State) + str(p1State), 2)
       
    # convert gray code to binary
    position = gray2binary(gray)
    
    return position

def read8Position(p1State, p2State, p3State, p4State):
    gray = str(p1State) + str(p2State) + str(p3State) + str(p4State)
    
    switcher = {
        '0000' : 7,
        '0100' : 6,
        '1100' : 5,
        '1110' : 4,
        '0110' : 3,
        '0111' : 2,
        '0011' : 1,
        '0010' : 0
    }
    
    return switcher.get(gray, 0)