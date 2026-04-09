import json
import sys

try:
    with open('/var/www/public/scripts/config.json', 'r') as f:
        config = json.load(f)

    print(f"Original api.origin: {config['api']['origin']}")

    config['api']['origin'] = 'http://localhost:8092'

    with open('/var/www/public/scripts/config.json', 'w') as f:
        json.dump(config, f, indent=2)

    print(f"New api.origin: {config['api']['origin']}")
    print("Config updated successfully!")
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
