import pytest

from core.portfolio.models import Categorie, Clothe, generate_filename


def test_categorie_type(category):
    assert isinstance(category, Categorie)


def test_categorie_str(category):
    assert str(category) == category.name


def test_clothe_type(clothe):
    assert isinstance(clothe, Clothe)


def test_clothe_str(category, clothe):
    assert str(clothe) == f"{category.name} - {clothe.name}"


def test_clothe_str_no_category(clothe_no_category):
    assert str(clothe_no_category) == clothe_no_category.name


def test_generate_filename(dummy_file):
    result = generate_filename(None, dummy_file)

    # Check if the result has the correct format
    assert result.startswith("images/")
    assert len(result.split(".")) == 2  # UUID + extension

    # Check if the extension is correct
    ext = dummy_file.split(".")[-1]

    assert result.endswith(f".{ext}")


def test_generate_filename_different_extensions():
    filename1 = "file1.txt"
    filename2 = "file2.png"

    result1 = generate_filename(None, filename1)
    result2 = generate_filename(None, filename2)

    # Check if the extensions are preserved in the generated filenames
    assert result1.endswith(".txt")
    assert result2.endswith(".png")


def test_generate_filename_empty_filename():
    with pytest.raises(ValueError, match="Filename cannot be empty"):
        generate_filename(None, "")


def test_generate_filename_no_extension():
    filename = "file_without_extension"

    result = generate_filename(None, filename)

    # Check if the result has the correct format and includes a generated UUID

    assert result.startswith("images/")
    assert len(result.split(".")) == 2  # UUID only
