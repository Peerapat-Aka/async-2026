import asyncio
from time import ctime

# 1. สร้าง Coroutine function ชื่อ fetch_stock_price(server_name, delay)
# ฟังก์ชันนี้ใช้จำลองการดึงข้อมูลราคาหุ้นจากเซิร์ฟเวอร์
async def fetch_stock_price(server_name, delay):
    # จำลองความหน่วงเวลาของแต่ละเซิร์ฟเวอร์
    await asyncio.sleep(delay)
    # คืนค่าผลลัพธ์เมื่อทำงานเสร็จ
    return f"[{server_name}] Price: 150 USD"

async def main():
    # 2. ภายในฟังก์ชัน main() ให้แตก Task ขึ้นมา 3 ตัวพร้อมกันใน Event Loop
    # สร้างกลุ่มของ Task ทั้ง 3 เซิร์ฟเวอร์
    tasks = {
        asyncio.create_task(fetch_stock_price("Alpha", 3.0)),
        asyncio.create_task(fetch_stock_price("Beta", 0.8)),
        asyncio.create_task(fetch_stock_price("Gamma", 1.5))
    }
    
    # 3. ใช้ asyncio.wait() เพื่อทำให้ระบบดีดตัวหลุดจากการรอทันทีเมื่อมีเซิร์ฟเวอร์ตัวแรกส่งข้อมูลกลับมาสำเร็จ
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    # 4. แสดงผลลัพธ์ของเซิร์ฟเวอร์ที่ชนะการแข่งขัน (ตัวที่เร็วที่สุด) ออกทางหน้าจอ
    # ดึงค่า Task ตัวแรกใน set ของ done
    winner_task = list(done)[0]
    print(f"{ctime()} Winner Result: {winner_task.result()}")
    
    # 5. เขียนคำสั่งวนลูปเคลียร์ระบบอัตโนมัติ เพื่อสั่งยกเลิก (.cancel()) งานของเซิร์ฟเวอร์อีก 2 ตัวที่เหลือ
    print(f"{ctime()} Cleaning up {len(pending)} pending tasks...")
    for task in pending:
        task.cancel()

if __name__ == "__main__":
    asyncio.run(main())
