#!/usr/bin/env bash
docker build -f ./tests/Dockerfile --tag cache_metrics_tests .
docker run --rm \
    -v $PWD/config-example.json:/etc/config.json \
    cache_metrics_tests
