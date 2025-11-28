import re
from typing import Any

def recursive_cleaner(data: Any) -> str:
    """
    Recursively transforms data into a clean, readable string.
    
    - Dicts: Concatenates keys and values into "Key: Value." phrases.
    - Lists: Joins elements with spaces.
    - Strings: Removes markdown symbols (#, *, etc.) and HTML tags.
    - Other: Converts to string.
    """
    if isinstance(data, dict):
        parts = []
        for key, value in data.items():
            cleaned_value = recursive_cleaner(value)
            # Ensure we don't end up with double periods or weird spacing if value is empty
            if cleaned_value:
                # Clean key as well just in case
                cleaned_key = recursive_cleaner(key)
                parts.append(f"{cleaned_key}: {cleaned_value}.")
        return " ".join(parts)
    
    elif isinstance(data, list):
        return " ".join([recursive_cleaner(item) for item in data if item is not None])
    
    elif isinstance(data, str):
        text = data
        
        # 1. Remove HTML tags
        text = re.sub(r'<[^>]+>', ' ', text)
        
        # 2. Remove Markdown headers (#)
        text = re.sub(r'#+\s*', '', text)
        
        # 3. Remove bold/italic (* or _)
        text = re.sub(r'[\*_]+', '', text)
        
        # 4. Remove links [text](url) -> text
        text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
        
        # 5. Remove code blocks (```) and inline code (`)
        text = re.sub(r'`+', '', text)
        
        # 6. Remove blockquotes (>)
        text = re.sub(r'>\s*', '', text)
        
        # 7. Remove list items (-, +, *) at start of line
        text = re.sub(r'^\s*[-+\*]\s+', '', text, flags=re.MULTILINE)
        
        # 8. Normalize whitespace (multiple spaces/newlines -> single space)
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
    
    elif data is None:
        return ""
        
    else:
        return str(data)
