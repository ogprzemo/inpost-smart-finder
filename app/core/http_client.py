import httpx
from app.core.config import settings


class InPostClient:
    async def get_points(self, page: int = 1):
        async with httpx.AsyncClient(timeout=20) as client:
            r = await client.get(
                settings.INPOST_API_URL,
                params={"page": page}
            )
            r.raise_for_status()
            return r.json()