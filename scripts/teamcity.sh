#!/usr/bin/env bash
HERE=${BASH_SOURCE%/*}
$HERE/test.sh

GIT_ID=$(git rev-parse --short=7 HEAD)
GIT_BRANCH=$(git symbolic-ref --short HEAD)
REGISTRY=docker.montagu.dide.ic.ac.uk:5000
NAME=cached-metrics

APP_DOCKER_COMMIT_TAG=$REGISTRY/$NAME:$GIT_ID
APP_DOCKER_BRANCH_TAG=$REGISTRY/$NAME:$GIT_BRANCH

docker build \
       --tag $APP_DOCKER_COMMIT_TAG \
       --tag $APP_DOCKER_BRANCH_TAG \
       .

docker push $APP_DOCKER_BRANCH_TAG
docker push $APP_DOCKER_COMMIT_TAG