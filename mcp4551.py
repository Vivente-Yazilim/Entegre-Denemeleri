import smbus
import time
bus=smbus.SMBus(1)
addr=0x2e
WRITE_COMMAND=0x00
value=0

first_byte: int =((value>>7) | WRITE_COMMAND)
second_byte: int = int(value & 0xFF)
bus.write_byte_data(addr, first_byte,second_byte)

for i in range(0, 250):    
    value=i
    first_byte: int =((value>>7) | WRITE_COMMAND)
    second_byte: int = int(value & 0xFF)
    bus.write_byte_data(addr, first_byte,second_byte)
    time.sleep(0.1)
    
value=0
first_byte: int =((value>>7) | WRITE_COMMAND)
second_byte: int = int(value & 0xFF)
bus.write_byte_data(addr, first_byte,second_byte)