import urllib.parse

# Define credentials and the base URL
username = "profoam"
password = "Mf#45671"
# Encoding the password as it is having #
encoded_password = urllib.parse.quote(password, safe='')
base_url = "staging.profoam.com/"

# Embed credentials in the URL
auth_url = f"https://{username}:{encoded_password}@{base_url}"



