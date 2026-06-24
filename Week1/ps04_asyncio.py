from time import ctime, time, process_time
import asyncio
import os
import threading
import psutil

# ฟังก์ชันจำลองการทำกาแฟแบบ Asynchronous
async def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    

    current_task = asyncio.current_task()
    task_name = current_task.get_name() # ชื่อ Task
    

    task_id = id(current_task)
    
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Async Task ID: {task_id}] [Task Name: {task_name}] กำลังชงกาแฟให้ ลูกค้า {customer_name}...")
    sum(i * i for i in range(1000000))

    await asyncio.sleep(5)
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Async Task ID: {task_id}] [Task Name: {task_name}] ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

async def main():
    queue = ['A', 'B', 'C']
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id
    
    print(f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] === เริ่มระบบจำลองตู้กาแฟแบบ asyncio ===")
    start_time = time()
    start_cpu = process_time()
    
    tasks = []
    for customer in queue:

        coro = make_coffee(customer)

        task = asyncio.create_task(coro, name=f"Task-{customer}")
        tasks.append(task)
        

    await asyncio.gather(*tasks)
    
    duration = time() - start_time
    cpu_duration = process_time() - start_cpu
    
    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 * 1024)
    
    print(f"[สรุปผล Asuncio]")
    print(f"เวลาที่ใช้จริง (Wall Time): {duration:.02f} วินาที")
    print(f"เวลาที่ CPU ใช้ประมวลผลจริง (CPU Time): {cpu_duration:.04f} วินาที")
    print(f"ทรัพยากร Memory (RAM) ที่ใช้: {mem_mb:.02f} MB")

if __name__ == "__main__":
    asyncio.run(main())