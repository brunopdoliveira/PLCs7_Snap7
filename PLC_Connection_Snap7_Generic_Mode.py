##########################################################################################
#                           PLC CONNECTION WITH SNAP 7 - Generic Mode                    #
##########################################################################################

# import libraries
import snap7
import time

# define IP, RACK & SLOT of PLC
IP = '192.168.0.1'
RACK = 0
SLOT = 1

# define DB number, start address & size
DB_NUMBER = 1
START_ADDRESS = 0
SIZE = 259

# connect to PLC
plc = snap7.client.Client()
plc.connect(IP, RACK, SLOT)
plc.get_connected()

# get info Module Type of CPU
plc_info = plc.get_cpu_info()
print(f'Module Type: {plc_info.ModuleTypeName}')

# get info state of CPU
state = plc.get_cpu_state()
print(f'State:{state}')

# initialize db to read data
db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)

# reads the db number 1 starting from the byte 2 until byte 256 (string type)
product_name = db[2:256].decode('UTF-8').strip('\x00')
print(f'PRODUCT NAME: {product_name}')

# reads the db number 1 starting from the byte 256 until byte 258
product_value = int.from_bytes(db[256:258], byteorder='big')
print(f'PRODUCT VALUE: {product_value}')

# reads the db number 1 starting from the byte 258 until byte 258
product_status = bool(db[258])
print(product_status)

# delay
time.sleep(15)

#Bruno Oliveira
