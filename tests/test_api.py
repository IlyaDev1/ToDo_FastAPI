from dotenv import load_dotenv
from requests import get  # type: ignore

from app.core.config import settings
from logger import logger

load_dotenv()

main_url = f"http://localhost:{settings.APP_HOST_PORT}{settings.API_V1_STR}/task"
logger.debug(main_url)


def test_get_all_tasks():
    response = get(main_url)
    assert response.status_code == 200
