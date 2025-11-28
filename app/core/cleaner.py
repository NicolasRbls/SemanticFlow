import re
from typing import Any

def recursive_cleaner(data: Any) -> str:
    """
    Recursively transforms data into a clean, readable string.
    
    - Dicts: Concatenates keys and values into "Key: Value." phrases.
    - Lists: Joins elements with spaces.
    - Strings: Removes markdown symbols (#, *, etc.).
    - Other: Converts to string.
    """
    if isinstance(data, dict):
        parts = []
        for key, value in data.items():
            cleaned_value = recursive_cleaner(value)
            # Ensure we don't end up with double periods or weird spacing if value is empty
            if cleaned_value:
                parts.append(f"{key}: {cleaned_value}.")
            else:
                parts.append(f"{key}.")
        return " ".join(parts)
    
    elif isinstance(data, list):
        return " ".join([recursive_cleaner(item) for item in data])
    
    elif isinstance(data, str):
        # Remove markdown symbols
        # Remove headers (#)
        text = re.sub(r'#+\s*', '', data)
        # Remove bold/italic (* or _)
        text = re.sub(r'[\*_]+', '', text)
        # Remove links [text](url) -> text
        text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
        # Remove code blocks (```)
        text = re.sub(r'`+', '', text)
        # Remove blockquotes (>)
        text = re.sub(r'>\s*', '', text)
        # Remove list items (-, +, *) at start of line
        text = re.sub(r'^\s*[-+\*]\s+', '', text, flags=re.MULTILINE)
        
        return text.strip()
    
    else:
        return str(data)
