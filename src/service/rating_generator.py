import ast
import logging
import sys

import aiohttp


async def query_rating(movie_title: str, config, proxy=None) -> None:
    """
    Queries OMDB api endpoint for Rotten Tomato rating
    """
    api_url = config.get_property("ombd", "api")
    api_key = config.get_property("ombd", "api_key")
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{api_url}{api_key}&t={prepare_movie_title(movie_title)}&r=json", proxy=proxy
        ) as resp:
            status_code = resp.status
            if status_code != 200:
                logging.error(f"Error querying api. Response code : {status_code}")
            else:
                logging.info(f"Success querying api!")
                resp = await resp.text()
                movie = " ".join(movie_title)
                print(
                    f"--> Rotten Tomatoes rate of movie: {movie.upper()} is {get_rotten_tomatoes_rate(resp, movie_title)}"
                )


def prepare_movie_title(movie_title) -> str:
    """
    Prepares movie title - in case of multiword titles
    """
    if len(movie_title) > 1:
        delim = "+"
        return delim.join(movie_title)
    else:
        return movie_title[0]


def get_rotten_tomatoes_rate(movie_info, movie_title) -> str:
    """
    Extracts rating from response payload
    """
    resp = ast.literal_eval(movie_info)
    try:
        if resp["Ratings"][1]["Source"] == "Rotten Tomatoes":
            return resp["Ratings"][1]["Value"]
        else:
            sys.exit("Api response does not contain queried data. Exiting")
    except IndexError:
        movie = " ".join(movie_title)
        sys.exit(f"No Rotten Tomatoes rating found for movie {movie}.")
    except (AttributeError, KeyError):
        sys.exit("Api response currently does not contain queried data. Exiting")
