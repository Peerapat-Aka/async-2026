# วัตถุประสงค์: จัดกลุ่มหลายการทำงานให้รันพร้อมกัน (concurrently) และคืนค่าผลลัพธ์เป็นลิสต์ตามลำดับ
import asyncio
from time import time, ctime

async def fetch_db_record(table_name, latency):
    await asyncio.sleep(latency)
    return f"RowData_{table_name}"

async def main():
    start = time()
    
    # ใช้ asyncio.gather เพื่อสั่งให้ฟังก์ชันทั้ง 3 ทำงานพร้อมๆ กัน และรอจนกว่าทั้งหมดจะเสร็จ
    results = await asyncio.gather(
        fetch_db_record("Users", 1.0),
        fetch_db_record("Products", 0.5),
        fetch_db_record("Invoices", 1.0)
    )
    
    print(f"{ctime()} Aggregated Output Results List: {results}")
    print(f"{ctime()} Execution Completed in: {time() - start:.2f} seconds") # จะใช้เวลาเท่ากับ task ที่ช้าที่สุด (1 วินาที)

asyncio.run(main())