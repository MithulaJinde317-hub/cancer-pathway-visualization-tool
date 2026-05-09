import requests

# KEGG pathway for ovarian cancer
pathway_id = "hsa05213"

# KEGG API URL
url = f"https://rest.kegg.jp/get/{pathway_id}"

# Fetch data
response = requests.get(url)

# Save pathway data
with open("../data/ovarian_cancer_pathway.txt", "w", encoding="utf-8") as file:
    file.write(response.text)

print("KEGG pathway data downloaded successfully!")