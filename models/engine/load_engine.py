#!/usr/bin/python3
from models.engine.file_storage import FileStorage


def load_engine():
    storage_sys = FileStorage()
    storage_sys.reload()
    available_obj = storage_sys.all()
    return available_obj
