FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    pytest \
    numpy \
    pandas \
    matplotlib \
    seaborn

COPY . .

CMD ["pytest", "-v"]