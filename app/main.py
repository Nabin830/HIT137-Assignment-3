
import sys
import os

# Add the parent directory to Python path so we can import from app package
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from app.gui.main import main

if __name__ == "__main__":
    main()

