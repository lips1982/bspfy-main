FROM python:3.9-slim-bullseye

WORKDIR /app

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
    git \
    xvfb xserver-xephyr xauth python3-tk python3-dev \
    ca-certificates scrot \
    xz-utils \
    sshpass \
    apt-get clean \

#RUN chromium chromium-driver
RUN apt-get -y install unzip wget gpg && \
    wget -P /root/ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get -y install -f /root/google-chrome*.deb && \
    wget -P /root/ https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip && \
    unzip /root/chromedriver_linux64.zip -d /root/ && \
    mv /root/chromedriver /usr/bin/ \
    apt-get clean

RUN rm -rf /var/lib/apt/lists/*

#ADD ./data-dir.tar.xz ./opt/
COPY /botSpotifyV1/requerimientosNeverinstall.txt ./requerimientosNeverinstall.txt

RUN pip3 install -r requerimientosNeverinstall.txt

#RUN sed -i 's%exec $LIBDIR/$APPNAME $CHROMIUM_FLAGS "$@"%exec $LIBDIR/$APPNAME $CHROMIUM_FLAGS "$@" --no-sandbox%g' "/usr/bin/chromium"

COPY /botSpotifyV1 .

#CMD ["bash", "-c", "Xvfb :5 -ac & export DISPLAY=:5 ; python3 mainNeverInstall.py"]
CMD ["bash", "-c", "python3 mainNeverInstall.py"]

# docker build -t display .
# docker run -it --rm -v $PWD/img:/app/Almacenamiento/img display

# docker build -t display . && docker run -it --rm -v $PWD/img:/app/Almacenamiento/img display


# docker build -t display .

# docker run -it --rm -v $PWD/data-dir:/app/Almacenamiento/img -v /tmp/.X11-unix:/tmp/.X11-unix --net=host -e DISPLAY=$DISPLAY display
# docker run -it --rm -v $PWD/app:/app -v /tmp/.X11-unix:/tmp/.X11-unix --net=host -e DISPLAY=$DISPLAY display

#sudo docker run -it --rm -v $PWD/data-dir:/app/opt/data-dir -v /tmp/.X11-unix:/tmp/.X11-unix --net=host -e DISPLAY=$DISPLAY display04


#sudo docker run -it --rm -v $PWD/img:/app/opt/ -v /tmp/.X11-unix:/tmp/.X11-unix --net=host -e DISPLAY=$DISPLAY display01