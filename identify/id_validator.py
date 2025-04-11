def validate_chinese_id(id_number):
    """
    Validate a Chinese ID number (15 or 18 digits)
    Returns tuple of (is_valid: bool, error_message: str)
    """
    if not isinstance(id_number, str):
        return False, "ID must be a string"
    
    id_number = id_number.strip()
    length = len(id_number)
    
    # Check length
    if length not in (15, 18):
        return False, "ID must be 15 or 18 digits"
    
    # Check all digits (except last which might be X)
    if not id_number[:-1].isdigit():
        return False, "ID must contain only digits (except last which can be X)"
    
    # Validate birth date
    if length == 15:
        birth_date = f"19{id_number[6:12]}"
    else:
        birth_date = id_number[6:14]
    
    try:
        from datetime import datetime
        datetime.strptime(birth_date, "%Y%m%d")
    except ValueError:
        return False, "Invalid birth date in ID"
    
    # For 18-digit IDs, validate check digit
    if length == 18:
        weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        check_digits = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        
        total = sum(int(d) * w for d, w in zip(id_number[:-1], weights))
        calculated_check = check_digits[total % 11]
        
        if id_number[-1].upper() != calculated_check:
            return False, "Invalid check digit"
    
    return True, "Valid ID number"


if __name__ == "__main__":
    with open('dates-6411.txt', 'r') as file:
        test_ids = [line.strip() for line in file.readlines()]
    
    for id_num in test_ids:
        is_valid, msg = validate_chinese_id(id_num)
        print(f"{id_num}: {'Valid' if is_valid else 'Invalid'} - {msg}")