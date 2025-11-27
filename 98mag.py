import requests

import lxml.html


url = r'https://www.98mag.kz/category/gorod/sobytiya/'

html = requests.get(url).content
tree = lxml.html.document_fromstring(html)
events = tree.findall('./body/section[1]/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div')
# soup = BeautifulSoup(html, 'lxml')
# events = soup.find_all('div', class_='rubric__slider-list_cell')

for event in events:
    title = event.find('div/div[2]/div[2]').text.strip()
    # title = event.find('div', class_='preview__body')
    event_url = event.find('div/a').attrib['href']
    event_page = requests.get(event_url).content
    event_page_tree = lxml.html.document_fromstring(event_page)
    date = event_page_tree.cssselect('div.post-date')[0].text.strip()
    print(title)
    print(event_url)
    print(date)
    print()
