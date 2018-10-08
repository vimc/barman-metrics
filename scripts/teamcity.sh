#!/usr/bin/env bash
docker build -f ./tests/Dockerfile --tag barman_metrics_tests .
docker run --rm \
    barman_metrics_tests
