## Common

### Dependencies

#### Install project dependencies

[🤖 Just](https://github.com/casey/just)

[🌐 Poetry](https://python-poetry.org/)

#### Install Python dependencies

```bash
python3 -m venv venv
source venv/bin/activate
just install
```

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

# Install Docker, git, nginx, mysql drivers and cetbot
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common git nginx certbot python3-certbot-nginx build-essential python3-dev default-libmysqlclient-dev

# Download the Docker GPG key (used to verify the authenticity and integrity of Docker packages during installation)
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# ONE COMMAND | adds the Docker repository entry to the system's software sources list
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker related tools
sudo apt update -y
sudo apt install -y docker-ce docker-ce-cli containerd.io

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Make it executable so we can run it directly from the command line
sudo chmod +x /usr/local/bin/docker-compose

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
```

Then start the containers
```bash
docker-compose build
docker-compose up -d
```

## Setup NGINX
ToDo

## Setup Certbot and request an SSL certificate
ToDo

## Updateing
```bash
# stop the containers
docker-compose down

# fetch the updated source code
git pull

# rebuild and restart the containers
docker-compose build
docker-compose up -d --force-recreate
```

## Troubleshooting
```bash
docker exec -it CONTAINER_ID /bin/bash
docker-compose up -d --force-recreate
sudo systemctl restart nginx
```
