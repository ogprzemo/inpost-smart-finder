from fastapi import APIRouter
import httpx

router = APIRouter()


@router.get("/external-points")
async def get_external_points():
    url = "https://api-global-points.easypack24.net/v1/points"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    return response.json()