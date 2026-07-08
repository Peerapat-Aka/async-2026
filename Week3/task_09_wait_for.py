# วัตถุประสงค์: บังคับใช้กำหนดเวลา (Deadline) ที่เข้มงวดในการดำเนินการ และแจ้งข้อผิดพลาดหากเกินเวลาที่กำหนด
import asyncio
from time import ctime

async def long_query_simulation():
    print(f"{ctime()} Database: Fetching data...")
    await asyncio.sleep(5.0) # จำลองว่าใช้เวลาทำงาน 5 วินาที
    return "Heavy_Report_Data"

async def main():
    try:
        print(f"{ctime()} Main: Enforcing a strict 2-second timeout deadline...")
        # รอผลลัพธ์จากการทำงาน แต่ยอมให้รอแค่สูงสุด 2 วินาทีเท่านั้น
        result = await asyncio.wait_for(long_query_simulation(), timeout=2.0)
        print(f"{ctime()} Result acquired: {result}")
    except asyncio.TimeoutError:
        # หากทำงานเกินเวลา จะเกิด TimeoutError และ Task ย่อยจะถูกยกเลิกอัตโนมัติ
        print(f"{ctime()} Main Error Alert: Operation timed out! Task terminated.")

asyncio.run(main())