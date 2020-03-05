import asyncio
import nest_asyncio

nest_asyncio.apply()

def sync(coro):
    r"""
        need to call async func from a sync func inside an event loop
        This will block the event loop ¯\_(ツ)_/¯
    """
    return asyncio.run(coro)
