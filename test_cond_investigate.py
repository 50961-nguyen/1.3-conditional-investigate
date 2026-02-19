import re

def test_header_comments():
    """Students should have a docstring with author, date, and description"""
    with open("cond_investigate.py", encoding="utf-8") as f:
        kids_code = f.read()

    # Check that a module-level docstring exists
    docstring_match = re.search(r'^\s*"""(.*?)"""', kids_code, re.DOTALL)
    assert docstring_match is not None, "You must include a header docstring using triple quotes (\"\"\")"

    docstring = docstring_match.group(1)

    # Check for author field with a non-empty value
    author_match = re.search(r'author\s*:\s*(.+)', docstring, re.IGNORECASE)
    assert author_match is not None, "Your header must include an 'author:' field"
    assert author_match.group(1).strip() != "", "Your 'author:' field must not be empty"

    # Check for date field with a non-empty value
    date_match = re.search(r'date\s*:\s*(.+)', docstring, re.IGNORECASE)
    assert date_match is not None, "Your header must include a 'date:' field"
    assert date_match.group(1).strip() != "", "Your 'date:' field must not be empty"

    # Check that there's at least one line that isn't just author/date (a description)
    lines = [line.strip() for line in docstring.strip().splitlines()]
    description_lines = [
        line for line in lines
        if line
        and not re.match(r'author\s*:', line, re.IGNORECASE)
        and not re.match(r'date\s*:', line, re.IGNORECASE)
    ]
    assert len(description_lines) >= 1, "Your header must include a short description of the program"

def test_var_count():
    """Students should have added an extra variable"""
    with open("cond_investigate.py", encoding="utf-8") as f:
        kids_code = f.read()

    found = re.findall("^[a-zA-Z_]+ ?=", kids_code, re.MULTILINE)
    assert len(found) >= 4, "You must add a new variable"

def test_var_used():
    """Students need to use that variable in an if statement"""
    with open("cond_investigate.py", encoding="utf-8") as f:
        kids_code = f.read()

    # find all the variables
    found = re.findall("^[a-zA-Z_]+ ?=", kids_code, re.MULTILINE)
    old_vars = ["is_cold_outside=", "favourite_number=", "name_of_hero=", "e="]
    new_vars = [var for var in found if var.replace(' ', '') not in old_vars]

    for var in new_vars:
        var = var.replace(' ', '')[:-1]
        found = re.search(f"^if .*{var}.*:", kids_code, re.MULTILINE)
        print(found)
        assert found is not None, f"You must use your new variable {var}"