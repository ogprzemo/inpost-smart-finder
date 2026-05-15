from app.core.http_client import InPostClient


class PointsService:
    def __init__(self):
        self.client = InPostClient()

    async def fetch_all_points(self):
        page = 1
        all_points = []

        while True:
            data = await self.client.get_points(page)

            items = data.get("items", [])
            if not items:
                break

            all_points.extend(items)

            meta = data.get("meta", {})
            if not meta.get("next_page"):
                break

            page += 1

        return all_points