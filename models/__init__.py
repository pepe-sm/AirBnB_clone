#!/usr/bin/python3
"""
    create a init module 
    allows use of moduless in engine sub-package
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
