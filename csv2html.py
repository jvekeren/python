import pandas as pd

# Read the CSV file
csv_file_path = r'o:\battery\2025-02-08-battery.csv'
df = pd.read_csv(csv_file_path, header=None)

# Define column names
df.columns = ['Date', 'Time', 'batSOC%', '(UN)LOAD', 'elecLOAD', 'totLOAD', 'totUNLOAD', 'batPWR']

# Convert the DataFrame to an HTML table
html_table = df.to_html(index=False, classes='table')

# Add CSS to center-align the 'batSOC%' column
html_table = html_table.replace('<td>', '<td style="text-align:center">')

# Add JavaScript for auto-reloading the page
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Battery Data</title>
    <style>
        .table {{
            width: 100%;
            border-collapse: collapse;
            margin: 0;
        }}
        .table th, .table td {{
            border: 1px solid black;
            padding: 4px; /* Reduced padding */
            text-align: center;
            margin: 0; /* No margin */
            font-size: 12px; /* Smaller font size */
            width: 40px; /* Fixed column width */
        }}
    </style>
    <script>
        // Function to check for changes and reload the page
        function checkForChanges() {{
            fetch(window.location.href, {{ cache: "no-store" }})
                .then(response => response.text())
                .then(html => {{
                    const parser = new DOMParser();
                    const newDoc = parser.parseFromString(html, "text/html");
                    const newContent = newDoc.body.innerHTML;
                    if (document.body.innerHTML !== newContent) {{
                        document.body.innerHTML = newContent;
                    }}
                }});
        }}

        // Check for changes every 5 seconds
        setInterval(checkForChanges, 5000);
    </script>
</head>
<body>
    {html_table}
</body>
</html>
"""

# Save the HTML content to a file
html_file_path = r'C:\Users\johan\OneDrive\Bureaublad\2025-02-08-battery.html'
with open(html_file_path, 'w') as file:
    file.write(html_content)

print(f"HTML file has been created at {html_file_path}")