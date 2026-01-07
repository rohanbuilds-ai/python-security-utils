from python_security_utils.log_parser import parse_log_file


def test_empty_file(tmp_path):
    p = tmp_path / "file.txt"
    p.write_text("")
    result = parse_log_file(str(p))
    assert result == (0, 0, 0)
