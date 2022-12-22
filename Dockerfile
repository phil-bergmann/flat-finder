FROM debian:bullseye
COPY ./flat_finder ./flat_finder
COPY main.py .
COPY poetry.lock .
COPY pyproject.toml .

RUN apt update && apt upgrade -y
RUN apt -y install python3 pip
RUN pip3 install --user poetry
ENV PATH="${PATH}:/root/.local/bin"
RUN poetry install --no-dev

CMD ["poetry", "run", "python", "-u", "main.py", "--config_path", "/conf"]