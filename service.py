from url_repo_interface import UrlRepoInterface
from model import URLRequest
import string
import random

class UrlShortnerService:
    def __init__(self, repo: UrlRepoInterface):
         self.repo = repo


    def _generate_short_id(self, count: int, length: int = 7):
        # count is gotten from zookeeper
        # count is in base10, we should convert it to base62[a-z,A-Z,0-9]
        # devide the base10 number by the 62, taking the ascii rep of the remender to form the 7 digits short_id
        chars = string.ascii_letters + string.digits
        base = len(chars) # 62

        if count == 0:
            return chars[0] * length

        short_id = []
        while count > 0:
            remender = count % base
            short_id.append(chars[remender])
            count //= base

        # Reverse the short_id and pad with the first character to ensure it is the correct length
        short_id = ''.join(reversed(short_id)).rjust(length, chars[0])

        return short_id


    async def shorten_url(self, url: URLRequest):
        short_id = self._generate_short_id(random.randint(0, 999_999)) 
        await self.repo.save(short_id, url)
        return short_id
    

    async def get_long_url(self, short_id: str):
        return await self.repo.get(short_id)