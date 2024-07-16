import os
from main import is_zip_file

def test_is_zip_file():
    zip_path = "tests_data/example01.zip"
    assert is_zip_file(zip_path)

    img_path = "tests_data/example_image01.png"
    assert not is_zip_file(img_path)
