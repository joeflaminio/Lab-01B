# TVMaze Show Data Aggregator

This project fetches show data from the TVMaze API and aggregates counts by genre and network channel into a structured JSON summary.

## Data source
- TVMaze API Endpoint: https://api.tvmaze.com/shows?page=0

## Setup & Execution
1. Install dependencies:
   pip install -r requirements.txt
2. Run the program:
   python records.py

## Example output
{"source_url": "https://api.tvmaze.com/shows?page=0", "total_records_processed": 240}

## Data quirks
- Missing Genres: Shows without listed genres are assigned to the 'not_categorized' category.
- Missing Networks: Shows with a null or missing network object are categorized under 'unknown Network'.

## Design choices
- Dictionaries for Aggregations: Used Python dictionary key-value lookup and .get() defaults for fast O(1) count updates and missing-key handling.
- Pathlib: Used pathlib.Path for cross-platform file handling when reading and writing outputs.

## Known limitations
- The script currently fetches only page 0 of the API rather than iterating across all paginated pages.
