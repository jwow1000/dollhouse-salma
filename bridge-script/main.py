from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
from lifxlan import LifxLAN, Light
from dotenv import load_dotenv
import os

# load env variables
load_dotenv()

# load env script
print("MAC:", os.getenv("BULB1_MAC"))
print("IP:", os.getenv("BULB1_IP"))

# Map bulb names to Light objects
lifx = LifxLAN()
bulbs = {
    "bulb1": Light(os.getenv("BULB1_MAC"), os.getenv("BULB1_IP")),
    "bulb2": Light(os.getenv("BULB2_MAC"), os.getenv("BULB2_IP"))
}

# change color and brightness handler
def set_color_handler(addr, *args):
    print("we got a message")
    bulb_name = addr.split("/")[1]  # e.g. 'bulb1' from '/bulb1/set_color'
    if bulb_name in bulbs:
        bulbs[bulb_name].set_color(args[:4], duration=args[4] if len(args) > 4 else 1000)

# dispatcher to receive the messages from pd
dispatcher = Dispatcher()
dispatcher.map("/bulb1/set_color", set_color_handler)
dispatcher.map("/bulb2/set_color", set_color_handler)
dispatcher.map("/bulb3/set_color", set_color_handler)
dispatcher.map("/bulb4/set_color", set_color_handler)
dispatcher.map("/bulb5/set_color", set_color_handler)
dispatcher.map("/bulb6/set_color", set_color_handler)

# osc server
server = osc_server.ThreadingOSCUDPServer(("0.0.0.0", 9000), dispatcher)
print("Listening on port 9000...")
server.serve_forever()