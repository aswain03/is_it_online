import asyncio
import aiohttp
from http.client import HTTPConnection
from urllib.parse import urlparse


def is_online(url, timeout=5):
    err = Exception("unknown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443):
        conn = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            conn.request("HEAD", "/")
            return True
        except Exception as e:
            err = e
        finally:
            conn.close()
    raise err


async def is_online_async(url, timeout=5):
    err = Exception("unknown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for scheme in ("http", "https"):
        url = scheme + "://" + host
        async with aiohttp.ClientSession() as session:
            try:
                await session.head(url, timeout=timeout)
                return True
            except asyncio.exceptions.TimeoutError as e:
                err = Exception(f"Timeout: {e}")
            except Exception as e:
                err = e
    raise err
