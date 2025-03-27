# Aganitha_Backend: PubMed Paper Fetcher

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

2. **Install dependencies using Poetry**:

   Make sure you have **Poetry** installed. If not, you can install it by following the instructions from the [Poetry documentation](https://python-poetry.org/docs/#installation).

   Once Poetry is installed, run:

   ```bash
   poetry install
   ```

   This will install all the required dependencies listed in the `pyproject.toml` file.

3. **Running the Script**:

   Once the dependencies are installed, you can run the script by calling the `fetch_pubmed_papers` function from `fetch.py`. For example:

   ```Python
   from fetch import fetch_pubmed_papers

   papers = fetch_pubmed_papers("cancer immunotherapy")
   print(papers)
   ```

   Alternatively, you can use the Poetry run command to execute the script:

   ```bash
   poetry run get-papers-list "cancer immunotherapy" -f results.csv
   ```

   This will fetch paper details related to the search query "cancer immunotherapy" and save them to `results.csv`.

## Tools and Libraries Used

- **Poetry**: A dependency management tool for Python that simplifies package management and project setup.
  - [Poetry Documentation](https://python-poetry.org/docs/)

- **`requests`**: A simple HTTP library for Python that allows you to send HTTP requests to the PubMed API.
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
        "Title": "Antibiotic prophylaxis when taking corticosteroids.",
        "Publication Date": "2025 Mar 26",
        "Non-academic Authors": ["Karthik Pohane"],
        "Company Affiliations": ["XYZ Pharma"],
        "Corresponding Author Email": "karthikpohane@xyzpharma.com"
    }
]
```

## Screenshot

Below is a screenshot of the program output for a sample search query:

![Program Output 1](https://github.com/user-attachments/assets/b5cd52a3-730a-4431-95ed-0f1698b14936)
![Program Output 2](https://github.com/user-attachments/assets/e39b0a83-2810-4c2d-a716-6419223ee0bd)
![Program Output 3](https://github.com/user-attachments/assets/fa52068c-87aa-4cf7-8b1d-c0184e5165d2)

## Command-line Program Features

The program allows you to fetch research papers based on a user-specified query using the PubMed API. The following options are available when executing the program via the command line:

### Accepts Query as a Command-line Argument:
You can specify the query to search for papers directly in the command line.

```bash
poetry run get-papers-list "your query here"
```

### Command-line Options:
The following command-line options are available to customize your execution:

- **`-h` or `--help`**: Displays usage instructions and available options.

    ```bash
    poetry run get-papers-list -h
    ```

- **`-d` or `--debug`**: Enables debug information during execution, which can help with troubleshooting or understanding the flow of the program. This option will print additional debug logs.

    ```bash
    poetry run get-papers-list -d "your query here"
    ```

- **`-f` or `--file`**: Specifies the filename where the results will be saved. If this option is not provided, the program will print the results to the console by default.

    ```bash
    poetry run get-papers-list -f results.csv "your query here"
    ```

## Contributing

Please feel free to fork the repository and submit pull requests. If you find any bugs or have suggestions for improvements, please open an issue.

## License

This project is open-source and available under the MIT License.

## Author

- Karthik Pohane  
- Email: kartikpohane0612@gmail.com
