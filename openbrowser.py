import webbrowser
import urllib.parse

# Define the JavaScript code to execute
js_code = """
alert('Hello from Python-executed JavaScript!');
"""

# Encode the JavaScript code for URL inclusion
encoded_js = urllib.parse.quote(js_code)

# Construct a data URL with the JavaScript
data_url = f"data:text/html,<script>{encoded_js}</script>"

# Open the data URL in a new browser tab
abluble = 'https://toyotabrasil.sharepoint.com/sites/memorial_dwg_materiais_gps/_api/search/query?querytext=%27YG79140013*.pdf%27&querytemplatepropertiesurl=%27spfile://webroot/queryparametertemplate.xml%27'
webbrowser.open_new_tab(abluble)