#!/bin/sh
poetry install
poetry run coverage run ./test.py
poetry run coverage report
