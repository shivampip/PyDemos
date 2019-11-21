import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    print("main Start")
    await asyncio.gather(count(), count(), count())
    print("main End")

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.new_event_loop().run_until_complete(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")