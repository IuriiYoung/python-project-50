import os
import subprocess


def test_gendiff_script():

    base_dir = os.path.dirname(__file__)
    file1 = os.path.join(base_dir, "test_data", "file1.json")
    file2 = os.path.join(base_dir, "test_data", "file2.json")
    expected_result = os.path.join(base_dir, "test_data", "expected_result.txt")

    result = subprocess.run(
        ["gendiff", file1, file2],
        capture_output=True,
        text=True,
    )

    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    print("RETURNCODE:", result.returncode)

    assert result.returncode == 0

    with open(expected_result, encoding="utf-8") as f:
        expected_output = f.read()

    assert result.stdout == expected_output


test_gendiff_script()
print("Done")