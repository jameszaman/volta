"""
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
"""
from dotenv import load_dotenv
from os import environ
from pathlib import Path
from dns import resolver

# This code is in case the DNS is not set properly by the user.
resolver.default_resolver=resolver.Resolver(configure=False)
resolver.default_resolver.nameservers=['8.8.8.8']

# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# MongoDB
MONGO_DATABASE_URI = environ.get('MONGO_DATABASE_URI', 'mongodb://localhost:27017')
MONGO_DATABASE_NAME = environ.get('MONGO_DATABASE_NAME', 'volta')

# FastAPI
API_PREFIX = environ.get('API_PREFIX', '/api/v1')
API_KEY = environ.get('API_KEY')