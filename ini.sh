#!/bin/bash
clear
echo "INICIANDO"
#sudo service docker stop

while getopts "a:b:c:" opt; do
  case $opt in
    a) param1="$OPTARG";;
    b) param2="$OPTARG";;
    c) param3="$OPTARG";;
    \?) echo "Opción inválida: -$OPTARG";;
  esac
done

echo "Nombre imagen: $param1"
echo "Datadir: $param2"
echo "Parámetro 3: $param3"
#sed -i "s|SERVERNAME|${SERVERNAME}|g" daemon.json
#sudo cp -f daemon.json /etc/docker/
#sudo service docker start

PUBLIC_IP=`wget http://ipecho.net/plain -O - -q ; echo`
echo "$PUBLIC_IP"

sed -i "s|REEMPLAZARPUBLICIP|${PUBLIC_IP}|g" botSpotifyV1/mainNeverInstall.py
#sudo apt-get -y install screen

sudo docker build -t ${param1} . 

screen -S docker -d -m bash -c "docker run -it --rm -v $PWD/img:/app/Almacenamiento/img display bash" 
#docker logs -f 
