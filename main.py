#!/usr/bin/env python3
"""
HIT137 Assignment 3 - AI Model Demo
Main entry point for the application.
"""

import sys
import os

# Add the current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Now we can import from the app package
from app.gui.main import main

if __name__ == "__main__":
    main()
