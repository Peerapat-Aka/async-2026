import asyncio
import httpx  
from time import ctime

async def fetch_stock_price(server_name: str):
    """
    TODO: Assignment 3 - เขียนฟังก์ชันเชื่อมต่อ Mock Server ผ่านระบบเครือข่าย
    1. กำหนดเป้าหมายไปที่พอร์ต 8088 ตามสเปกเซิร์ฟเวอร์ของอาจารย์
    2. ใช้ httpx.AsyncClient() ดึงข้อมูลเพื่อไม่ให้เกิดการ Block สัญญาณ Event Loop
    3. นำข้อมูล JSON (server และ price_usd) มาจัดฟอร์แมตแสดงผล
    """
    url = f"http://172.16.2.117:8088/price/{server_name}"
    
    # 2. ใช้ httpx.AsyncClient() ดึงข้อมูลเพื่อไม่ให้เกิดการ Block สัญญาณ Event Loop
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        # 3. นำข้อมูล JSON (server และ price_usd) มาจัดฟอร์แมตแสดงผล
        return f"[{data['server']}] Price: {data['price_usd']} USD"

async def main():
    # 4. ทำการแปลงฟังก์ชันคอรูทีนดึงข้อมูลของทั้ง 3 สาขา (Alpha, Beta, Gamma) ให้กลายเป็น asyncio.Task
    # เพื่อส่งเข้าคิวรันพร้อมกันใน Event Loop
    tasks = {
        asyncio.create_task(fetch_stock_price("Alpha")),
        asyncio.create_task(fetch_stock_price("Beta")),
        asyncio.create_task(fetch_stock_price("Gamma"))
    }
    
    # 5. ใช้คำสั่ง asyncio.wait() และระบุออปชันเงื่อนไข return_when=asyncio.FIRST_COMPLETED 
    # เพื่อให้โปรแกรมหลักดีดตัวหลุดจากการรอทันทีเมื่อมีเซิร์ฟเวอร์ตัวแรกส่งข้อมูลกลับมาสำเร็จ
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    # 6. ดึงผลลัพธ์จากเซิร์ฟเวอร์ที่ชนะการแข่งขัน (ตัวที่เร็วที่สุด) ออกมาพิมพ์แสดงบนหน้าจอ
    winner_task = list(done)[0]
    print(f"{ctime()} Winner Result: {winner_task.result()}")
    
    # 7. [สำคัญมาก - Anti-Memory Leak]: เขียนคำสั่งวนลูปดึงงานที่ยังคงค้างคาอยู่ในเซต pending 
    # มาสั่งยกเลิกงานทิ้งให้หมดสิ้นด้วยคำสั่ง .cancel() เพื่อตัดสัญญาณ Network Request ที่ยังวิ่งค้างอยู่
    print(f"{ctime()} Cleaning up {len(pending)} pending tasks...")
    for task in pending:
        task.cancel()

if __name__ == "__main__":
    asyncio.run(main())