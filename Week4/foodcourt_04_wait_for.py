import asyncio
from time import ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301008"
    
    print(f"{ctime()} | --- [Task 4] Practice using wait_for to handle timeouts ---")
    
    task = send_order_to_kitchen(MY_STUDENT_ID, "steak", "Sizzling Steak")
    print(f"{ctime()} | [System] Order sent. Monitoring 2.0s timeout limit...")
    
    try:
        # บังคับกำหนดเวลาสูงสุด (hard timeout) ที่ 2.0 วินาที
        result = await asyncio.wait_for(task, timeout=2.0)
        print(f"{ctime()} | Meal ready: {result}")
    except (asyncio.TimeoutError, TimeoutError):
        # ใน Python 3.11 ขึ้นไป asyncio.TimeoutError คือตัวเดียวกับ TimeoutError ของระบบ
        print(f"{ctime()} | Timeout occurred: Steak took too long! Leaving the food court now.")

if __name__ == "__main__":
    asyncio.run(main())
