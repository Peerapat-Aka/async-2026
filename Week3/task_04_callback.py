# วัตถุประสงค์: แนบฟังก์ชัน synchronous ทั่วไปที่จะถูกเรียกโดยอัตโนมัติเมื่อ Task ทำงานเสร็จ
import asyncio
from time import ctime

def alert_manager(finished_task):
    # ฟังก์ชันนี้จะถูกเรียกทันทีที่ Task (download_file) ทำงานเสร็จ
    print(f"{ctime()} Callback Triggered! Task output fetched: {finished_task.result()}")

async def download_file():
    print(f"{ctime()} Downloading packet...")
    await asyncio.sleep(1.0)
    return "Data_Payload.zip"

async def main():
    task = asyncio.create_task(download_file())
    # ผูกฟังก์ชัน alert_manager เข้ากับ task เพื่อให้ทำงานเมื่อ task เสร็จสมบูรณ์
    task.add_done_callback(alert_manager)
    
    await task # รอให้ Task ทำงานจนเสร็จ

asyncio.run(main())