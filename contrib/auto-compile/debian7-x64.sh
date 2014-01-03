#!/bin/bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install -y git-core
sudo apt-get install -y build-essential autotools-dev autoconf
sudo apt-get install -y libtool libssl-dev libminiupnpc-dev libdb5.1++-dev libboost1.49-dev
git clone https://github.com/bitcoin/bitcoin.git
cd bitcoin/
./autogen.sh
./configure
make