#  Test program for communication of Snap7 python with S7 1200
# Reading and writing db S7 1200
# by Radosław Tecmer
# radek69tecmer@gmail.com
# 2023 -02-28 ( ok)
# ------------------------


import snap7.client as c
from snap7.util import *
from snap7.types import *


def write_data_area(db_number, start, data):
    data = bytearray(data)
    plc.write_area(Areas['DB'], db_number, start, data)


# Function write data from instance db, %MW,
def write_db(db_number, start, value):
    data = value
    plc.as_db_write(db_number, start, data)


def test_db_write_byte(db_number, start, size):
    data = bytes(size)
    plc.as_db_write(db_number, start, data)


# function reading real

def data_block_read(db_number, inst_number, data):
    db_val = plc.db_read(db_number, inst_number, data)
    value_struct = struct.iter_unpack("!f", db_val[:4])
    for value_pack in value_struct:
        value_unpack = value_pack
    # Convert tuple to float
    # using join() + float() + str() + generator expression
    result = float('.'.join(str(ele) for ele in value_unpack))
    my_str_value = '%-.4f' % result
    return my_str_value


# function reading int

def data_block_read_int(db_number, inst_number, data):
    db_val = plc.db_read(db_number, inst_number, data)
    value_struct = struct.iter_unpack("!h", db_val[:2])
    for value_pack in value_struct:
        value_unpack = value_pack
    # Convert tuple to float
    # using join() + float() + str() + generator expression
    result = int('.'.join(str(ele) for ele in value_unpack))
    my_str_value = '%-.2i' % result
    return my_str_value


plc = c.Client()
plc.connect('192.168.2.22', 0, 1)


# PLC
#  data
#
# DB14 DBW18 - oxygen
# DB1 DBW20 - oxygen 2
# DB1 DBB30 -
# DB1 DBW74 - Current

write_data_area(14, 18, (5, 0, 0, 0))


# writing byte-by-byte saving
write_data_area(14, 30, (10, 0, 0, 0))

# reading  bytearray (b'\x00\x00\x00\x00')

my_read = plc.db_read(14, 36, 4)

my_read1 = data_block_read_int(14, 18, 2)
my_read2 = data_block_read_int(14, 20, 2)
my_read3 = data_block_read(14, 74, 4)
my_read4 = data_block_read_int(14, 30, 2)


print(my_read)
print(my_read1)
print(my_read2)
print(my_read3)
print(my_read4)


plc.disconnect()
