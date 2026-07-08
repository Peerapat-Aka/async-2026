# วัตถุประสงค์: ดึงข้อมูลที่ส่งกลับอย่างปลอดภัยและตรวจสอบ Task ที่แครชโดยไม่ทำให้ลูปหลักพัง
import asyncio
from time import ctime

async def division_worker(a, b):
    await asyncio.sleep(0.5)
    return a / b # อาจเกิด ZeroDivisionError ได้ถ้า b เป็น 0

async def main():
    task_success = asyncio.create_task(division_worker(10, 2))
    task_fail = asyncio.create_task(division_worker(10, 0))

    # รอให้ทั้งสอง Task ทำงานจนเสร็จสิ้น (หรือไม่ก็เกิดข้อผิดพลาด)
    await asyncio.sleep(1)
    
    # ตรวจสอบและดึงผลลัพธ์ของ Task ที่ทำงานสำเร็จ
    if task_success.done() and not task_success.exception():
        print(f"{ctime()} Task Success Result: {task_success.result()}") # ดึงค่าผลลัพธ์ออกมา
        
    # ตรวจสอบและดึงข้อผิดพลาดของ Task ที่ล้มเหลว
    if task_fail.done():
        print(f"{ctime()} Task Fail Exception: {type(task_fail.exception()).__name__}") # ดึงประเภทของ Exception ออกมา

asyncio.run(main())