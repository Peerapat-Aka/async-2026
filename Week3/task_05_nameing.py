# วัตถุประสงค์: ตั้งชื่อให้กับออบเจกต์ Task อย่างชัดเจนเพื่อให้ง่ายต่อการเขียนล็อกและติดตามในระบบจริง
import asyncio
from time import ctime

async def background_worker():
    await asyncio.sleep(0.1)

async def main():
    task = asyncio.create_task(background_worker())
    
    # ตรวจสอบชื่อเริ่มต้นของ Task ที่ระบบตั้งให้
    print(f"{ctime()} Initial Name: {task.get_name()}") # ปกติจะเป็นชื่อเช่น Task-1, Task-2
    
    # เปลี่ยนชื่อของ Task ให้สื่อความหมายมากขึ้น
    task.set_name("Payment-Gateway-Validator")
    print(f"{ctime()} Updated Name: {task.get_name()}") # จะได้ชื่อที่เราตั้งไว้

asyncio.run(main())