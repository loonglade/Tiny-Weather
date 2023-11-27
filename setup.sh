#!/bin/bash

# Check for Python and Git
command -v python3 >/dev/null 2>&1 || { echo >&2 "Python 3 is required but it's not installed. Aborting."; exit 1; }
command -v git >/dev/null 2>&1 || { echo >&2 "Git is required but it's not installed. Aborting."; exit 1; }


cd "/Users/$(whoami)/Applications"
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
python temp.py
EOF

# Make run_project.sh executable
chmod +x run_project.sh

# Create the launchd plist file
PLIST="$HOME/Library/LaunchAgents/com.user.tinyweather.plist"
cat << EOF > "$PLIST"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.tinyweather</string>
    <key>Program</key>
    <string>$PROJECT_DIR/run_project.sh</string>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
EOF

# Load the plist file
launchctl load "$PLIST"

echo "Setup is complete."
