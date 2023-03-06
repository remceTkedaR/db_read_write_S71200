#  Test program for communication of Snap7 python with S7 1200
# Reading and writing db S7 1200
# by Radosław Tecmer
# radek69tecmer@gmail.com
# 2023 -02-28 ( ok)
# ------------------------

import snap7
import struct
import csv
import time
from datetime import datetime
from datetime import date
import snap7.client as c
from snap7.util import *
from snap7.types import *
import os


# Function write data from instance db, %MW,


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


def data_block_read_byte(db_number, inst_number, size=1):
    db_area = plc.db_read(db_number, inst_number, size)
    db4_byte = bin(db_area[0]).replace('0b', '')
    data_list = []
    for x in db4_byte:
        data_list.append(x)
    return data_list


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


def data_block_read_float(db_number, inst_number, data):
    db_val = plc.db_read(db_number, inst_number, data)
    value_struct = struct.iter_unpack("!f", db_val[:4])
    for value_pack in value_struct:
        value_unpack = value_pack
    # Convert tuple to float
    # using join() + float() + str() + generator expression
    result = float('.'.join(str(ele) for ele in value_unpack))
    my_str_value = '%-.4f' % result
    return my_str_value


plc = c.Client()
plc.connect('192.168.2.22', 0, 1)


# Home PLC
#  DB14 DBW 36, DB14 DBD 38, DB18 DBB19
# Job PLC
# DB1 DBW18 - oxygen
# DB1 DBW20 - oxygen 2
# DB1 DBW22 - Pressure
# DB1 DBW24 - Current

write_data_area('DB1', 1, 18, (0, 123, 0))

#write_data_area('DB1', 20, 23, 1)

#write_data_area(1, 30, (62, 234, 123, 0))

#  DB14 DBW 36, DB14 DBD 38, DB18 DBB19


#my_read = plc.db_read(14, 36, 1)

#my_read1 = data_block_read_int(14, 18, 1)
#my_read2 = data_block_read_int(14, 20, 1)


#db4 = data_block_read_byte(1, 3)


print(my_read1)
print(my_read2)
print(db4)

plc.disconnect()
