import requests
from bs4 import BeautifulSoup
from terminaltables import AsciiTable


def last_updated():
    url = "https://www.microsoft.com/en-us/download/details.aspx?id=56519"
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.content, 'html.parser')
    header = soup.find("div", attrs={"class": "header date-published"})
    if header is not None:
        date = header.next_sibling.text
    else:
        date = None
    return date

def show_on_terminal():
    date = last_updated()
    table_data = [["Last Updated"],[date]]
    table = AsciiTable(table_data)
    print(table.table)

if __name__ == '__main__':
    show_on_terminal()

