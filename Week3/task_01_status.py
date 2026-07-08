# วัตถุประสงค์: เรียนรู้วิธีตรวจสอบสถานะวงจรชีวิตของออบเจกต์ Task
import asyncio
from time import ctime

async def short_job():
    await asyncio.sleep(1)
    return "Success"

async def main():
    task = asyncio.create_task(short_job())
    
    # ตรวจสอบสถานะก่อน Task จะทำงานเสร็จ
    print(f"{ctime()} Is task done? {task.done()}")          # ตรวจสอบว่างานเสร็จหรือยัง
    print(f"{ctime()} Is task canceled? {task.cancelled()}")  # ตรวจสอบว่างานถูกยกเลิกหรือยัง
    
    await task # รอให้ Task ทำงานจนเสร็จ
    
    # ตรวจสอบสถานะอีกครั้งหลังจากทำงานเสร็จแล้ว
    print(f"{ctime()} Is task done now? {task.done()}")      # ควรเป็น True
    print(f"{ctime()} Is task canceled now? {task.cancelled()}") # ควรเป็น False

asyncio.run(main())