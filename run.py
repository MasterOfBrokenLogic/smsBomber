import sys
import os

# Must be set BEFORE any bot imports so helpers/apis are findable
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import asyncio
from bot.main import main

if __name__ == "__main__":
    asyncio.run(main())