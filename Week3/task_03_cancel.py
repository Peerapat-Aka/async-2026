# วัตถุประสงค์: หยุดการทำงานที่กำลังดำเนินการอยู่ก่อนกำหนด โดยกระตุ้นให้เกิด Cancellation Exception
import asyncio
from time import ctime

async def background_loop():
    try:
        print(f"{ctime()} Worker: Starting long infinite process...")
        while True:
            await asyncio.sleep(1)
            print(f"{ctime()} Worker: Still ticking...")
    except asyncio.CancelledError:
        # ดักจับข้อผิดพลาดเมื่อถูกสั่งยกเลิกงาน
        print(f"{ctime()} Worker: Interrupted! Executing clean-up logic before exit...")

async def main():
    task = asyncio.create_task(background_loop())
    await asyncio.sleep(2.5) # ปล่อยให้ Task ทำงานไป 2.5 วินาที
    
    print(f"{ctime()} Main: Changing plans, canceling the worker task now!")
    task.cancel() # สั่งยกเลิก Task
    await asyncio.sleep(0.1) # รอเวลาเล็กน้อยเพื่อให้ Task จัดการ Exception จนเสร็จ

asyncio.run(main())