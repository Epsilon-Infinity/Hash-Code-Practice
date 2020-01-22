#!/usr/bin/bash

set -e
# set -x

# Install dependencies
sudo apt-get install -y git pkg-config coinor-libcbc-dev coinor-libosi-dev coinor-libcoinutils-dev coinor-libcgl-dev

# This file is required by the Cylp installer (not present in standard coinor-libcbc-dev package of all debian version)
CBC_ADDLIBS="/usr/share/coin/doc/Cbc/cbc_addlibs.txt"

# If it does not exist,
if [[ ! (-f "$CBC_ADDLIBS") ]]; then

    # Clone the Cbc repository
    if [[ ! (-d "Cbc/") ]]; then
        git clone https://github.com/coin-or/Cbc.git Cbc/
    fi

    # Go into the directory 
    cd Cbc/

    # Go to the same version as the one in the official repositories
    git checkout releases/`pkg-config --modversion cbc`

    # Configure and install (in the current directory) the library
    ./configure -C
    make
    make install

    # Create a symlink in the default system folder
    sudo ln -s "$(pwd)/share/coin/doc/Cbc/cbc_addlibs.txt" "$CBC_ADDLIBS"
fi


echo
echo "----------------------------------"
echo "In order to install CyLP, please use the following command in you Python virtual environment:"
echo
echo "COIN_INSTALL_DIR=/usr/ pip install --pre cylp"
echo
echo "----------------------------------"
echo

exit 0
