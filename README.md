# omdb-rotten-tomatoes



## Basic usage

To query for the movie's Rotten Tomato rating, in root directory simply run in unix shell:

```
python3 -m src <movie_title>
```

Rating should be returned to stdout.

## Dockerization

To build docker image, in root directory run:

```
docker build . -t <image_name>
```

## Integrate with your tools

In "ci" directory, there is dsl file written in Groovy, which generates Jenkins View and
Job, which could be used to distribute this tool among team users.

When generated, this job accepts single string parameter named MOVIE, and executes shell
script. In logs, Rotten Tomato rating of a movie should be visible.

## Further development

One of the things that should be considered is using this tool behind (corporate)
proxy. Some sort of proxy usage mechanism should be implemented - there is proxy definition in config.ini file,
as it could be done this way.  