import pytest
from grazer.grazer import Grazer

def test_grazer_init():
    grazer = Grazer('tests/testkeys.key')
    assert grazer._client is not None

def test_grazer_missing_key_file():
    with pytest.raises(FileNotFoundError):
        grazer = Grazer('tests/missingkeys.key')

def test_grazer_live_url():
    grazer = Grazer('tests/testkeys.key', live=True)
    assert grazer._client is not None