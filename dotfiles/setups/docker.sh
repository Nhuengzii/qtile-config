# check is docker is installed
if [ -x "$(command -v docker)" ]; then
    echo "Docker is already installed"
    sudo pacman -Syu docker-compose docker-buildx --noconfirm
else
    echo "Installing Docker"
    sudo pacman -S docker docker-compose docker-buildx --noconfirm
fi
sudo systemctl enable docker
sudo usermod -aG docker $USER
