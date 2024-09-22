# config.py

import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./main_blueprints_test.sqlite'
    # TEMPLATE_FOLDER = 'templates'
    TEMPLATE_FOLDER = '../templates'  # Assuming the Config class is in the blueprint_manager directory
    STATIC_FOLDER = '../static'  # Assuming the Config class is in the blueprint_manager directory