import time
import smbus

MCP4725_ADDR=0x60
mcp4725=smbus.SMBus(1)

def mcp4725_write(value: int ):
        fast_mode: int=0x00
        fast_mode=fast_mode << 6
        power_down: int=0x00
        power_down=power_down<<4
        digital_data: int=value  
        digital_data_4_bit: int=int(digital_data>>8)
        digital_data_8_bit: int=int(digital_data & 0xFF)
        first_byte: int=int(fast_mode | power_down | digital_data_4_bit)
        mcp4725.write_byte_data(MCP4725_ADDR, first_byte, digital_data_8_bit)

mcp4725_write(0)
print(0)
time.sleep(0.5)
mcp4725_write(2000)
print(3500)
time.sleep(0.5)
mcp4725_write(0)
print(0)
