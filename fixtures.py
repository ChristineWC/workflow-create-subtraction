from pathlib import Path
from types import SimpleNamespace
from typing import List

from pyfixtures import fixture
from virtool_workflow.api.subtractions import SubtractionProvider


@fixture
def subtraction_provider(subtraction_providers: List[SubtractionProvider]):
    return subtraction_providers[0]


@fixture
def intermediate():
    """A namespace for intermediate variables."""
    return SimpleNamespace()


@fixture
def input_path(input_files: dict) -> Path:
    """The path to the input FASTA file for the subtraction."""
    return list(input_files.values())[0]


@fixture
def fasta_path(work_path: Path) -> Path:
    """The path to the decompressed FASTA file."""
    return work_path / "subtraction.fa"
