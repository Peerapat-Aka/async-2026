# วัตถุประสงค์: เปรียบเทียบความแตกต่างทางโครงสร้างและกลไกของทั้งสองวิธี (gather และ wait) ในสถานการณ์จำลองการแข่งขัน
import asyncio
from time import ctime

async def runner(name, speed):
    await asyncio.sleep(speed)
    return f"{name} crossed line!"

async def main():
    # แบบแรก: ใช้ gather() - เป็นการรวบรวมข้อมูลแบบครบวงจร
    print(f"{ctime()} --- Starting gather() approach (Unified Aggregation) ---")
    all_finishes = await asyncio.gather(runner("A", 0.5), runner("B", 2.0))
    print(f"{ctime()} Gather output: {all_finishes}\n")
    
    # แบบสอง: ใช้ wait() - เพื่อควบคุมสถานะหรือการแข่งขัน (หาผู้ชนะ)
    print(f"{ctime()} --- Starting wait() approach (State control / Racing) ---")
    active_tasks = {asyncio.create_task(runner("A", 0.5)), asyncio.create_task(runner("B", 2.0))}
    
    done, pending = await asyncio.wait(active_tasks, return_when=asyncio.FIRST_COMPLETED)
    print(f"{ctime()} Wait output: The winner of the race is -> {list(done)[0].result()}")
    
    # ยกเลิกงานของคนที่แพ้การแข่งขัน (ที่ยังวิ่งไม่เสร็จ)
    for t in pending:
        t.cancel()

asyncio.run(main())