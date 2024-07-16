import os
import pytest
from main import unzip_file


@pytest.fixture
def setup_test_environment():
    zip_path = "tests_data/example01.zip"
    extract_to = "tests_data/test_extract_to"
    yield zip_path, extract_to

    cleanup_test_environment(extract_to)
    cleanup_test_environment(os.path.splitext(zip_path)[0])


def cleanup_test_environment(path):
    if os.path.exists(path):
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                cleanup_test_environment(file_path)
        os.rmdir(path)


def test_unzip_file(setup_test_environment):
    zip_path, extract_to = setup_test_environment

    assert unzip_file(zip_path, extract_to) > 0
    assert os.path.exists(extract_to)

    assert unzip_file(zip_path) > 0
    assert os.path.exists(os.path.splitext(zip_path)[0])
