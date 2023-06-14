import os
import uuid


def generate_unique_filename(filename: str) -> str:
    _name, extension = os.path.splitext(filename)
    return f'{uuid.uuid4()}.{extension}'
