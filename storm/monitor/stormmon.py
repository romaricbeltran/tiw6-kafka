#!/usr/bin/env python3

import asyncio
import sys


async def handle_client(reader, writer):
    request = None
    try:
        while not reader.at_eof():
            request = (await reader.readline()).decode("utf8")
            print(str(request))
    except:
        print("Erreur lors de la lecture des données")
    finally:
        writer.close()


port = 12345
args = sys.argv
if len(args) > 1:
    if args[1] == "-h":
        print("Usage: {} [port]".format(args[0]))
        sys.exit(0)
    else:
        port = int(args[1])
print("Listening on port {}".format(port))
loop = asyncio.get_event_loop()
loop.create_task(asyncio.start_server(handle_client, None, port))
loop.run_forever()
