def generate_mermaid_diagram(code):
    try:
        mermaid_code = """
        graph TD;
            A[Start] --> B{Is it working?};
            B -->|Yes| C[Continue];
            B -->|No| D[Fix Issue];
            C --> E[End];
            D --> B;
        """
        return mermaid_code
    except Exception as e:
        return None
