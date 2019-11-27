import asyncio
import aiohttp
import json
import signal 
import sys 
import time 

loop= asyncio.get_event_loop()
client= aiohttp.ClientSession(loop= loop)


async def get_json(client, url):
    async with client.get(url) as response:
        assert response.status== 200
        return await response.read()


async def get_raddit_top(subreddit, client):
    print("\nGet Retting for {}\n".format(subreddit))
    data= await get_json(client, 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')

    jdata= json.loads(data.decode('utf-8'))
    for i in jdata['data']['children']:
        time.sleep(.7)
        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        print(subreddit+">> "+str(score) + ': ' + title + ' (' + link + ')')
    print('DONE:', subreddit + '\n')


def signal_handler(sig, frame):
    print("\nSTOPPING\n")
    loop.stop()
    client.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


asyncio.ensure_future(get_raddit_top("python", client))
asyncio.ensure_future(get_raddit_top("programming", client))
asyncio.ensure_future(get_raddit_top("compsci", client))

print("Starting run forever")
loop.run_forever()
print("After forever")













