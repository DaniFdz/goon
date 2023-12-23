FROM python:3.11.6-buster

# Set the working directory in the container
WORKDIR /opt/project

# Setup environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /opt/project
ENV CORE_SETTING_IN_DOCKER true

# Install dependencies
RUN set -xe \
		&& apt-get update \
		&& apt-get install -y --no-install-recommends build-essential just \
		&& pip install --no-cache-dir virtualenvwrapper poetry==1.7.0 \
		&& apt-get clean \
		&& rm -rf /var/lib/apt/lists/*

# Copy and install dependencies
COPY [ "poetry.lock", "pyproject.toml", "./" ]
RUN poetry install --no-root --no-dev

# Copy project files
COPY [ "README.md", "justfile", "./" ]
COPY core core
# COPY local local

# Expose Django development server port
EXPOSE 8000

# Set up entrypoint
COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
