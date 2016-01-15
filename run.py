#!flask/bin/python
from app import app
app.run(threaded=True, debug=True)
