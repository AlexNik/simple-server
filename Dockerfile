FROM python:alpine as compile

# hadolint ignore=DL3013,DL3018
RUN apk add --no-cache binutils && \
    pip install --no-cache-dir pyinstaller

COPY main.py /main.py

RUN pyinstaller --onefile main.py --paths "$(python -m site --user-site)"

FROM alpine:3.16.0

ENTRYPOINT ["/main"]
EXPOSE 8000

COPY --from=compile /dist/main /
