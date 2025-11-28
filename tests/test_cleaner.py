import pytest
from app.core.cleaner import recursive_cleaner

def test_recursive_cleaner_nested_dict():
    data = {"a": {"b": "c"}}
    # "a: b: c.."
    expected = "a: b: c.."
    assert recursive_cleaner(data) == expected

def test_recursive_cleaner_list():
    data = ["hello", "world"]
    expected = "hello world"
    assert recursive_cleaner(data) == expected

def test_recursive_cleaner_mixed():
    data = {"title": "My Post", "tags": ["news", "tech"]}
    # "title: My Post. tags: news tech."
    expected = "title: My Post. tags: news tech."
    assert recursive_cleaner(data) == expected

def test_recursive_cleaner_markdown():
    data = "# Title *bold* and [link](url)"
    expected = "Title bold and link"
    assert recursive_cleaner(data) == expected

def test_recursive_cleaner_html():
    data = "<div><p>Paragraph</p> <br> <span>Text</span></div>"
    # Should remove tags and normalize whitespace
    expected = "Paragraph Text"
    assert recursive_cleaner(data) == expected

def test_recursive_cleaner_complex_nested():
    data = {
        "section": {
            "header": "## Welcome",
            "content": ["* Item 1", "> Quote"]
        }
    }
    # Inner list: "Item 1 Quote"
    # Inner dict: "header: Welcome. content: Item 1 Quote."
    # Outer dict: "section: header: Welcome. content: Item 1 Quote.."
    
    expected = "section: header: Welcome. content: Item 1 Quote.."
    assert recursive_cleaner(data) == expected

def test_recursive_cleaner_code_blocks():
    data = "Here is code: ```python print('hello') ``` end."
    expected = "Here is code: python print('hello') end."
    # Note: My regex `re.sub(r'`+', '', text)` just removes backticks, keeping content.
    # This is often desired for "narrative" output unless we want to strip code entirely.
    # The current implementation removes backticks.
    assert recursive_cleaner(data) == expected

def test_recursive_cleaner_none():
    assert recursive_cleaner(None) == ""
