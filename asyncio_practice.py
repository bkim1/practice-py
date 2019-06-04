import asyncio
import aiohttp

WP_URL = 'http://18.219.114.43/wp-json/wp/v2/posts' \
         '?slug=bc-accepts-27-percent-of-2022-applicants'


async def load_info(session, url):
    async with session.get(url) as response:
        text = await response.json()
        post = text[0]
        title = post['title']['rendered']
        print('Hi')
        await asyncio.sleep(0.5)
        return title


async def other_func():
    print('Other func!')


async def main():
    async with aiohttp.ClientSession() as session:
        print('Starting call!')
        html = await load_info(session, WP_URL)
        await other_func()
        print(html)
        print('Test end!')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
