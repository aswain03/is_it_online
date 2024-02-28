import asyncio
import pathlib
import sys

from is_it_online.checker import is_online, is_online_async
from is_it_online.cli import read_args, check_result


def main():
    user_args = read_args()
    urls = _get_urls(user_args)
    if not urls:
        print("No URLs to check.", file=sys.stderr)
        sys.exit(1)
    if user_args.asynchronous:
        asyncio.run(_asynchronous_check(urls))
    else:
        _synchronous_check(urls)


def _get_urls(user_args):
    urls = user_args.urls
    if user_args.input_file:
        urls += _read_file(user_args.input_file)
    return urls


def _read_file(file):

    file_path = pathlib.Path(file)
    if file_path.is_file():
        with file_path.open() as f:
            urls = [url.strip() for url in f]
            if urls:
                return urls
            print(f"No URLs found in {file}", file=sys.stderr)
    else:
        print(f"File {file} does not exist.", file=sys.stderr)
    return []


async def _asynchronous_check(urls):
    async def _check(url):
        err = ""
        try:
            result = await is_online_async(url)
        except Exception as e:
            result = False
            err = str(e)
        check_result(result, url, err)

    await asyncio.gather(*(_check(url) for url in urls))


def _synchronous_check(urls):
    for url in urls:
        err = ""
        try:
            result = is_online(url)
        except Exception as e:
            result = False
            err = e
        check_result(result, url, err)


if __name__ == "__main__":
    main()
