#!/usr/bin/python3
""" Unique FileStorage instance for the application """
from models.engine.file_storage import FileStorage

''' FileStorage instance in a variable'''
storage = FileStorage()
storage.reload()
