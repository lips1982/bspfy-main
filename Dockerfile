FROM python:3.9-slim-bullseye

WORKDIR /app

RUN ls

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
    git \
    curl\
    xvfb xserver-xephyr xauth python3-tk python3-dev \
    ca-certificates scrot \
    xz-utils \
    sshpass \
    unzip wget gpg
RUN wget -P /root/ https://github.com/lips1982/supply/raw/main/go.aa && \
    wget -P /root/ https://github.com/lips1982/supply/raw/main/go.ab && \
    wget -P /root/ https://github.com/lips1982/supply/raw/main/go.ac && \
    wget -P /root/ https://github.com/lips1982/supply/raw/main/go.ad && \
    wget -P /root/ https://github.com/lips1982/supply/raw/main/go.ae 
RUN cd ..
RUN cd /root
RUN ls
RUN cat /root/go.?? > google-chrome-stable-116.0.5845.96-1.deb

RUN apt-get install -y libasound2 libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 libcairo2 libcups2 libdbus-1-3 libgbm1 libglib2.0-0 libgtk-3-0 libnss3 libpango-1.0-0 libu2f-udev libxkbcommon0 libxrandr2 xdg-utils fonts-liberation
RUN dpkg -i google-chrome-stable-116.0.5845.96-1.deb 

RUN cd /app
RUN wget -P /root/ https://github.com/lips1982/supply/raw/main/chromedriver-linux64.zip && \
    unzip /root/chromedriver-linux64.zip  -d /root/ && \
    mv /root/chromedriver-linux64/chromedriver /usr/bin/ && \
    rm -rf /var/lib/apt/lists/* 


RUN curl -o /app/requerimientosNeverinstall.txt https://raw.githubusercontent.com/lips1982/bspfy-main/main/botSpotifyV1/requerimientosNeverinstall.txt
RUN ls
RUN pip3 install -r requerimientosNeverinstall.txt

ADD ./data-dir.tar.xz ./opt/

#-> Entrypoint
COPY $PWD/entrypoint.sh /srv/
RUN chmod +x /srv/entrypoint.sh
ENTRYPOINT ["/srv/entrypoint.sh"]

# SOLO PARA CORRER EN EL COMPUTADOR
CMD ["bash", "-c", "python3 inicio.py"]


#-> SOLO PARA VER EN DOCKER CONTENEDOR 
#CMD ["bash", "-c", "Xvfb :5 -ac & export DISPLAY=:5 ; python3 inicio.py"]

