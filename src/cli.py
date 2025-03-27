import typer
import csv
from typing import Optional
from pubmed.fetch import fetch_pubmed_papers

app = typer.Typer()


@app.command()
def main(
    query: str,
    file: Optional[str] = typer.Option(None, "-f", "--file", help="Save output to CSV."),
    debug: bool = typer.Option(False, "-d", "--debug", help="Enable debug mode."),
):
    """Fetch PubMed papers and print or save results."""
    try:
        if debug:
            typer.echo("Fetching papers with query: " + query)

        papers = fetch_pubmed_papers(query)

        if not papers:
            typer.echo("No results found for the query.")
            return

        if file:
            save_to_csv(papers, file)
            typer.echo(f"Results saved to '{file}'")
        else:
            for paper in papers:
                typer.echo(paper)

    except Exception as e:
        typer.echo(f"Error: {e}")


def save_to_csv(papers: list, filename: str):
    """Save the fetched papers to a CSV file."""
    fieldnames = ["PubmedID", "Title", "Publication Date", "Non-academic Authors", "Company Affiliations", "Corresponding Author Email"]
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for paper in papers:
            writer.writerow({
                "PubmedID": paper["PubmedID"],
                "Title": paper["Title"],
                "Publication Date": paper["Publication Date"],
                "Non-academic Authors": ", ".join(paper["Authors"]["Non-academic Authors"]) if paper["Authors"]["Non-academic Authors"] else "N/A",
                "Company Affiliations": ", ".join(paper["Authors"]["Company Affiliations"]) if paper["Authors"]["Company Affiliations"] else "N/A",
                "Corresponding Author Email": paper["Corresponding Author Email"]
            })


if __name__ == "__main__":
    app()
