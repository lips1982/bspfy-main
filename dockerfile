FROM python:3.10.6-slim-bullseye

WORKDIR /app

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
    git \
    curl\
    xvfb xserver-xephyr xauth python3-tk python3-dev \
    ca-certificates scrot \
    xz-utils \
    sshpass \
    unzip wget gpg && \
    wget -P /root/ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get -y install -f /root/google-chrome*.deb && \
    wget -P /root/ https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip && \
    unzip /root/chromedriver_linux64.zip -d /root/ && \
    mv /root/chromedriver /usr/bin/ && \
    rm -rf /var/lib/apt/lists/*

RUN curl -o /app/requerimientosNeverinstall.txt https://raw.githubusercontent.com/lips1982/bspfy-main/main/botSpotifyV1/requerimientosNeverinstall.txt

ADD ./data-dir1.tar.xz ./opt/
RUN pip3 install -r requerimientosNeverinstall.txt

#-> Entrypoint
COPY $PWD/entrypoint.sh /srv/
RUN chmod +x /srv/entrypoint.sh
ENTRYPOINT ["/srv/entrypoint.sh"]

CMD ["bash", "-c", "python3 mainNeverInstall.py"]

#CMD ["bash", "-c", "Xvfb :5 -ac & export DISPLAY=:5 ; python3 mainNeverInstall.py"]

