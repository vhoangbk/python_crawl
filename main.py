from bs4 import BeautifulSoup

def main():
    soup = BeautifulSoup("<html> <a id=\"id_google\" href=\"http://google.com\"> google </a> a web page</html>", 'html.parser').b

    print(soup['id_google'])

main()
