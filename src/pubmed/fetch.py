import requests
import xml.etree.ElementTree as ET
from typing import List, Dict
from .utils import extract_authors_info, parse_email

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"


def fetch_pubmed_papers(query: str, max_results: int = 10) -> List[Dict]:
    """Fetch papers from PubMed API using a query string."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "xml",
    }

    response = requests.get(PUBMED_API_URL, params=params)
    if response.status_code != 200:
        raise Exception("Failed to fetch data from PubMed API.")
    
    root = ET.fromstring(response.text)
    paper_ids = [id_elem.text for id_elem in root.findall(".//Id")]

    return fetch_paper_details(paper_ids)


def fetch_paper_details(paper_ids: List[str]) -> List[Dict]:
    """Fetch detailed information for a list of PubMed paper IDs."""
    if not paper_ids:
        return []

    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "xml",
    }

    response = requests.get(PUBMED_SUMMARY_URL, params=params)
    if response.status_code != 200:
        raise Exception("Failed to fetch paper details from PubMed API.")

    root = ET.fromstring(response.text)
    papers = []
    
    for doc in root.findall(".//DocSum"):
        # Parsing details for each paper
        paper_data = {
            "PubmedID": doc.find(".//Id").text,
            "Title": doc.find(".//Item[@Name='Title']").text,
            "Publication Date": doc.find(".//Item[@Name='PubDate']").text or "Unknown",
            "Authors": extract_authors_info(doc),
            "Corresponding Author Email": parse_email(doc),
        }
        papers.append(paper_data)
    
    return papers
