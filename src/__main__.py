import asyncio
import logging
import sys

from .configuration import config as config
from .service.rating_generator import query_rating

logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO)

config = config.read_config()


if __name__ == "__main__":
    logging.warning(
        "You are currently using script author's OMDB api key. Please, generate your own api key and paste it into config.ini file"
        "This one is only for demonstration purposes"
    )
    if len(sys.argv) > 1:
        movie = sys.argv[1:]
        loop = asyncio.get_event_loop()
        # TODO use proxy based on jenkins job's parameter
        loop.run_until_complete(query_rating(movie, config=config))
    else:
        sys.exit("Movie title must be provided")
