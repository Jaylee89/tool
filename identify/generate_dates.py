import sys
from datetime import datetime, timedelta

last_4_digits = "6411"
template = "610527{}{}"

def generate_identify(value: str) -> str:
    return template.format(value, last_4_digits)

def generate_dates(year):
    """Generate all dates for a given year in YYYYMMDD format"""
    if not isinstance(year, int) or year < 1:
        raise ValueError("Year must be a positive integer")
    
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    
    current_date = start_date
    while current_date <= end_date:
        yield current_date.strftime("%Y%m%d")
        current_date += timedelta(days=1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_dates.py YEAR")
        sys.exit(1)
        
    try:
        year = int(sys.argv[1])
        with open(f"dates-{last_4_digits}.txt", "w") as f:
            for date_str in generate_dates(year):
                f.write(generate_identify(value=date_str) + "\n")
        print(f"Successfully generated {year} dates in dates.txt")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()