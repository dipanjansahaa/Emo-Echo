import asyncio
from bleak import BleakClient

DEVICE_ADDRESS = "D0:FF:5A:62:4D:31"  # Replace with your device's address
HEART_RATE_CHARACTERISTIC_UUID = "00002A37-0000-1000-8000-00805F9B34FB"

async def get_heart_rate():
    async with BleakClient(DEVICE_ADDRESS) as client:
        print("Connected to device.")
        await client.start_notify(HEART_RATE_CHARACTERISTIC_UUID, notification_handler)

        # Listen for heart rate data for 30 seconds
        await asyncio.sleep(30)
        await client.stop_notify(HEART_RATE_CHARACTERISTIC_UUID)

def notification_handler(sender, data):
    heart_rate = int(data[1])  # Decode the heart rate value
    print(f"Heart Rate: {heart_rate} bpm")

asyncio.run(get_heart_rate())
