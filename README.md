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
mkdir -p ~/.docker/cli-plugins/
curl -SL https://github.com/docker/compose/releases/download/v2.3.3/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose
chmod +x ~/.docker/cli-plugins/docker-compose

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
MYSQL_DATABASE=core
MYSQL_USER=<user>
MYSQL_PASSWORD=<password>
MYSQL_ROOT_PASSWORD=<password>
```

Open the `./local/settings.prod.py` file and type:
```py
DEBUG = False
SECRET_KEY = '<Paste the key here>'
ADMIN_URL = '<New url for django admin panel>'
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

Delete the content in the ngnix config file and open it
```bash
rm /etc/nginx/sitex-available/default
vim /etc/nginx/sitex-available/default
```

Then paste this configuration:
```nginx
server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://localhost:8000;


        proxy_http_version 1.1;

        proxy_set_header Upgrade $http_upgrade;

        proxy_set_header Connection "upgrade";

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
Save the file and exit the editor

Test the nginx configuration
```bash
nginx -t
```

If tests is successful, restart NGINX to load in the new configuration
```bash
systemctl restart nginx
```

Allow NGINX through firewall
```
sudo ufw allow 'Nginx Full'
```

## Setup Certbot and request an SSL certificate

Follow the prompts to obtain an SSL certificate for your domain name. Certbot will automatically configure NGINX to use the SSL certificate.
```bash
certbot --nginx
```
Make sure the certificate auto-renewal is set up by running the following command
```bash
sudo certbot renew --dry-run
```

Create a new NGINX configuration file
```bash
sudo rm /etc/nginx/sites-available/default
sudo nano /etc/nginx/sites-available/default
```

```nginx
server {
    listen 80 default_server;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl default_server;
    ssl_certificate /etc/letsencrypt/live/goon-web.es/fullchain.pem;

    ssl_certificate_key /etc/letsencrypt/live/goon-web.es/privkey.pem;

    ssl_session_cache shared:le_nginx_SSL:10m;
    ssl_session_timeout 1440m;

    ssl_session_tickets off;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers off;


    client_max_body_size 20M;

    location / {
        proxy_pass http://localhost:8000/;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_redirect   off;

        proxy_buffering  off;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host $http_host;
    }

    location /static {
        autoindex off;
        alias /var/www/static;
    }

    location /media {
        autoindex off;
        alias /var/www/media;
    }
}
```

Save the file and exit the editor

Test the NGINX configuration
```bash
sudo nginx -t
```

If the test is successful, restart NGINX
```bash
sudo systemctl restart nginx
```

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
docker ps -a -q | xargs docker rm -f
docker images -q | xargs docker rmi
docker volume ls -q | xargs docker volume rm

docker exec -it CONTAINER_ID /bin/bash
docker compose up -d --force-recreate
sudo systemctl restart nginx
```
