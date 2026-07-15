import asyncio
import httpx
from time import time, ctime

async def turn_on_light(client, base_url, student_id, light_id):
    print(f"{ctime()} | Sending request to turn on {light_id}...")
    await client.post(f"{base_url}/api/{student_id}/lights/{light_id}", json={"status": "ON"})
    print(f"{ctime()} | {light_id} is ON.")

async def main():
    MY_STUDENT_ID = "6710301008"
    BASE_URL = "http://172.16.2.117:8088"
    
    print(f"{ctime()} | --- [Task] Turning on lights concurrently (asyncio.gather) ---")
    
    async with httpx.AsyncClient() as client:
        # Reset all lights first
        await client.delete(f"{BASE_URL}/api/{MY_STUDENT_ID}/lights/reset")
        
        start_time = time()
        
        # Create tasks for all 4 lights
        tasks = [
            turn_on_light(client, BASE_URL, MY_STUDENT_ID, "light_1"),
            turn_on_light(client, BASE_URL, MY_STUDENT_ID, "light_2"),
            turn_on_light(client, BASE_URL, MY_STUDENT_ID, "light_3"),
            turn_on_light(client, BASE_URL, MY_STUDENT_ID, "light_4")
        ]
        
        # Run them all at the exact same time
        await asyncio.gather(*tasks)
        
    end_time = time()
    print(f"{ctime()} | Total time taken: {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())
