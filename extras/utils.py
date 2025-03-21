import asyncio

# Example utility function for async delays
async def wait_and_print(message, delay=2):
    await asyncio.sleep(delay)
    print(message)