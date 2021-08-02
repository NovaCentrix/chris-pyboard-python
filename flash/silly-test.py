import machine
import pyb
import utime

message = 'there'
uart = pyb.UART(6, 115200)
# while True:
#   uart.write(message.encode())
#   utime.sleep(0.1)
#

while True:
  if uart.any():
    ch=uart.readchar()
    uart.writechar(ch)
    