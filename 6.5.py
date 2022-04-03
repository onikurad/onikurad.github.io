decimal_number = int(input("Enter a number: "))

conversion_table = {0: '0', 1: '1', 2: '2', 3: '3',
                    4: '4', 5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B',
                    12: 'C', 13: 'D', 14: 'E', 15: 'F'}
  
def to_hex(decimal_number):
    if(decimal_number <= 0):
        return ''
    remainder = decimal_number % 16
    return to_hex(decimal_number//16) + conversion_table[remainder]
  
print("The hexadecimal form of", decimal_number,
      "is", to_hex(decimal_number))


decimal_red = int(input("Enter a RED number: "))
decimal_green = int(input("Enter a GREEN number: "))
decimal_blue = int(input("Enter a BLUE number: "))

def hex_colorR(decimal_red):
    if(decimal_red <= 0):
        return ''
    remainder = decimal_red % 16
    return hex_colorR(decimal_red//16) + conversion_table[remainder]

def hex_colorG(decimal_green):
    if(decimal_green <= 0):
        return ''
    remainder = decimal_green % 16
    return hex_colorG(decimal_green//16) + conversion_table[remainder]

def hex_colorB(decimal_blue):
    if(decimal_blue <= 0):
        return ''
    remainder = decimal_blue % 16
    return hex_colorB(decimal_blue//16) + conversion_table[remainder]


print("#"+str(hex_colorR(decimal_red))+str(hex_colorG(decimal_green))+str(hex_colorB(decimal_blue)))    
