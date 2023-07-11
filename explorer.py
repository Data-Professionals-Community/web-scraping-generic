# %%
import requests
from bs4 import BeautifulSoup

# %%
url = 'https://www.imdb.com/chart/top/'
payload = {
    'ref_':'nv_mv_250'
}

headers = {
    'Accept-Language':'en-US,en;q=0.9',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

response = requests.get(
    url=url,
    params=payload,
    headers=headers,
)

print(type(response))
print(f'URL: {response.url}')
print(f'Status Code: {response.status_code}')
print(f'Status Code text: {response.reason}')
print(f'Encoding: {response.encoding}')

# %%
html_content = response.content
parser = 'html.parser'

soup = BeautifulSoup(
    markup=html_content,
    features=parser,
)

soup

# %%

div_class = 'ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-14dd939d-7 fjdYTb cli-title'
html_tag = 'div'

for element in soup.find_all(name=html_tag, class_=div_class):
    print(element.find(name='h3', class_='ipc-title__text').text)
    print(element.find(name='a', class_='ipc-title-link-wrapper').get('href'))
    
# %%
