#!/bin/bash

# Check for Python and Git
command -v python3 >/dev/null 2>&1 || { echo >&2 "Python 3 is required but it's not installed. Aborting."; exit 1; }
command -v git >/dev/null 2>&1 || { echo >&2 "Git is required but it's not installed. Aborting."; exit 1; }

# Create and activate a Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Get the current directory (the project directory)
PROJECT_DIR="$(pwd)"

# Create run_project.sh
cat << EOF > run_project.sh
#!/bin/bash

# Get the current directory (the project directory)
PROJECT_DIR="\$( cd "\$( dirname "\${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Navigate to the project directory
cd "\$PROJECT_DIR"

# Activate the virtual environment
source venv/bin/activate

# Infinite loop to keep the application running
while true; do
    # Run the main Python script (update this with the correct script name)
    python3 temp.py

    # Wait for 1 minute before restarting the script in case it exits
    echo "Application stopped. Restarting in 1 minute..."
    sleep 60
done
EOF

# Make run_project.sh executable
chmod +x run_project.sh

# Add a cron job to run the script at boot
(crontab -l 2>/dev/null; echo "@reboot $PROJECT_DIR/run_project.sh") | crontab -

echo "Running Tiny-Weather"
nohup ./run_project.sh &

echo "Setup is complete."