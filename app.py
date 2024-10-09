# run.py
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from .  import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)