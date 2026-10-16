from datetime import datetime
#validation of date is here available for all functionalities
def validate_date(date_text):
    try:
        parsed_date = datetime.strptime(date_text, "%d.%m.%Y")
        if parsed_date.strftime("%d.%m.%Y") == date_text:
            return True
    except ValueError:
        return False
#validates if json data is a list and contains the correct type of entries for example str
def validate_list(data_list, type_of_entries):
    if not isinstance(data_list, list):
        return False
    for data in data_list:
        if not type(data) == type_of_entries:
            return False
    return True