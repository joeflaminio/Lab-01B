# Delivery Fee Calculator

Calculates order delivery fees based on order total thresholds and the day of the week. Built for Lab 01B.

## Setup

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

## Run

python app.py

## Example

Enter the order total in dollars: 90
Enter the delivery day (e.g. Saturday): Thursday
Order: $90.00 on Thursday, delivery fee is $1.00.

## Known Limitations

* Day inputs require proper capitalization to match the valid days list.
* Input validation prompts print error messages rather than looping for re-entry.
