FROM --platform=${TARGETPLATFORM:-linux/amd64} ghcr.io/openfaas/classic-watchdog:0.2.1 as watchdog
FROM --platform=${TARGETPLATFORM:-linux/amd64} python:3.10-slim
ARG TARGETPLATFORM
ARG BUILDPLATFORM
COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog
# Add non root user
RUN groupadd app && useradd -r -g app app

WORKDIR /home/app/

COPY index.py           .
COPY requirements.txt   .
RUN chown -R app /home/app && \
    mkdir -p /home/app/python && chown -R app /home/app
USER app
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
ENV PATH=$PATH:/home/app/.local/bin:/home/app/python/bin/
ENV PYTHONPATH=$PYTHONPATH:/home/app/python
RUN pip --no-cache-dir install -r requirements.txt --target=/home/app/python
RUN mkdir -p function
RUN touch ./function/__init__.py
WORKDIR /home/app/function/
COPY function/requirements.txt	.
RUN pip --no-cache-dir install onnxruntime orjson requests --target=/home/app/python 
RUN pip --no-cache-dir install -r requirements.txt --target=/home/app/python 
RUN find /home/app/ -name '*.pyc' -delete


WORKDIR /home/app/

USER root
RUN apt-get autoclean
COPY function           function
# Allow any user-id for OpenShift users.
RUN chown -R app:app ./ && \
    chmod -R 777 /home/app/python

USER app

ENV fprocess="python3 index.py"
EXPOSE 8080

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
