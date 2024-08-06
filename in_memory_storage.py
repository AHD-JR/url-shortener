from url_repo_interface import UrlRepoInterface

class Inmemory_storage(UrlRepoInterface):
    def __init__(self):
        self.url_dict = {}

    async def save(self, short_id: str, long_url: str) -> None:
        self.url_dict[short_id] = long_url
        print(self.url_dict)

    async def get(self, short_id: str) -> str | None:
        return self.url_dict.get(short_id)