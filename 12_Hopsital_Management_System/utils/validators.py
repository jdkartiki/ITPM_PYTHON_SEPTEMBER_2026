def validate_age(age):
    if age < 0 or age > 120:
        raise ValueError("Invalid Age")

def validate_date(date_str):
    from datetime import datetime
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")

# Concepts:
# Exception
# Validation