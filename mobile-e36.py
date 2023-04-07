from bs4 import BeautifulSoup
import requests

url = 'https://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=rxes3n&f1=1'
html_sc = requests.get(url).text
soup = BeautifulSoup(html_sc, 'html5lib')
mock_budget = 10000

def year_popper(string):
    basic_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in string:
        if char not in basic_nums:
            string = string.replace(char, '')
    return int(string[:4])


def price_popper(string):
    basic_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in string:
        if char not in basic_nums:
            string = string.replace(char, '')           
    try:
        return int(string)
    except ValueError:
        return 0   

num_page = soup.find_all('a', class_ = 'pageNumbers')
pages_links = []
pages_links.append(url)

for index, i in enumerate(num_page):
    i = num_page[index]['href'] 
    i = 'https:' + i
    if i not in pages_links:
        pages_links.append(i)

counter = 1

for link in pages_links:
    url = link
    page_url = requests.get(url).text
    page_soup = BeautifulSoup(page_url, 'html5lib')
    all_listings_per_page = page_soup.find_all('table', class_ = 'tablereset', style='width:660px; margin-bottom:0px; border-top:#008FC6 1px solid;')
    page_info = page_soup.find('span', class_ = 'pageNumbersInfo').text

    for listing in all_listings_per_page:
        urll = listing.find('td', class_ = 'valgtop', style = 'width:162px;height:40px;padding-left:4px').a
        linkk = 'https:' + urll['href']
        title = urll.text
        price = listing.find('td', class_ = 'algright valgtop', style = 'width:135px;height:40px;padding-left:4px').span.text
        production_year = listing.find('td', style = 'width:440px;height:50px;padding-left:4px').text

        price = price_popper(price)
        production_year = year_popper(production_year)
        print("Listing: ", counter, " ", production_year, title, price)
        counter+=1

        # if E30
        if production_year in range(1982, 1995):
            if price <= mock_budget:
                with open('e30-list.md', 'a') as ff:
                    ff.write(f"Model: {title}\n")
                    ff.write(f"Year: {production_year}\n")
                    ff.write(f"URL: {linkk}\n")
                    ff.write(f"Price: {price}\n\n\n")
            else:
                with open('dream-car-list.md', 'a') as ff:
                    ff.write(f"Model: {title}\n")
                    ff.write(f"Year: {production_year}\n")
                    ff.write(f"URL: {linkk}\n")
                    ff.write(f"Price: {price}\n\n\n")
        # if E36            
        elif production_year in range(1996, 2000):
            if '316' in title or '1.6' in title:
                continue
            elif price <= mock_budget:
                with open('e36-list.md', 'a') as ff:
                    ff.write(f"Model: {title}\n")
                    ff.write(f"Year: {production_year}\n")
                    ff.write(f"URL: {linkk}\n")
                    ff.write(f"Price: {price}\n\n\n")
            else:
                continue
