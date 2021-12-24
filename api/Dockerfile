# temp stage
#FROM python:3.9-buster as builder
#WORKDIR /api
#COPY requirements.txt .
#RUN pip wheel --no-cache-dir --no-deps --wheel-dir /api/wheels -r requirements.txt

# final stage
FROM arm32v7/python:3.9-buster
COPY . /api/api

ENV PYTHONPATH=/api
WORKDIR /api

#COPY --from=builder /api/wheels /wheels
#COPY --from=builder /api/requirements.txt .
COPY requirements.txt .

RUN pip install --no-cache -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["api.app:app", "--host", "0.0.0.0", "--reload"]
