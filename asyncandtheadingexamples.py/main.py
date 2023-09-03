from collections.abc import Callable, Iterable, Mapping
import time
import asyncio
from typing import Any
import requests
import aiohttp
import threading

def get_data_sync(urls):
    st = time.time()
    json_array = []
    for url in urls:
        json_array.append(requests.get(url).json())
    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
    return json_array

class ThreadingDowlander(threading.Thread):
    def __init__(self):
        super.__init__()
           
    def run(self):
        response = requests.get("")
        self.json_array.append(response)
        return response.json()


urls = ['https://postman-echo.com/delay/3'] * 10
#get_data_sync(urls) #42 seconds
#asyncio.run(get_data_async_but_as_wrapper(urls)) #34 seconds
#asyncio.run(get_data_async_concurrently(urls)) #4 seconds
#get_data_threading(urls) # 4 seconds