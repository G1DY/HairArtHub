#!/usr/bin/env python
import sys

from flask_cors import CORS

from hairArtProject import create_app

# print(sys.path)

app = create_app()
CORS(app)


if __name__ == "__main__":
    app.run(debug=True)
