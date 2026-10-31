import os
import sys

# Ensure api directory is always on path
api_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "api"))
if api_dir not in sys.path:
    sys.path.insert(0, api_dir)

# Set offline mode and test mode flags
os.environ["OFFLINE_MODE"] = "1"
os.environ["IS_TESTING"] = "1"
os.environ["DISABLE_OLLAMA"] = "1"

