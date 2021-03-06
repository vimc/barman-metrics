#!/usr/bin/env bash
HERE=${BASH_SOURCE%/*}
$HERE/test.sh

GIT_ID=$(git rev-parse --short=7 HEAD)
GIT_BRANCH=$(git symbolic-ref --short HEAD)
REGISTRY=docker.montagu.dide.ic.ac.uk:5000
PUBLIC_REGISTRY=vimc
NAME=cached-metrics

APP_DOCKER_COMMIT_TAG=$REGISTRY/$NAME:$GIT_ID
APP_DOCKER_BRANCH_TAG=$REGISTRY/$NAME:$GIT_BRANCH

docker build \
       --tag $APP_DOCKER_COMMIT_TAG \
       --tag $APP_DOCKER_BRANCH_TAG \
       .

docker push $APP_DOCKER_BRANCH_TAG
docker push $APP_DOCKER_COMMIT_TAG

if [[ $GIT_BRANCH == "master" ]]; then
    PUBLIC_TAG=$PUBLIC_REGISTRY/$NAME:master
    docker tag $APP_DOCKER_BRANCH_TAG $PUBLIC_TAG
    docker push $PUBLIC_TAG
fi