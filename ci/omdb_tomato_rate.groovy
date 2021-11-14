REPOSITORY_URL="Your team's repo url"
JOB_NODE_LABEL="ombd-cloud"
IMAGE_NAME="Image name defined during build process"
TAG="Tag, according to Your way  of tagging"

def ViewJob() {
    listView("OMDB-tomato-rate") {
        description("OMDB query api for Rotten Tomato rating of a movie")
        filterBuildQueue()
        filterExecutors()
    }
}

def OMDBJob() {
    job("OMDB_ROTTEN_TOMATO") {
        disabled()
        description("OMDB query api for Rotten Tomato rating of a movie")
        logRotator {
            numToKeep(50)
        }
        label("${JOB_NODE_LABEL}")
        parameters {
            stringParam("MOVIE", "Movie title")
            stringParam("proxy", "Proxy address")
        }
        steps {
            shell"""#!/usr/bin/bash

docker pull \$REPOSITORY_URL/\$IMAGE_NAME:\$TAG

docker run \$REPOSITORY_URL/\$IMAGE_NAME \$MOVIE
"""
        }
    }
}