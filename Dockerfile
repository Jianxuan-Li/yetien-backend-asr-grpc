ARG PROJECT_PATH=/app

FROM docker.io/freeyeti/dev-in-docker:pyinstaller5.8.0-poetry1.4.0 AS poetry

ARG PROJECT_PATH
RUN mkdir -p $PROJECT_PATH
WORKDIR $PROJECT_PATH
COPY . .

RUN poetry export --output requirements.txt

FROM docker.io/python:3.10.12-bookworm AS python3

ARG PROJECT_PATH

RUN mkdir -p $PROJECT_PATH
WORKDIR $PROJECT_PATH
COPY . .

COPY --from=poetry $PROJECT_PATH/requirements.txt ./

RUN yes | pip3 install --no-cache-dir -r requirements.txt

COPY ./docker/docker-entrypoint ./
COPY ./docker/test-in-container.sh ./

RUN chmod +x ./docker-entrypoint
RUN chmod +x ./test-in-container.sh

EXPOSE 9000

CMD [ "./docker-entrypoint" ]
