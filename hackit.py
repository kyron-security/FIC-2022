# Import modules
import sys
from pymodbus.client.sync import ModbusTcpClient

# Get the three lines
nbargs = len(sys.argv) -1
#print("=%s=" % (sys.argv))
if(nbargs!=3):
    print("wrong number of arguments (%d). Only 3 is supported" % (nbargs))
    exit()
else:
    line1 = sys.argv[1]
    line2 = sys.argv[2]
    line3 = sys.argv[3]

#    print("Line 1 = ", line1)
#    print("Line 2 = ", line2)
#    print("Line 3 = ", line3)
    
# Check the max length of lines : max 10
if (len(line1)>10):
    print("First line is too long (%d). Max is 10" % (len(line1)))
    exit()
elif (len(line2)>10):
    print("Second line is too long (%d). Max is 10" % (len(line2)))
    exit()
elif (len(line3)>10):
    print("Third line is too long (%d). Max is 10" % (len(line3)))
    exit()
else:
    print("Running...")

# add spaces for padding
while len(line1) < 10:
    line1 = "%s " % (line1)

while len(line2) < 10:
    line2 = "%s " % (line2)

while len(line3) < 10:
    line3 = "%s " % (line3)

# generate the int from the strings for each lines
li1_1 = line1[slice(0,2)]
li1_2 = line1[slice(2,4)]
li1_3 = line1[slice(4,6)]
li1_4 = line1[slice(6,8)]
li1_5 = line1[slice(8,10)]

li2_1 = line2[slice(0,2)]
li2_2 = line2[slice(2,4)]
li2_3 = line2[slice(4,6)]
li2_4 = line2[slice(6,8)]
li2_5 = line2[slice(8,10)]

li3_1 = line3[slice(0,2)]
li3_2 = line3[slice(2,4)]
li3_3 = line3[slice(4,6)]
li3_4 = line3[slice(6,8)]
li3_5 = line3[slice(8,10)]

intli1_1 = int(li1_1.encode('hex'),16)
intli1_2 = int(li1_2.encode('hex'),16)
intli1_3 = int(li1_3.encode('hex'),16)
intli1_4 = int(li1_4.encode('hex'),16)
intli1_5 = int(li1_5.encode('hex'),16)

intli2_1 = int(li2_1.encode('hex'),16)
intli2_2 = int(li2_2.encode('hex'),16)
intli2_3 = int(li2_3.encode('hex'),16)
intli2_4 = int(li2_4.encode('hex'),16)
intli2_5 = int(li2_5.encode('hex'),16)

intli3_1 = int(li3_1.encode('hex'),16)
intli3_2 = int(li3_2.encode('hex'),16)
intli3_3 = int(li3_3.encode('hex'),16)
intli3_4 = int(li3_4.encode('hex'),16)
intli3_5 = int(li3_5.encode('hex'),16)

#import logging
#logging.basicConfig()
#log = logging.getLogger()
#log.setLevel(logging.DEBUG)

client = ModbusTcpClient('172.30.2.20', port=502)
client.connect()
unit = 0x1

#write line 1
client.write_registers(1, intli1_1)
client.write_registers(3, intli1_2)
client.write_registers(5, intli1_3)
client.write_registers(7, intli1_4)
client.write_registers(9, intli1_5)


client.write_registers(11, intli2_1)
client.write_registers(13, intli2_2)
client.write_registers(15, intli2_3)
client.write_registers(17, intli2_4)
client.write_registers(19, intli2_5)

client.write_registers(21, intli3_1)
client.write_registers(23, intli3_2)
client.write_registers(25, intli3_3)
client.write_registers(27, intli3_4)
client.write_registers(29, intli3_5)

client.close()

print("Done !")
