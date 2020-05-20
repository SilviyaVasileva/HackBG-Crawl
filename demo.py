from bs4 import BeautifulSoup
import requests
import ssl
import sys, os


ssl.match_hostname = lambda cert, hostname: True


def get_links(start_link, all_links):
    # start_link += input

    try:
        r = requests.get(start_link)
        # html = r.content.decode('utf-8')
        soup = BeautifulSoup(r.text, 'html.parser')

        links = soup.find_all('a')

        for link in links:
            link_to_print = link.get('href')
            if link_to_print is None:
                # print("HERE1")
                pass
            elif len(link_to_print) <= 0:
                pass
            elif link_to_print[0] == '#':
                # print("HERE2")
                pass
            elif "/setLanguage" in link_to_print:
                # print("HERE3")
                pass
            elif link_to_print in all_links:
                pass
            elif link_to_print[0] == "/" or '.bg' not in link_to_print:
                link_to_print = start_link + link_to_print
            elif "http" not in link_to_print:
                print(link_to_print)
                all_links.append(link_to_print)
                print("-----------------------------")
            elif "javascript:window.bookmarksite" in link_to_print:
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
                    print("-----------------------------")
                    get_links(link_to_print, all_links)
    except requests.exceptions.SSLError:
        pass


def main():
    all_links = []
    # print("1111111")

    # get_links("https://www.cpdp.bg/userfiles/file/KZLD-clip.mp4", all_links)
    get_links("https://register.start.bg", all_links)


if __name__ == '__main__':
    main()
