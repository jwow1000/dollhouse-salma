from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
from lifxlan import LifxLAN, Light, WorkflowException
from dotenv import load_dotenv
import requests
import os
import time

# load env variables
load_dotenv()

# notify flask server function
def notify_flask(status_msg):
    try:
        response = requests.post("http://localhost:5000/bulb-status", json={"status": status_msg})
        print("Status sent to Flask:", response.text)
    except Exception as e:
        print("Failed to contact Flask server:", e)

# test connection function
MAX_RETRIES = 5
RETRY_DELAY = 2  # seconds

def try_connect_bulb(mac, ip, name):
    for attempt in range(MAX_RETRIES):
        try:
            bulb = Light(mac, ip)
            bulb.get_power()  # simple ping/test command
            print(f"{name} connected!")
            return bulb
        except Exception as e:
            print(f"[{name}] Attempt {attempt+1} failed: {e}")
            time.sleep(RETRY_DELAY)
    print(f"[{name}] FAILED to connect after {MAX_RETRIES} attempts.")
    return None

# Map bulb names to Light objects
lifx = LifxLAN()
bulbs = {
    "bulb1": try_connect_bulb(os.getenv("BULB1_MAC"), os.getenv("BULB1_IP"), "bulb1"),
    "bulb2": try_connect_bulb(os.getenv("BULB2_MAC"), os.getenv("BULB2_IP"), "bulb2"),
}
# Remove bulbs that failed to connect
bulbs = {k: v for k, v in bulbs.items() if v is not None}

# Stop script and notify flask server 
if len(bulbs) < 6:
    print("ERROR: Not all bulbs connected. Aborting startup.")
    # Notify Flask server here 
    notify_flask("ERROR: Not all bulbs connected.")
    exit(1)

# change color and brightness handler
def set_color_handler(addr, *args):
    bulb_name = addr.split("/")[1]  # e.g. 'bulb1' from '/bulb1/set_color'
    bulb = bulbs.get(bulb_name)
    if bulb:
        try:
            bulbs[bulb_name].set_color(args[:4], duration=args[4] if len(args) > 4 else 1000)
        except WorkflowException as e:
            print(f"Failed to set color on {bulb_name}: {e}")
    else: 
        print(f"No bulb found with name {bulb_name}")


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