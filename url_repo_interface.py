from abc import ABC, abstractmethod
from typing import Optional

class UrlRepoInterface(ABC):
    @abstractmethod
    async def save(self, short_id: str, long_url: str)  -> None:
        pass

    @abstractmethod
    async def get(self, short_id: str) -> Optional[str]:
        pass
