def display(lcd, row1, row2, color):
    lcd.clear()
    cursor1 = int((16 - len(row1)) / 2)
    cursor2 = int((16 - len(row2)) / 2)
    lcd.setCursor(cursor1, 0)
    lcd.printout(row1)
    lcd.setCursor(cursor2, 1)
    lcd.printout(row2)
    lcd.setRGB(color[0], color[1], color[2])
    
      
def print_time(time):
    m, s = divmod(time, 60)
    h, m = divmod(m, 60)
    s = round(s, 1)
    
    ss = str(s)
    mm = str(int(m))
    hh = str(int(h))
    
    if s < 10:
        ss = '0' + ss
    if m < 10:
        mm = '0' + mm
    if h < 10:
        hh = '0' + hh
        
    return hh + ':' + mm + ':' + ss