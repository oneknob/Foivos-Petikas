#!/bin/bash

echo "Installing Homebrew..."
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo "Homebrew installed."

echo "Installing Python 3.8..."
brew install python@3.8 > /dev/null
echo "Python 3.8 installed."

echo "Installing ttkbootstrap..."
pip3 install ttkbootstrap > /dev/null
echo "ttkbootstrap installed."

echo "Installing NumPy..."
pip3 install numpy > /dev/null
echo "NumPy installed."

echo "Installing Matplotlib..."
pip3 install matplotlib > /dev/null
echo "Matplotlib installed."

echo "Installing Pillow..."
pip3 install pillow > /dev/null
echo "Pillow installed."

echo "Installing Pandas..."
pip3 install pandas > /dev/null
echo "Pandas installed."

echo "Upgrading pip..."
pip3 install --upgrade pip > /dev/null
echo "pip upgraded."

echo "Installing NotoSansJP-VariableFont_wght.ttf font..."
brew install --cask font-noto-sans-cjk-jp > /dev/null
echo "NotoSansJP-VariableFont_wght.ttf font installed."

echo "All installations complete."
