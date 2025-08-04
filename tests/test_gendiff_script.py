import os
import subprocess

import pytest


@pytest.mark.parametrize("ext", ["json", "yaml"])
def test_gendiff_script(ext):
    base = os.path.dirname(__file__)
    test_data = os.path.join(base, "test_data")

    file1 = os.path.join(test_data, f"file1.{ext}")
    file2 = os.path.join(test_data, f"file2.{ext}")
    expected_result_path = os.path.join(test_data, "expected_result.txt")

    result = subprocess.run(
        ["gendiff", file1, file2],
        capture_output=True,
        text=True,
    )

    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    print("RETURNCODE:", result.returncode)

    assert result.returncode == 0

    with open(expected_result_path, encoding="utf-8") as f:
        expected_output = f.read()

    assert result.stdout.strip() == expected_output.strip()


# import os
# import subprocess


# def test_gendiff_script():

#    base_dir = os.path.dirname(__file__)
#    file1 = os.path.join(base_dir, "test_data", "file1.json")
#    file2 = os.path.join(base_dir, "test_data", "file2.json")
#   expected_result = os.path.join(base_dir, "test_data", "expected_result.txt")

#    result = subprocess.run(
#        ["gendiff", file1, file2],
#        capture_output=True,
#        text=True,
#    )

#    print("STDOUT:", result.stdout)
#    print("STDERR:", result.stderr)
#    print("RETURNCODE:", result.returncode)

#    assert result.returncode == 0

#    with open(expected_result, encoding="utf-8") as f:
#        expected_output = f.read()

#    assert result.stdout == expected_output


# test_gendiff_script()
# print("Done")