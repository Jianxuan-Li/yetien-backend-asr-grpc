#!/bin/sh
mkdir -p /data/logs
mkdir -p /data/cache

poetry install
poetry run python test.py
poetry run coverage report
