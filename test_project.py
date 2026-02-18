import pytest
from project import validate_sequence, get_sequence_stats, generate_reverse_complement

def test_validate_sequence():
    assert validate_sequence("atgc") == "ATGC"
    assert validate_sequence("A C G T") == "ACGT"
    with pytest.raises(ValueError):
        validate_sequence("ATGX") # Invalid base

def test_get_sequence_stats():
    stats = get_sequence_stats("GGCC")
    assert stats["gc_percentage"] == 100.0
    assert stats["length"] == 4
    assert stats["counts"]["G"] == 2

def test_generate_reverse_complement():
    # DNA test
    assert generate_reverse_complement("ATGC") == "GCAT"
    # RNA test
    assert generate_reverse_complement("AUGC") == "GCAU"
    # Ambiguous N test
    assert generate_reverse_complement("ATTN") == "NAAT"

