#!/bin/bash

# Check for Python and Git
command -v python3 >/dev/null 2>&1 || { echo >&2 "Python 3 is required but it's not installed. Aborting."; exit 1; }
command -v git >/dev/null 2>&1 || { echo >&2 "Git is required but it's not installed. Aborting."; exit 1; }

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Get the current directory (the project directory)
PROJECT_DIR="$(pwd)"

# Create run_project.sh
cat << EOF > run_project.sh
#!/bin/bash

# Navigate to the project directory
cd "$PROJECT_DIR"

# Activate the virtual environment
source venv/bin/activate

# Run the main Python script (update this with the correct script name)
python3 temp.py
EOF

# Make run_project.sh executable
chmod +x run_project.sh

# Add a cron job to run the script at boot
(crontab -l 2>/dev/null; echo "@reboot $PROJECT_DIR/run_project.sh") | crontab -

echo "Setup is complete."