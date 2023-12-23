## Dependencies

### Install project dependencies

[🤖 Just](https://github.com/casey/just)

[🌐 Poetry](https://python-poetry.org/)

### Install Python dependencies

```bash
python3 -m venv venv
source venv/bin/activate
Poetry install
```

## Create development environment

```bash
mkdir -p local
cp core/project/settings/templates/settings.dev.py ./local/settings.dev.py
```
