import asyncio
from bleak import BleakScanner

async def discover_services(device_address):
    from bleak import BleakClient

    async with BleakClient(device_address) as client:
        services = await client.get_services()
        for service in services:
            print(f"Service: {service.uuid}")
            for characteristic in service.characteristics:
                print(f"  Characteristic: {characteristic.uuid}")

async def discover_devices():
    devices = await BleakScanner.discover()
    for device in devices:
        print(f"Device: {device.name}, Address: {device.address}")
    return devices

async def main():
    devices = await discover_devices()
    if devices:
        address = devices[0].address  # Pick the first device
        await discover_services(address)

asyncio.run(main())
