import time
import smbus


MCP4728_ADDR=0x60
mcp4728=smbus.SMBus(1)

IR_Channel=0
White_Channel=1


def mcp4728_write(channel: int, value: int):     
    command=0x40
    udac=0x00
    first_byte=(command | (channel<<1) | udac)
    vref=0x00
    power_down=0x00
    gain=0x00
    mcp4728.write_i2c_block_data(MCP4728_ADDR, first_byte, [(value>>8), (value & 0xFF)])

for i in range(0, 4095, 10):
    mcp4728_write(White_Channel, i)
    time.sleep(0.2)