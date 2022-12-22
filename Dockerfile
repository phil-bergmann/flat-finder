FROM linuxserver/rdesktop:ubuntu-xfce
COPY flat_finder .
COPY main.py .
COPY poetry.lock .
COPY pyproject.toml .

RUN sudo apt update
RUN sudo apt -y install chromium-browser

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH = "${PATH}:$HOME/.local/bin:$PATH"
RUN poetry install --no-dev

CMD python3 main.py /config