FROM debian:bullseye
COPY ./flat_finder ./flat_finder
COPY main.py .
COPY poetry.lock .
COPY pyproject.toml .

RUN apt update && apt upgrade -y
RUN apt -y install python3 pip
#RUN curl http://ftp.de.debian.org/debian/pool/main/c/chromium/chromium_108.0.5359.124-1_arm64.deb --output chrome.deb
#RUN sudo apt install ./chrome.deb

#RUN curl -sSL https://install.python-poetry.org | python3 -
#ENV PATH = "${PATH}:$HOME/.poetry/bin:$PATH"
#RUN source $HOME/.poetry/env
RUN pip3 install --user poetry
ENV PATH="${PATH}:/root/.local/bin"
#ENV POETRY_HOME="/opt/poetry" \
#    POETRY_VIRTUALENVS_CREATE=false \
#    POETRY_VIRTUALENVS_IN_PROJECT=false \
#    POETRY_NO_INTERACTION=1 \
#    POETRY_VERSION=1.1.14
#ENV PATH="$PATH:$POETRY_HOME/bin"
RUN poetry install --no-dev

#CMD ["chromium-browser", "--product-version"]

CMD ["poetry", "run", "python", "-u", "main.py", "--config_path", "/conf"]