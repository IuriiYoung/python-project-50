import json
import os

from gendiff.gendiff import gendiff


def load_json(file_name):
    path = os.path.join(os.path.dirname(__file__), 'test_data', file_name)
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def load_text(file_name):
    path = os.path.join(os.path.dirname(__file__), 'test_data', file_name)
    with open(path, encoding='utf-8') as f:
        return f.read().strip()
    

def test_gendiff_flat_json():
    dict1 = load_json('file1.json')
    dict2 = load_json('file2.json')
    expected = load_text('expected_result.txt')
    result = gendiff(dict1, dict2)
    assert result == expected

