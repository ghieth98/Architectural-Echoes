"""
Web scraping file
"""
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://www.ranker.com/list/world-famous-architects-throughout-history/info-lists/')
time.sleep(2)

elem = driver.find_element("xpath", "/html/body")

no_of_page_downs = 156

while no_of_page_downs:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    no_of_page_downs -= 1

# Find the <ul> element containing the <li> items
article = driver.find_element("xpath", "//ul[@class='blogView_list__0crL4']")
# Find all <li> elements within the <ul>
items = article.find_elements("xpath",
                              "./li[@class='blogItem_container__WRfTk blogItem_content__D40Pl blogItem_landscapeContent__WqX7L']")

csv_file = open('echoes_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['name', 'image', 'quote', 'age', 'place_of_birth', 'projects'])

for item in items:
    try:
        architect_name = item.find_element("xpath",
                                           ".//div[@class='HeaderContainer_container__2tow7 blogItem_title__XZpF5']/div[@class='HeaderContainer_itemNameContainer__rXHhg']/h2").text
        print(architect_name)

        image = item.find_element("xpath",
                                  ".//div[@class='blogItem_mediaItem__3JLMe']/a/figure[@class='Media_main__ex93e Media_roundedCorners__1e4A_ blogItem_fullWidth__RhaT4']/img")
        image_source = image.get_attribute("src")
        print(image_source)

        bio = item.find_element("xpath",
                                ".//div[@class='blogItem_bottomContentWrapper__Wmx64']/div[@class='container_container__53t32']/div[@class='container_innerContainer__ulE_r']").text
        print(bio)

        age = item.find_element("xpath", ".//div[@class='blogItem_bottomContentWrapper__Wmx64']/ul/li[1]").text.strip('Age: ')
        print(age)

        place_of_birth = item.find_element("xpath",
                                           ".//div[@class='blogItem_bottomContentWrapper__Wmx64']/ul/li[2]").text.strip('Place of Birth: ')

        print(place_of_birth)

        projects = item.find_element("xpath", ".//div[@class='blogItem_bottomContentWrapper__Wmx64']/ul/li[3]").text.strip('Structures: ').split(',')
        print(projects)
    except Exception as e:
        architect_name = None
        image_source = None
        bio = None
        age = None
        place_of_birth = None
        projects = None

    csv_writer.writerow([architect_name, image_source, bio, age, place_of_birth, projects])

csv_file.close()

driver.quit()
