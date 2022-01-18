import asyncio

# async def main():
#     print('tim')
#     task = asyncio.create_task(foo('text'))
#     await asyncio.sleep(1)
#     print('finished')

# async def foo(text):
#     print(text)
#     await asyncio.sleep(1)

async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data' : 1}

async def printd_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(printd_numbers())

    value = await task1
    value = await task2
    print(value)

asyncio.run(main())