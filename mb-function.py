# imports
from bs4 import BeautifulSoup
import requests


# helper functions
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


# main
def listing_crunch(url, budget):

    html_sc = requests.get(url).text
    soup = BeautifulSoup(html_sc, 'html5lib')

    page_info = soup.find('span', class_ = 'pageNumbersInfo').text
    pages_links = []
    pages_links.append(url)
    exact_pages = int(page_info[-2:])

    for i in range(2, exact_pages + 1):
        trimmed_url = url[:-1]
        added_url = trimmed_url + str(i)
        if added_url not in pages_links:
            pages_links.append(added_url)
    # ANOTHER THING I CAN THINK OF FOR GETTING ALL THE PAGES HOWEVER MANY THEY MAY BE, JUST ITERATE OVER THE NEXT PAGE BUTTON, UNTIL THERE IS NO MORE
    counter = 1

    for link in pages_links:
        url = link
        page_url = requests.get(url).text
        page_soup = BeautifulSoup(page_url, 'html5lib')
        all_listings_per_page = page_soup.find_all('table', class_ = 'tablereset', style='width:660px; margin-bottom:0px; border-top:#008FC6 1px solid;')
        page_info = page_soup.find('span', class_ = 'pageNumbersInfo').text
        print(page_info)

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

            # CHECK WHETHER IN BUDGET OR NOT
            if price <= budget:
                with open('listings-within-budget.md', 'a') as ff:
                    ff.write(f"Model: {title}\n")
                    ff.write(f"Year: {production_year}\n")
                    ff.write(f"URL: {linkk}\n")
                    ff.write(f"Price: {price}\n\n\n")
            else:
                pass
                # with open('over-budget.md', 'a') as ff:
                #     ff.write(f"Model: {title}\n")
                #     ff.write(f"Year: {production_year}\n")
                #     ff.write(f"URL: {linkk}\n")
                #     ff.write(f"Price: {price}\n\n\n")
            # HOW WOULD THE PRODUCTION YEARS BE INCORPORATED - INPUT AND THEN F''? (but the production years have to be before the budget)


if __name__ == "__main__":
    listing_crunch('https://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=rylc4e&f1=1', 2000)


# https://www.youtube.com/watch?v=704hLk559c8
