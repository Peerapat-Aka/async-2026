# วัตถุประสงค์: ตรวจสอบบริบทการทำงานขณะรันไทม์ และเฝ้าดูคิวงานที่เปิดอยู่บน Loop ปัจจุบัน
import asyncio
from time import ctime

async def dynamic_job(number):
    await asyncio.sleep(1.0)

async def main():
    # ดึงออบเจกต์ Task ปัจจุบัน (ซึ่งก็คือ main task) ออกมาดู
    me = asyncio.current_task()
    me.set_name("Main-Coordinator")
    print(f"{ctime()} Active Execution Context Name: {me.get_name()}")
    
    # สร้าง Task ย่อยๆ หลายตัวใส่ไว้ใน Loop
    tasks = [asyncio.create_task(dynamic_job(i), name=f"Job-{i}") for i in range(3)]
    
    # ดึงรายการ Task ทั้งหมดที่กำลังทำงานหรืออยู่ในคิวของ Loop ปัจจุบัน
    all_active = asyncio.all_tasks()
    print(f"{ctime()} Total Active Tasks inside Loop: {len(all_active)}")
    for t in all_active:
        print(f"{ctime()}  -> Active Queue Item: {t.get_name()}")

    await asyncio.sleep(1.1) # รอจนกว่า Task ย่อยทั้งหมดจะทำงานเสร็จ

asyncio.run(main())