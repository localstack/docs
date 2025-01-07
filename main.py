import requests
from xml.etree import ElementTree as ET

# URL of the sitemap
sitemap_url = "https://docs.localstack.cloud/sitemap.xml"

# Fetch the sitemap
response = requests.get(sitemap_url)
sitemap_content = response.content

# Parse the XML content
namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
root = ET.fromstring(sitemap_content)

# Fetch all pages under /academy
academy_pages = []
for url in root.findall('ns:url', namespace):
    loc = url.find('ns:loc', namespace).text
    if '/academy/' in loc:
        academy_pages.append(loc)

print(academy_pages)