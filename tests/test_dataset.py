import pytest
from mleb.dataset import MLEBDataset
from mleb.extractor import Subject


def test_mleb_dataset_initialization(temp_output_file):
    dataset = MLEBDataset(str(temp_output_file), rewrite=True)
    assert dataset.output_file == temp_output_file


def test_mleb_dataset_add_subject(sample_dataset, mocker):
    mock_subject = mocker.Mock(spec=Subject)
    mock_subject.extract.return_value = mock_subject
    mock_subject.to_inspect_dataset.return_value = None

    mocker.patch('mleb.dataset.Subject', return_value=mock_subject)

    sample_dataset.add_subject("phy", "2023")

    # It's expected to be called twice (once for each language)
    assert mock_subject.extract.call_count == 2
    assert mock_subject.to_inspect_dataset.call_count == 2


def test_mleb_dataset_invalid_subject(sample_dataset):
    with pytest.raises(ValueError, match="Subject 'invalid' is not a valid subject code."):
        sample_dataset.add_subject("invalid", "2023")


def test_mleb_dataset_existing_file(temp_output_file):
    MLEBDataset(str(temp_output_file), rewrite=True)

    with pytest.raises(ValueError, match="Output file already exists. Use rewrite=True to overwrite it."):
        MLEBDataset(str(temp_output_file), rewrite=False)
