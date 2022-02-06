##########################################################################################
#                           PLC CONNECTION WITH SNAP 7                                   #
##########################################################################################

# import libraries
import snap7
from snap7 import util

# define IP, RACK & SLOT of PLC
IP = '192.168.0.1'
RACK = 0
SLOT = 1

# connect to PLC
plc = snap7.client.Client()
plc.connect(IP, RACK, SLOT)
plc.get_connected()

# reads the db number 1 starting from the byte 0 until byte 4 (real type).
db = plc.db_read(1, 0, 4)
t = util.get_real(db, 0)
print(t)

# reads the db number 1 starting from the byte 4 until byte 6 (int type).
db = plc.db_read(1, 4, 2)
t = util.get_int(db, 0)
print(t)

# reads the db number 1 starting from the byte 6 until byte 8 (int type).
db = plc.db_read(1, 6, 2)
t = util.get_int(db, 0)
print(t)

# reads the db number 1 starting from the byte 10 until byte 11 (bool type).
db = plc.db_read(1, 10, 1)
# read byte_index 0 and bit_index 0
t = util.get_bool(db, 0, 0)
print(t)

# writes the db number 2 a boolean status in bytearray
buffer = bytearray([0b00000001])
wt = plc.db_write(2, 0, buffer)
print(t)

#Bruno Oliveira



