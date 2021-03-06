from bs4 import BeautifulSoup
import requests
import ssl
from gateway import Gateway
import sys, os


ssl.match_hostname = lambda cert, hostname: True

gw = Gateway()


def add_in_db(link):
    # gw = Gateway()

    # print("here")
    if gw.check_if_in_db(link):
        # print("there")
        gw.insert_in_db(link)


def get_links(start_link):
    # start_link += input
    all_links = []

    try:
        r = requests.get(start_link)
        # html = r.content.decode('utf-8')
        soup = BeautifulSoup(r.text, 'html.parser')

        links = soup.find_all('a')

        for link in links:
            link_to_print = link.get('href')
            if link_to_print is None:
                pass
            elif len(link_to_print) <= 0:
                pass
            elif link_to_print[0] == '#':
                pass
            elif "/setLanguage" in link_to_print:
                pass
            elif link_to_print in all_links:
                pass
            elif link_to_print[0] == "/" or '.bg' not in link_to_print:
                link_to_print = start_link + link_to_print
            # elif "http" not in link_to_print:
            #     print(link_to_print)
            #     all_links.append(link_to_print)
            #     print("-----------------------------")
            elif "javascript" in link_to_print:
                pass
            else:
                if "fb-messenger://share/?link=" in link_to_print:
                    link_to_print2 = link_to_print[27:]
                    link_to_print = link_to_print2
                if link_to_print in all_links:
                    pass
                else:
                    print(link_to_print)
                    all_links.append(link_to_print)
                    add_in_db(link_to_print)
                    print("-----------------------------")
    except requests.exceptions.SSLError:
        pass

    finally:
        return all_links


def crawler_recurtion(url, visited_links):
    if url is None:
        return False

    visited_links.append(url)

    if not gw.check_if_in_db(url):
        if gw.is_vivited(url):
            url = gw.get_link()
        gw.set_visited(url)
    else:
        add_in_db(url)
        gw.set_visited(url)

    all_links = get_links(url)
    for link in all_links:
        if link not in visited_links:
            crawler_recurtion(link, visited_links)


def parrallel_link(all_links):
    # gw = Gateway()
    url_link = gw.get_link()
    crawler_recurtion(url_link, all_links)


def main():
    all_links = []
    command = sys.argv[1]
    if command == "parallel":
        parrallel_link(all_links)
    elif command == "commit":
        gw.db.session.commit()
    else:
        crawler_recurtion("https://register.start.bg", all_links)


if __name__ == '__main__':
    main()
