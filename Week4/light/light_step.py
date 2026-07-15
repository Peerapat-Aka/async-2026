import asyncio
import httpx
from time import time, ctime

async def main():
    MY_STUDENT_ID = "6710301008"
    BASE_URL = "http://172.16.2.117:8088"
    
    print(f"{ctime()} | --- [Task] Turning on lights step-by-step ---")
    
    # First, let's reset all lights to OFF to start fresh
    async with httpx.AsyncClient() as client:
        await client.delete(f"{BASE_URL}/api/{MY_STUDENT_ID}/lights/reset")
        
        start_time = time()
        
        # Step 1: Turn on light 1
        print(f"{ctime()} | Turning on light_1...")
        await client.post(f"{BASE_URL}/api/{MY_STUDENT_ID}/lights/light_1", json={"status": "ON"})
        print(f"{ctime()} | light_1 is ON.")
        
        # Step 2: Turn on light 2
        print(f"{ctime()} | Turning on light_2...")
        await client.post(f"{BASE_URL}/api/{MY_STUDENT_ID}/lights/light_2", json={"status": "ON"})
        print(f"{ctime()} | light_2 is ON.")
        
        # Step 3: Turn on light 3
        print(f"{ctime()} | Turning on light_3...")
        await client.post(f"{BASE_URL}/api/{MY_STUDENT_ID}/lights/light_3", json={"status": "ON"})
        print(f"{ctime()} | light_3 is ON.")
        
        # Step 4: Turn on light 4
        print(f"{ctime()} | Turning on light_4...")
        await client.post(f"{BASE_URL}/api/{MY_STUDENT_ID}/lights/light_4", json={"status": "ON"})
        print(f"{ctime()} | light_4 is ON.")
        
    end_time = time()
    print(f"{ctime()} | Total time taken: {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())
