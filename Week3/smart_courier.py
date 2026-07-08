import asyncio
from time import ctime

# 1. สร้าง Coroutine function ชื่อ delivery_task(package_id, duration)
# ฟังก์ชันนี้ใช้จำลองการส่งพัสดุ โดยรับรหัสพัสดุและเวลาที่ใช้ในการส่ง
async def delivery_task(package_id, duration):
    # พิมพ์ข้อความเมื่อเริ่มส่งของ
    print(f"{ctime()} Courier started delivering {package_id}...")
    try:
        # จำลองการส่งของด้วย asyncio.sleep(duration)
        await asyncio.sleep(duration)
        # เมื่อส่งเสร็จสิ้นให้ return ข้อความ
        return f"Package {package_id} Delivered!"
    except asyncio.CancelledError:
        # 5. ดักจับข้อผิดพลาด asyncio.CancelledError ในตัวคูรูทีนส่งของ
        # เพื่อพิมพ์ข้อความระบุว่า "Delivery Canceled! Returning package to warehouse."
        print(f"{ctime()} Delivery Canceled! Returning package to warehouse.")
        # ต้องโยนข้อผิดพลาดกลับออกไป (raise) เพื่อให้ตัวแปรภายนอกมีสถานะ .cancelled() เป็น True จริงๆ
        raise

async def main():
    # 2. ภายในฟังก์ชัน main() ให้สร้าง Task จาก delivery_task ขึ้นมา 1 ตัว 
    # โดยส่งค่า package_id="P001" และ duration=5.0 (ใช้เวลาส่ง 5 วินาที)
    # และทำการตั้งชื่อ Task นี้ว่า "Express-Courier"
    task = asyncio.create_task(delivery_task("P001", 5.0), name="Express-Courier")
    
    # 3. ให้เขียนโปรแกรมจำลองว่าระหว่างที่พัสดุกำลังเดินทาง (เช่น ผ่านไป 2 วินาที)
    await asyncio.sleep(2.0)
    
    # ให้ทำการตรวจสอบด้วยคำสั่งแฝงว่า Task นี้เสร็จหรือยัง (.done())
    # ตัวแปร is_done จะเก็บค่า True หากงานเสร็จแล้ว หรือ False หากงานยังไม่เสร็จ
    is_done = task.done()
    
    # และสั่งพิมพ์ชื่อของ Task ปัจจุบันออกมาดูบนหน้าจอ
    # .get_name() ใช้สำหรับดูชื่อที่เราตั้งไว้ตอนสร้าง Task
    print(f"{ctime()} Checking task '{task.get_name()}'. Is it done? {is_done}")
    
    # 4. หากพบว่าส่งของนานเกินไป (ผ่านไป 2 วินาทีแล้วยังไม่เสร็จ) 
    if not is_done:
        print(f"{ctime()} Taking too long! Canceling the task...")
        # ให้โปรแกรมหลักทำการยกเลิกงานนั้นทันทีด้วย .cancel()
        task.cancel()
        
    try:
        # รอให้ Task ทำงานให้จบ (ซึ่งจะจบลงด้วยการถูกยกเลิก และโยน CancelledError ออกมา)
        await task
    except asyncio.CancelledError:
        # โปรแกรมหลักรับรู้ว่าเกิดการยกเลิกงาน
        pass
        
    # 5. ตรวจสอบสถานะตัวแปรภายนอกว่า .cancelled() เป็น True หรือไม่
    # ถ้า Task ถูกยกเลิกสมบูรณ์ ค่าของ .cancelled() จะเป็น True
    is_cancelled = task.cancelled()
    print(f"{ctime()} Final verify: Is task officially canceled? {is_cancelled}")

if __name__ == "__main__":
    # เริ่มต้นการทำงานของ Event Loop
    asyncio.run(main())
