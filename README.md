# PubMed Paper Fetcher

## Overview

The **PubMed Paper Fetcher** is a Python script that fetches PubMed paper details based on a search query and extracts relevant information like PubMed ID, title, publication date, authors, company affiliations, and the corresponding author's email. The results are returned in CSV format for further analysis or processing.

## How the Code is Organized

The project is organized into two main files:

1. **`fetch.py`**:
   - Contains the main logic for interacting with the PubMed API to fetch paper IDs and their detailed information.
   - **`fetch_pubmed_papers`**: Takes a search query and returns a list of paper details.
   - **`fetch_paper_details`**: Fetches detailed information (like authors, title, and publication date) for each paper ID.

2. **`utils.py`**:
   - Provides helper functions for extracting and processing data.
   - **`extract_authors_info`**: Extracts author information, including identifying non-academic authors and company affiliations.
   - **`parse_email`**: Parses the corresponding author's email.
   - **`is_academic_affiliation`** and **`is_company_affiliation`**: Used to classify authors based on their affiliation.

## Installation Instructions

Follow these steps to set up the project and run the code:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/karthikpohane/Aganitha_Takehome.git
   cd Aganitha_Takehome
   ```

2. **Install dependencies**:

   Make sure you have Python 3.x installed. Then, install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

   The required libraries are listed in `requirements.txt`. If you don't have a `requirements.txt` file, you can create it using:

   ```bash
   pip freeze > requirements.txt
   ```

   Ensure to include the following dependencies:

   - `requests` (for making HTTP requests)
   - `xml.etree.ElementTree` (for XML parsing)

3. **Running the Script**:

   Once the dependencies are installed, you can run the script by calling the `fetch_pubmed_papers` function from `fetch.py`. For example:

   ```Python
   from fetch import fetch_pubmed_papers

   papers = fetch_pubmed_papers("cancer immunotherapy")
   print(papers)
   ```

   This will print out a list of paper details based on your search query. You can also modify the script to save the data in CSV format or perform other operations.

   ```
   poetry run get-papers-list "cancer immunotherapy" -f results.csv
   ```

## Tools and Libraries Used

- **` requests`**: A simple HTTP library for Python that allows you to send HTTP requests to the PubMed API.
  - [Requests Documentation](https://docs.python-requests.org/en/latest/)
  
- **`xml.etree.ElementTree`**: A built-in Python library for parsing and creating XML. It's used here to parse the XML responses from the PubMed API.

- **Regular Expressions**: Used in `utils.py` to parse emails of corresponding authors.

## Example Output

After executing the script, you'll get a list of dictionaries containing the following fields:

- `PubmedID`: The unique identifier for the paper.
- `Title`: The title of the paper.
- `Publication Date`: The publication date of the paper.
- `Non-academic Authors`: A list of authors affiliated with non-academic institutions.
- `Company Affiliations`: A list of authors affiliated with pharmaceutical/biotech companies.
- `Corresponding Author Email`: The corresponding author's email address, if available.

For example:

```Python
[
    {
        "PubmedID": "40145190",
        "Title": "Antibiotic prophylaxis when taking corticosteroids."
        "Publication Date": "2025 Mar 26",
        "Non-academic Authors": ["Karthik Pohane"],
        "Company Affiliations": ["XYZ Pharma"],
        "Corresponding Author Email": "karthikpohane@xyzpharma.com"
    }
]
```

## Screenshot

Below is a screenshot of the program output for a sample search query:

![image](https://github.com/user-attachments/assets/b5cd52a3-730a-4431-95ed-0f1698b14936)  
![image](https://github.com/user-attachments/assets/e39b0a83-2810-4c2d-a716-6419223ee0bd)
![image](https://github.com/user-attachments/assets/fa52068c-87aa-4cf7-8b1d-c0184e5165d2)



## Contributing

Please feel free to fix the repository and submit pull requests. If you find any bugs or have suggestions for improvements, please open an issue.

## License

This project is open-source and available under the MIT License.

## Author

Karthik Pohane
Email: kartikpohane0612@gmail.com
