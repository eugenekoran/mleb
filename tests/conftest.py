import pytest
from pathlib import Path
from mleb.dataset import MLEBDataset
from mleb.extractor import Subject, QuestionExtractor, AnswerExtactor, ImageExtractor, TableExtractor


@pytest.fixture
def temp_output_file(tmp_path):
    return tmp_path / "test_output.jsonl"


@pytest.fixture
def sample_subject():
    return Subject("phy", "rus", "2023")


@pytest.fixture
def sample_dataset(temp_output_file):
    return MLEBDataset(str(temp_output_file), rewrite=True)


@pytest.fixture
def sample_pdf_path(tmp_path):
    pdf_path = tmp_path / "sample.pdf"
    # Create a dummy PDF file
    pdf_path.write_bytes(b'%PDF-1.5\n%\xe2\xe3\xcf\xd3\n')
    return pdf_path.as_posix()


@pytest.fixture
def question_extractor(sample_pdf_path):
    return QuestionExtractor(sample_pdf_path)


@pytest.fixture
def answer_extractor(sample_pdf_path):
    return AnswerExtactor(sample_pdf_path)


@pytest.fixture
def image_extractor(sample_pdf_path):
    return ImageExtractor(sample_pdf_path)


@pytest.fixture
def table_extractor(sample_pdf_path):
    return TableExtractor(sample_pdf_path)
