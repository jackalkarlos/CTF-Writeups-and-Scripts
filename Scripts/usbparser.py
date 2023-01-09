#!/usr/bin/env python3
import logging
# disable warning messages
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
# pip3 install scapy-python3
from scapy.all import PcapReader
import sys, binascii

if len(sys.argv) != 2:
    print('Usage: {} <usb pcap file>'.format(sys.argv[0]))
    sys.exit(1)
packets = PcapReader(sys.argv[1])

# parse left right arrow keys
def cleanup(dirty):
    pointer = 0
    tmp = []
    for c in dirty:
        if c == '←': # left arrow
            pointer-=1
        elif c == '→': # right arrow
            pointer+=1
        elif c == '\b': # backspace
            try:
                pointer-=1
                del tmp[pointer]
            except IndexError:
                pointer+=1
        elif c == '⌦': # delete key
            try:
                del tmp[pointer]
            except IndexError:
                pass
        else:
            tmp.insert(pointer, c)
            pointer+=1
    return ''.join(tmp)

# uses US keyboard mapping
# does not detect home, end, page up, page down, function keys, insert key
# also does not support keypad num lock stuff
# keycode references: https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2
# shows arrow up and down keys but they are not parsed
shiftMapping = {'1e':'!', '1f':'@', '20':'#', '21':'$', '22':'%', '23':'^', '24':'&', '25':'*', '26':'(', '27':')',
'28':'\n', '2a':'\b', '2b':'\t', '2c':' ', '2d':'_', '2e':'+', '2f':'{', '30':'}', '31':'|', '33':':', '34':'"',
'35':'~', '36':'<', '37':'>', '38':'?', '4c':'⌦', '4f':'→', '50':'←', '51':'↓', '52':'↑'}

mapping = {'28':'\n', '2a':'\b', '2b':'\t', '2c':' ', '2d':'-', '2e':'=', '2f':'[', '30':']', '31':'\\', '33':';',
'34':'\'', '35':'`', '36':',', '37':'.', '38':'/', '4c':'⌦', '4f':'→', '50':'←', '51':'↓', '52':'↑'}

parsedPackets = []
output = ''
caps = False
# Let's iterate and parse every packet
for pkt in packets:
    pktType = str(binascii.hexlify(bytes(pkt)))[44:48]
    if pktType != '8101': # only parse interrupt in packets
        continue
    keyBytes = str(binascii.hexlify(bytes(pkt)))[-17:-1]
    if keyBytes == '0000000000000000' or keyBytes[-14:] == '00000000000000':
        continue
    modifyer = keyBytes[0]+keyBytes[1]
    key = keyBytes[4]+keyBytes[5]
    intKey = int(key, 16)
    if modifyer == '02': # shift key pressed
        if intKey != 0:
            if key in shiftMapping: # shift symbols
                output += shiftMapping[key]
                continue
            elif intKey >= 4 and intKey <= 29: # uppercase alphabets
                output += chr(intKey+61)
                continue
#            else:
                # key not supported yet
#                print("Unknown Key Combination\nKey Code: {} Modifyer: {}".format(key, modifyer))
#                continue
        else:
            continue
    if intKey >= 0x4 and intKey <= 0x1d: # lowercase alphabets
        if caps:
            chr(intKey+61)
        else:
            output += chr(intKey+93)
    elif intKey < 0x27: # numbers 1-9
        output+=str(intKey-29)
    elif intKey == 0x27: # number 0
        output += '0'
    elif key in mapping: # symbols
        output += mapping[key]
    elif key == '39':
        if caps:
            caps = False
        else:
            caps = True
#    else:
#        # key not supported yet
#        print("Unknown Key Combination\nKey Code: {} Modifyer: {}".format(key, modifyer))
#        continue

# display parsed string
print(cleanup(output))
