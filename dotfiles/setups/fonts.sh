HOME="/home/nhuengzii"
rm -rf "$HOME/.config/qtile/dotfiles/cache/CascadiaCode.zip"
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.2/CascadiaCode.zip -P "$HOME/.config/qtile/dotfiles/cache"
sudo unzip "$HOME/.config/qtile/dotfiles/cache/CascadiaCode.zip" -d "/usr/share/fonts/caskaydia"
fc-cache -fv
