#!/bin/bash

echo "INICIANDO ENTRYPOINT"
cd /app
git clone https://github.com/lips1982/bspfy-main.git
mv /app/bspfy-main/botSpotifyV1/* /app/
rm -R /app/bspfy-main
ls -la
cd /usr/bin/ 
ls -la
cd /app/
echo "FINALIZANDO ENTRYPOINT"
clear 
ls -la
exec "$@"