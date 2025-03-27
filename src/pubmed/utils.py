import re
from typing import List, Dict, Optional


def extract_authors_info(doc) -> Dict[str, List[str]]:
    """Extract author information and identify non-academic authors."""
    authors_data = {
        "Non-academic Authors": [],
        "Company Affiliations": []
    }
    authors = doc.findall(".//Item[@Name='AuthorList']//Item")

    # Ensure that we handle empty author or affiliation fields gracefully
    if not authors:
        return authors_data

    for author in authors:
        name = author.find(".//Name").text if author.find(".//Name") is not None else "Unknown"
        affiliation = author.find(".//Affiliation").text if author.find(".//Affiliation") is not None else ""

        if is_company_affiliation(affiliation):
            authors_data["Company Affiliations"].append(name)
        elif not is_academic_affiliation(affiliation):
            authors_data["Non-academic Authors"].append(name)

    return authors_data


def is_academic_affiliation(affiliation: str) -> bool:
    """Check if the affiliation is academic."""
    academic_keywords = ["university", "institute", "college", "research"]
    return any(keyword.lower() in affiliation.lower() for keyword in academic_keywords)


def is_company_affiliation(affiliation: str) -> bool:
    """Check if the affiliation is related to a company."""
    company_keywords = ["pharma", "biotech", "ltd", "inc", "corp"]
    return any(keyword.lower() in affiliation.lower() for keyword in company_keywords)


def parse_email(doc) -> Optional[str]:
    """Extract the email of the corresponding author."""
    emails = doc.findall(".//Item[@Name='AuthorList']//Item//Affiliation")
    for email in emails:
        if email is not None and re.match(r"[^@]+@[^@]+\.[^@]+", email.text):
            return email.text
    return "N/A"  # Return "N/A" if no email is found
