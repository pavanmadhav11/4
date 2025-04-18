from flask import render_template, request
from app.mermaid_diagram import generate_mermaid_diagram
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    chart_url = None
    error = None
    if request.method == "POST":
        code = request.form["code"]
        mermaid_code = generate_mermaid_diagram(code)
        
        if mermaid_code:
            chart_url = f"https://mermaid-js.github.io/mermaid-live-editor/#/edit/{mermaid_code}"
        else:
            error = "Error generating the Mermaid diagram. Please check your code."
    
    return render_template("index.html", chart_url=chart_url, error=error)
