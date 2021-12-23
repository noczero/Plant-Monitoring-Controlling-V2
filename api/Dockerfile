# temp stage
FROM python:3.9-buster as builder
WORKDIR /api
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /api/wheels -r requirements.txt

# final stage
FROM python:3.9-slim-buster
COPY . /api/api

ENV PYTHONPATH=/api
WORKDIR /api

COPY --from=builder /api/wheels /wheels
COPY --from=builder /api/requirements.txt .

RUN pip install --no-cache /wheels/*

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["api.app:app", "--host", "0.0.0.0", "--reload"]
