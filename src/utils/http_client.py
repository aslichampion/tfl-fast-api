import httpx
from src.core.config import settings

httpx_client = httpx.AsyncClient(
    timeout=10.0,
    headers={"app_key": settings.TRACKERNET_API_KEY},
)
