import asyncio
from time import ctime, time
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301008"
    
    print(f"{ctime()} | --- [Task 5] Advanced Practice: Mixing concepts together ---")
    start_time = time()
    
    try:
        # Standard task for noodles
        noodle_task = asyncio.create_task(
            send_order_to_kitchen(MY_STUDENT_ID, "noodle", "Egg Noodles")
        )
        
        # Chicken rice task with a strict 1.0s timeout limit
        chicken_task = asyncio.create_task(
            asyncio.wait_for(
                send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice Special"), 
                timeout=1.0
            )
        )
        
        # Resolve both tasks concurrently using gather
        results = await asyncio.gather(noodle_task, chicken_task)
        
        print(f"{ctime()} | Success: All food served on time! Received {len(results)} dishes.")
    except (asyncio.TimeoutError, TimeoutError):
        print(f"{ctime()} | Error: A dish timed out!")
        
    end_time = time()
    elapsed = end_time - start_time
    print(f"{ctime()} | Total elapsed time: {elapsed:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())
