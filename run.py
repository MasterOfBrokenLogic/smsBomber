import sys
import os
import asyncio

# add project root to python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from bot.main import main

if __name__ == "__main__":
    asyncio.run(main())