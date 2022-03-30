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
        '0000' : 0,
        '0100' : 1,
        '1100' : 2,
        '1110' : 3,
        '0110' : 4,
        '0111' : 5,
        '0011' : 6,
        '0010' : 7
    }
    
    return switcher.get(gray, 0)