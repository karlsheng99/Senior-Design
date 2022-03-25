def gray2binary(gray):
    binary = gray
    while gray > 0:
        gray >>= 1
        binary ^= gray
        
    return binary


def readPosition(p1State, p2State, p3State, p4State):
    gray = int(str(p4State) + str(p3State) + str(p2State) + str(p1State), 2)
       
    # convert gray code to binary
    binary = gray2binary(gray)
    position = binary
    
    return binary, position