from lifxlan import LifxLAN

lifx = LifxLAN()
devices = lifx.get_devices()

print(f"Found {len(devices)} light(s).")
for light in devices:
    print(f"{light.get_label()} - {light.get_mac_addr()} - {light.get_ip_addr()}")
