# Goon

## Developers

### Install [🤖 Just](https://github.com/casey/just) and [🌐 Poetry](https://python-poetry.org/)

```bash
sudo apt install cargo pipx
cargo install just
pipx install poetry
```

### Add cargo bin to path

Add this line to your .bashrc or .zshrc

```bash
export PATH="$HOME/.cargo/bin:$PATH"
```

### Install dependencies
```bash
just install
```

### Run the application

```bash
mkdir -p local
cp core/project/settings/templates/settings.dev.py ./local/settings.dev.py
just dev
just migrations
just run
```

### Install dependencies
```
# Update the package index and upgrade packages
sudo apt update -y && sudo apt upgrade -y

# Install Docker, git, nginx, mysql drivers and certbot
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common git nginx certbot python3-certbot-nginx build-essential python3-dev default-libmysqlclient-dev

# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update

# Install Docker related tools
sudo apt update -y
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Add your user to the Docker group
sudo usermod -aG docker $USER

# Exit then ssh back in to pick up new permissions
exit
ssh ubuntu@IP_ADDRESS
```

### Download the repo
```bash
# Create a new ssh-key with empty passphrase
ssh-keygen -t rsa -b 4096 -f ~/.ssh/github

# Print the public key and copy it
cat ~/.ssh/github.pub
```

Create a new ssh key in [github](https://github.com/settings/keys) and paste it

And the clone the repo
```
git clone git@github.com:DaniFdz/goon.git
cd goon
```

### Run the application

Locally create a new django secret key with the next command:
```bash
poetry run python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the secret key and the:
```
# Connect to the instance
ssh ubuntu@IP_ADDRESS

# Create local settings file
test -f .env || touch .env
mkdir -p local
sudo touch ./local/settings.prod.py
```

Open the `.env` file and type:
```
MYSQL_USER=<user>
MYSQL_PASSWORD=<password>
MYSQL_ROOT_PASSWORD=<password>
```

Open the `./local/settings.prod.py` file and type:
```py
DEBUG = False
SECRET_KEY = '<Paste the key here>'
CORE_SETTINGS_ADMIN_URL = '<New url for django admin panel>'

LOGGING["formatters"]["colored"] = {  # type: ignore # noqa: F821
    "()": "colorlog.ColoredFormatter",
    "format": "%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s",
}
LOGGING["loggers"]["core"]["level"] = "PROD"  # type: ignore # noqa: F821
LOGGING["handlers"]["console"]["level"] = "PROD"  # type: ignore # noqa: F821
LOGGING["handlers"]["console"]["formatter"] = "colored"  # type: ignore # noqa: F821
```

Then start the containers
```bash
docker compose build
docker compose up -d
```

Create superuser oneliner
```bash
docker exec -it $(docker ps | grep app | awk '{print $1}') poetry run python3 -m core.manage createsuperuser
```

## Setup NGINX
ToDo

## Setup Certbot and request an SSL certificate
ToDo

## Updating
```bash
# stop the containers
docker compose down

# fetch the updated source code
git pull

# rebuild and restart the containers
docker compose build
docker compose up -d --force-recreate
```

## Troubleshooting
```bash
docker exec -it CONTAINER_ID /bin/bash
docker compose up -d --force-recreate
sudo systemctl restart nginx
```
