## Шпаргалка

Установка актуальной версии:
```bash
sudo apt update

sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev

wget https://www.python.org/ftp/python/3.10.*/Python-3.10.*.tgz

tar -xvf Python-3.10.*.tgz

cd Python-3.10.*

sudo ./configure --enable-optimizations --prefix=/home/user_name/.python3.10.*

make -j 2

sudo make altinstall

vi ~/.bashrc
export PATH=$PATH:/home/username/.python3.10.*/bin/
source ~/.bashrc
```