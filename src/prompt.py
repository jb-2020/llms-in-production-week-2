PROMPT = """
You will be given a prompt which you will have to translate to SQL.
Only respond with SQL in a single line.
Verify that the SQL is valid.
Do not include any formatting
Do not capitalize column headers or table names
Capitalize SQL keywords
Use the input context to determine table names
End the SQL statement with a semicolon
Do not use SQL 'AS' Keyword to rename columns

Here is the query: ${query}

${gr.complete_json_suffix_v3}
"""
