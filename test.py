# test to scrape static GitHub page
import csv

from requests_html import HTMLSession

session = HTMLSession()

url = "https://github.com/timebreaker49?tab=repositories"
response = session.get(url)

container = response.html.find("#user-repositories-list", first=True)
myList = container.find("li")

sheet = [["Name", "Language"]]

languages = ["Python", "JavaScript", "Kotlin", "Java", "CSS", "HTML"]


def in_list(element):
    for lan in languages:
        for elem in element:
            if lan in elem:
                return lan


for item in myList:
    elements = item.text.split("\n")
    name = elements[0]
    lang = in_list(elements)

    sheet.append([name, lang])

with open("Filename.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(sheet)
