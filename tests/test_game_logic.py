from logic_utils import (
    check_guess,
    load_high_score,
    parse_guess,
    save_high_score,
    update_score,
)


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_check_guess_too_high():
    assert check_guess(60, 40) == "Too High"


def test_check_guess_too_low():
    assert check_guess(20, 40) == "Too Low"


def test_check_guess_win():
    assert check_guess(40, 40) == "Win"


def test_update_score_win_first_attempt():
    assert update_score(0, "Win", 1) == 90


def test_update_score_win_second_attempt():
    assert update_score(0, "Win", 2) == 80


def test_parse_guess_not_a_number():
    assert parse_guess("abc") == (False, None, "That is not a number.")


def test_parse_guess_empty():
    assert parse_guess("") == (False, None, "Enter a guess.")


def test_parse_guess_valid():
    assert parse_guess("42") == (True, 42, None)


def test_load_high_score_missing_file(tmp_path):
    assert load_high_score(tmp_path / "missing.txt") == 0


def test_load_high_score_valid_file(tmp_path):
    score_file = tmp_path / "high_score.txt"
    score_file.write_text("85")
    assert load_high_score(score_file) == 85


def test_load_high_score_invalid_content(tmp_path):
    score_file = tmp_path / "high_score.txt"
    score_file.write_text("not-a-number")
    assert load_high_score(score_file) == 0


def test_save_high_score(tmp_path):
    score_file = tmp_path / "high_score.txt"
    save_high_score(score_file, 120)
    assert score_file.read_text() == "120"


def test_save_and_load_high_score(tmp_path):
    score_file = tmp_path / "high_score.txt"
    save_high_score(score_file, 40)
    assert load_high_score(score_file) == 40
