# import asyncio


# def foo():
#     return


# foo()
# print("nishi")


# Coroutines

# import asyncio


# async def main():
#     print("nishi")
#     # await foo("text")
#     task = asyncio.create_task(foo("text"))
#     await task  # if it is there finished will be print afterwards
#     # await asyncio.sleep(2)
#     await asyncio.sleep(0.5)

#     print("finished")


# async def foo(text):
#     print(text)
#     await asyncio.sleep(10)


# asyncio.run(main())

# Async Event-Loop
# Async/Await Keywords
# Tasks


# Async Example


import asyncio

#  User can only use await inside of async function. Adding in the event loop can be done by tasks.

# “stackless” and “stackful” coroutines. Python has the “stackless” kind, which is why the await keyword can only be used in the top level of an async-function, not anywhere else.
async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2)
    print("done fetching")
    return {"data": 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)


async def main():
    task2 = asyncio.create_task(print_numbers())
    await fetch_data()
    # task1 = asyncio.create_task(fetch_data())

    # value = await task1
    # print(value)
    await task2


asyncio.run(main())
