#!/bin/bash

# Define some variables
PROJECT_DIR=$(pwd)

# Check if poetry is installed
if ! command -v poetry &> /dev/null
then
    echo "Poetry could not be found, installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
fi

# Check if pyproject.toml exists
if [ ! -f "$PROJECT_DIR/pyproject.toml" ]; then
    echo "pyproject.toml not found. Please make sure it exists in the project directory."
    exit 1
fi

# Install the required packages from pyproject.toml
echo "Installing required packages using Poetry..."
poetry install

# Activate the virtual environment
echo "Activating virtual environment..."
source $(poetry env info --path)/bin/activate



# Run Django migrations
echo "Running Django database migrations..."
poetry add gunicorn
poetry run python manage.py migrate
poetry run python manage.py collectstatic --no-input

echo "Setup completed successfully!"
