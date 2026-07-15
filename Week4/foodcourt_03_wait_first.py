import asyncio
from time import ctime, time
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301008"
    
    print(f"{ctime()} | --- [Task 3] Practice using wait (FIRST_COMPLETED) ---")
    start_time = time()
    
    # Create tasks as asyncio Tasks explicitly to allow cancellation later
    task1 = asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice Thigh"))
    task2 = asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "noodle", "Wonton Noodles"))
    task3 = asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "steak", "Sizzling Steak"))
    
    # 1. Wait for the FIRST_COMPLETED task
    done, pending = await asyncio.wait(
        [task1, task2, task3],
        return_when=asyncio.FIRST_COMPLETED
    )
    
    # 2. Get the winner result
    winner_task = done.pop()
    result = winner_task.result()
    shop = result.get('shop', 'unknown')
    menu = result.get('menu', 'unknown')
    
    print(f"{ctime()} | Winner served dish: Shop: {shop} | Menu: {menu}")
    
    # 3. Cancel remaining pending tasks
    print(f"{ctime()} | Cleaning up: Canceling {len(pending)} remaining pending orders...")
    for task in pending:
        task.cancel()
        
    end_time = time()
    elapsed = end_time - start_time
    print(f"{ctime()} | Total waiting time for the first dish: {elapsed:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())
