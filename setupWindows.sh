#!/bin/sh
virtualenv --no-site-packages --distribute .env && source .env/Scripts/activate && pip install -r requirements.txt
