import os
import asyncio
from uploadthing_py import UTApi

async def main():
    utapi = UTApi(os.getenv("UPLOADTHING_SECRET"))
    files = await utapi.list_files()
    print(files)

asyncio.run(main())