"""
couple of things to test

1. is it iterating the pages?

2. why tf does it not go below 1999

3. why no car more expensive than the budget does not go into the other list

4. 

---

links are fetching, pages are changing, so it either has to be in the way i define all_listings per page and I need to find another way to redefine,

also if I'm starting from the 1st page, I have to switch the if cases for the 30 and 36, so that when it is not an e36, it will enter the checks for the e30

maybe when iterating the soup element is not updating, so try to redefine it in the second loop, for the listings

when printing the page status, it stays on the first one, find out why is that

OKE I FIXED THE MOST IDIOTIC MISTAKE, AKA THE DEFINITION OF THE NAME OF THE SOUP WAS DIFFERENT, BUT THERE ARE OTHER ISSUES NOW, WHEN THE PRICE IS MORE THAN 4 DIGITS, 
THE POPPER FUNCTION BREAKS, CUZ WE TAKIN UP TO THE 4TH CHARACTER, SO MAYBE A DIFFERENT FUNCTION FOR THE PRICE THAT TAKES THE ENTIRE STRING INSTEAD OF 


"""

from bs4 import BeautifulSoup
import requests

url = 'https://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=rylc4e&f1=1'
html_sc = requests.get(url).text
soup = BeautifulSoup(html_sc, 'html5lib')
mock_budget = 10000

def popper(string):
    basic_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in string:
        if char not in basic_nums:
            string = string.replace(char, '')
    return int(string[:4])




# this is ok when the pages are no more than 10 - 11, but in the case of for example 58 pages, another way needs to be - Страница 1 от (58) - take this num and iterate over the links adding the respective changes
num_page = soup.find_all('a', class_ = 'pageNumbers')
page_info = soup.find('span', class_ = 'pageNumbersInfo').text
pages_links = []
pages_links.append(url)
exact_pages = int(page_info[-2:])
print(exact_pages)

for i in range(2, exact_pages + 1):
    trimmed_url = url[:-1]
    added_url = trimmed_url + str(i)
    if added_url not in pages_links:
        pages_links.append(added_url)


# for index, i in enumerate(num_page):
#     i = num_page[index]['href'] 
#     i = 'https:' + i
#     if i not in pages_links:
#         pages_links.append(i)

print(pages_links)

# all_listings_per_page = soup.find('table', class_ = 'tablereset', style='width:660px; margin-bottom:0px; border-top:#008FC6 1px solid;')


# prdyer = all_listings_per_page.find('td', style = 'width:440px;height:50px;padding-left:4px').text

# print(prdyer)

# prdyer = popper(prdyer)

# print(prdyer)

#------------

# for link in pages_links:
#     url = link
#     source_code = requests.get(url).text
#     soup = BeautifulSoup(source_code, 'html5lib')

#     page_info = soup.find('span', class_ = 'pageNumbersInfo').text
#     print(page_info)


#--------------
# line by line debugging to find out why tf does the above code iterate over the pages and the below does not 



# for link in pages_links:
#     print(link)
#     url = link
#     source_code = requests.get(url).text
#     soup = BeautifulSoup(source_code, 'html5lib')
#     # all_listings_per_page = soup.find_all('table', class_ = 'tablereset', style='width:660px; margin-bottom:0px; border-top:#008FC6 1px solid;')
#     # print(len(all_listings_per_page))
#     page_info = soup.find('span', class_ = 'pageNumbersInfo').text
#     print(page_info)
    # # pages_links.pop(0)

    # for listing in all_listings_per_page:
    #     urll = listing.find('td', class_ = 'valgtop', style = 'width:162px;height:40px;padding-left:4px').a
    #     linkk = 'https:' + urll['href']
    #     title = urll.text
    #     price = listing.find('td', class_ = 'algright valgtop', style = 'width:135px;height:40px;padding-left:4px').span.text
    #     production_year = listing.find('td', style = 'width:440px;height:50px;padding-left:4px').text
    #     # list_url = requests.get(linkk).text
    #     # soup1 = BeautifulSoup(list_url, 'html5lib')
    #     # prdyer = soup1.find('ul', class_ = 'dilarData').find_all('li')[1].text
    #     # # prdyer = prdyer.split()
    #     # production_year = prdyer#[1]

    #     price = popper(price)
    #     production_year = popper(production_year)
    #     print(counter, " ", production_year, title)
    #     # page_info = soup.find('span', class_ = 'pageNumbersInfo').text
    #     # print(page_info)
    #     counter+=1

    #     # if E30
    #     if int(production_year) in range(1982, 1995):
    #         if int(price) <= mock_budget:
    #             with open('e30-list.md', 'a') as ff:
    #                 ff.write(f"Model: {title}\n")
    #                 ff.write(f"Year: {production_year}\n")
    #                 ff.write(f"URL: {linkk}\n")
    #                 ff.write(f"Price: {price}\n\n\n")
    #         else:
    #             with open('dream-car-list.md', 'a') as ff:
    #                 ff.write(f"Model: {title}\n")
    #                 ff.write(f"Year: {production_year}\n")
    #                 ff.write(f"URL: {linkk}\n")
    #                 ff.write(f"Price: {price}\n\n\n")
    #     # if E36            
    #     elif int(production_year) in range(1996, 1999):
    #         if '316' in title or '1.6' in title:
    #             continue
    #         elif int(price) <= mock_budget:
    #             with open('e36-list.md', 'a') as ff:
    #                 ff.write(f"Model: {title}\n")
    #                 ff.write(f"Year: {production_year}\n")
    #                 ff.write(f"URL: {linkk}\n")
    #                 ff.write(f"Price: {price}\n\n\n")
    #         else:
    #             continue







"""
removed from the main function
        # list_url = requests.get(linkk).text
        # soup1 = BeautifulSoup(list_url, 'html5lib')
        # prdyer = soup1.find('ul', class_ = 'dilarData').find_all('li')[1].text
        # # prdyer = prdyer.split()
        # production_year = prdyer#[1]


"""