from app.core.http_client import InPostClient
from app.repositories.points_repo import PointsRepo
from app.models.point import Point


class SyncService:
    def __init__(self):
        self.client = InPostClient()
        self.repo = PointsRepo()

    async def sync_all(self):
        page = 1
        all_points = []

        while True:
            data = await self.client.get_points(page)
            items = data.get("items", [])

            if not items:
                break

            for item in items:
                all_points.append(
                    Point(
                        id=item.get("id"),
                        name=item.get("name"),
                        latitude=item.get("latitude"),
                        longitude=item.get("longitude"),
                        city=item.get("address_details", {}).get("city")
                    )
                )

            if not data.get("meta", {}).get("next_page"):
                break

            page += 1

        self.repo.save_many(all_points)
        return {"saved": len(all_points)}