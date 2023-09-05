import spidev
import argparse

parser = argparse.ArgumentParser(
        prog="external_mic",
        description="Configure the soundcard"
        )
parser.add_argument("-g", "--gain", required=True)
parser.add_argument("-p", "--phantom", choices=['none', 'pip', 'p48', '3v3'], required=True)

args = parser.parse_args()
gain = int(args.gain)

if not (gain >= 0 and gain <= 20):
    print("gain must be between 0 and 20")
    exit(-1)

if args.phantom ==  "none":
    gpo = 0
elif args.phantom == "pip":
    gpo = 1<<0
elif args.phantom == "p48":
    gpo = 1<<2
elif args.phantom == "3v3":
    gpo = 1<<1

print("Setting phantom to {} and gain to {} dB".format(args.phantom, gain*3))

spi = spidev.SpiDev()
bus = 0     #SPI0
device = 0  #CS0
spi.open(bus, device)

spi.max_speed_hz = 10_000_000

GPOMD = 1   # Update GPO outputs on next audio zero-crossing
GAINMD = 1  # Update gain on next audio zero-crossing

msb = GPOMD<<5 | GAINMD<<4 | gpo
lsb = gain 

to_send = [lsb, msb]
spi.writebytes(to_send)

