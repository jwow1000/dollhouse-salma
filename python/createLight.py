from lifxlan import LifxLAN, Light
import time

lifx = LifxLAN()
light = Light("d0:73:d5:84:3b:1f", "192.168.0.165")     

light.set_power("on")
time.sleep(0.5)  # give it a moment to power on
light.set_color([10000, 65535, 65535, 3500], duration=5000)  # full red, full brightness