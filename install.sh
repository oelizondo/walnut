echo 'Installing Walnut...'
git clone https://github.com/oelizondo/walnut ~/.walnut

walnut=$(echo $PATH | grep walnut)

if [ -z $walnut ]; then
  echo 'Adding Walnut to your Path...'
  echo 'export PATH="$HOME/.walnut:$PATH"' >> ~/.bash_profile
  echo 'export PATH="$HOME/.walnut:$PATH"' >> ~/.bashrc
  echo 'export PATH="$HOME/.walnut:$PATH"' >> ~/.zshrc
fi

echo 'Walnut is installed.'
echo 'Restart you terminal to start working.'
