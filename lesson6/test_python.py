import math
import pytest
from lesson5.file_manager import create_folder, delete_file_or_folder, list_directory


def test_filter_even_numbers():
	assert list(filter(lambda x: x % 2 == 0, range(10))) == [0, 2, 4, 6, 8]


def test_filter_none():
	assert list(filter(None, [1, "a", 0, False, True])) == [1, "a", True]


def test_map_square():
	assert list(map(lambda x: x**2, range(5))) == [0, 1, 4, 9, 16]


def test_map_str():
	assert list(map(str, [1, 2, 3])) == ["1", "2", "3"]


def test_sorted_numbers():
	assert sorted([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]


def test_sorted_strings():
	assert sorted(["banana", "apple", "cherry"]) == ["apple", "banana", "cherry"]


def test_pi():
	assert math.pi == 3.141592653589793


def test_sqrt():
	assert math.sqrt(9) == 3


def test_pow():
	assert math.pow(2, 3) == 8


def test_hypot():
	assert math.hypot(3, 4) == 5


def test_create_folder(monkeypatch, tmp_path):
	# Тестирование создания папки
	folder_name = "test_folder"
	monkeypatch.setattr("builtins.input", lambda _: str(tmp_path / folder_name))
	create_folder()
	assert (tmp_path / folder_name).is_dir()


def test_delete_file_or_folder(monkeypatch, tmp_path):
	# Тестирование удаления файла/папки
	folder_name = tmp_path / "test_folder"
	folder_name.mkdir()
	monkeypatch.setattr("builtins.input", lambda _: str(folder_name))
	delete_file_or_folder()
	assert not folder_name.exists()


def test_list_directory(monkeypatch, capsys, tmp_path):
	# Тестирование вывода содержимого директории
	(tmp_path / "file1").touch()
	(tmp_path / "file2").touch()
	monkeypatch.setattr("os.listdir", lambda _: ["file1", "file2"])
	monkeypatch.setattr("os.getcwd", lambda: str(tmp_path))

	list_directory()
	captured = capsys.readouterr()
	assert "file1" in captured.out
	assert "file2" in captured.out
