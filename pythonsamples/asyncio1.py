import asyncio
import time
async def hello_world():
    print("Hello World!")
    #time.sleep(5)
    return 'vikas'

loop = asyncio.get_event_loop()

# Blocking call which returns when the hello_world() coroutine is done
name = loop.run_until_complete(hello_world())
print("hi", name)
loop.close()