# check is docker is installed
if [ -x "$(command -v docker)" ]; then
    echo "Docker is already installed"
else
    echo "Installing Docker"
    sudo pacman -S docker --noconfirm
fi

sudo systemctl enable docker
sudo usermod -aG docker $USER
