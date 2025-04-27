#!/bin/bash

set -e

echo " Deploy mulai..."

# Pastikan docker dan docker compose tersedia
if ! command -v docker &> /dev/null
then
    echo "Docker tidak ditemukan, install dulu!"
    sudo apt-get update
    sudo apt-get install -y docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
fi

if ! command -v docker-compose &> /dev/null
then
    echo "Docker Compose tidak ditemukan, install dulu!"
    sudo apt-get install -y docker-compose
fi

# Pindah ke folder project
cd /home/ubuntu/webapps/website

echo " Jalankan docker compose up -d ..."
sudo docker-compose up -d

echo " Deploy sukses!" 