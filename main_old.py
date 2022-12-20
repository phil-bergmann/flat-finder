import undetected_chromedriver as uc
import time

from bs4 import BeautifulSoup


def immoscout():
    api_url = "https://www.immobilienscout24.de/Suche/de/bayern/muenchen/wohnung-mieten?numberofrooms=2.0-&price=-2000.0&livingspace=60.0-&pricetype=rentpermonth&geocodes=0916200017,0916200016,0916200013051,0916200013050,0916200014060,0916200025008,0916200014070,0916200010033,0916200014048,0916200010,0916200013,0916200015,0916200010032,0916200014,0916200025,0916200025075&sorting=2&enteredFrom=result_list"

    #api_url = "https://abrahamjuliot.github.io/creepjs/"
    options = uc.ChromeOptions()
    #options.headless = True
    #options.add_argument('--headless')
    chrome = uc.Chrome(options=options)
    chrome.get(api_url)
    time.sleep(5)
    chrome.save_screenshot('datadome_undetected_webddriver.png')
    element = chrome.execute_script(
        """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
    element.click()
    time.sleep(5)

    chrome.save_screenshot('datadome_undetected_webddriver.png')

    html = chrome.page_source

    print(html)

    with open("html.html", "w") as outf:
        for l in html:
            outf.write(l)


def soup():
    with open("html.html") as inf:
        html = "".join(inf.readlines())

    soup = BeautifulSoup(html, 'html.parser')

    #print(soup.select("#resultListItems li.result-list__listing'"))

    print(soup.select("#resultListItems li.result-list__listing")[0].select(".result-list-entry .result-list-entry__criteria .grid-item:first-child dd"))

    #print([i.select('.result-list-entry') for i in soup.select('#resultListItems li.result-list__listing')])

    first_children = [i.text for i in soup.select('.result-list-entry .result-list-entry__criteria .grid-item:first-child dd')]
    print(first_children)

    for tag in soup.find_all(attrs={'class': 'result-list-entry__brand-title-container'}):
        print(tag("h5")[0].text)

    for tag in soup.find_all(attrs={'class': 'result-list-entry__criteria'}):
        #print("----")
        #print(tag)
        dd = tag.find_all_next("dd")
        #print(dd)
        #for ddd in dd:
            #print(ddd.text)



if __name__ == "__main__":
    soup()