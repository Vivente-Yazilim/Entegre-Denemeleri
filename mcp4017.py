import time
import smbus
import picamera
MCP4017_ADDR=0x2F
mcp4017=smbus.SMBus(1)

def mcp4017_write(value: int):
    mcp4017.write_byte(MCP4017_ADDR,value)

for i in range(1,127):
     print(i)
     mcp4017_write(i)
     time.sleep(0.1)

time.sleep(0.1)
mcp4017_write(0)    
