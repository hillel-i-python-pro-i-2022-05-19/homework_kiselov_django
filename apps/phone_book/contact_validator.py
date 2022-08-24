import re


def contact_validator(contact_type: str, contact_value: str) -> bool:
    if contact_type == "Phone":
        pattern = r"[+]380\d{9}$"
    elif contact_type == "email":
        pattern = r"\w+@(gmail.com|ukr.net)$"
    elif contact_type == "Telegram":
        pattern = r"@\w+"
    elif contact_type == "LinkedIn":
        pattern = r"https://www.linkedin.com/in/\w+"

    result = re.findall(pattern, contact_value)
    if result:
        return True
    else:
        return False
