# tests/test_utils.py
from pubmed.utils import is_academic_affiliation, is_company_affiliation


def test_is_academic_affiliation():
    assert is_academic_affiliation("Harvard University") is True
    assert is_academic_affiliation("ABC Pharma Ltd.") is False


def test_is_company_affiliation():
    assert is_company_affiliation("Pfizer Inc.") is True
    assert is_company_affiliation("Oxford University") is False
