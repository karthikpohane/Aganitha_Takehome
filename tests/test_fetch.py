# tests/test_fetch.py
import pytest
from pubmed.fetch import fetch_pubmed_papers


def test_fetch_pubmed_papers():
    query = "cancer immunotherapy"
    papers = fetch_pubmed_papers(query, max_results=1)
    
    assert isinstance(papers, list)
    assert len(papers) > 0
    assert "PubmedID" in papers[0]
    assert "Title" in papers[0]
