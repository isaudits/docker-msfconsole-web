FROM tsl0922/ttyd

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install pymetasploit3 python-dotenv

COPY entrypoint.py /opt/entrypoint.py

ENTRYPOINT ["/opt/entrypoint.py"]