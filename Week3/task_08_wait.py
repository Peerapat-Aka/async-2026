# วัตถุประสงค์: สร้างเวิร์กโฟลว์การประมวลผลที่ซับซ้อนตามเงื่อนไขความสำเร็จของงาน (Task)
import asyncio
from time import ctime

async def network_probe(server_name, delay):
    await asyncio.sleep(delay)
    return f"Ping successful: {server_name}"

async def main():
    # สร้างกลุ่มของ Task เพื่อทำงานพร้อมๆ กัน (ใช้ set เก็บ Task)
    tasks = {
        asyncio.create_task(network_probe("Primary-Server", 2.0)),
        asyncio.create_task(network_probe("Backup-Server-1", 0.5)),
        asyncio.create_task(network_probe("Backup-Server-2", 1.0))
    }
    
    # ใช้ asyncio.wait เพื่อรอให้ Task ใด Task หนึ่งเสร็จสิ้นเป็นอย่างแรก (FIRST_COMPLETED)
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    print(f"{ctime()} Count of Tasks Done: {len(done)}")       # จำนวนงานที่เสร็จแล้ว
    print(f"{ctime()} Count of Tasks Pending: {len(pending)}") # จำนวนงานที่ยังค้างอยู่
    
    for finished_task in done:
        print(f"{ctime()} Fastest Task Result: {finished_task.result()}")
        
    # ยกเลิกงานที่เหลือที่ยังทำงานไม่เสร็จ
    for ongoing_task in pending:
        ongoing_task.cancel()

asyncio.run(main())