# Pull Request Reporter

This Python project generates summary reports for each pull request in a specified GitHub repository.

## Features
- Retrieve pull requests from a GitHub repository
- Generate summary reports including title, author, creation date, merge status, and more
- Easy to extend and customize

## Setup
1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the dependencies using `pip install -r requirements.txt`.
4. Create a `.env` file with your GitHub token and repository.
5. Run the script using `python scripts/generate_reports.py`.

## Running Tests
Run the tests using:
```bash
python -m unittest discover tests
