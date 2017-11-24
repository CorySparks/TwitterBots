import requests
from bs4 import BeautifulSoup

while True:
    def GirlNames():
        print "Working"
        # Collect first page of boy name list
        page = requests.get("http://www.babywonderland.co.uk/baby-names/girls-names/girls-a-z-traditional.html")

        # Create a BeautifulSoup object
        soup = BeautifulSoup(page.text, "html.parser")

        # Pull text from all instances of <a> tag within  div
        NameClass = soup.find(class_="article-content")
        name = NameClass.find_all("li")
        print "Collecting Names"

        # Create for loop to print out all boy names
        for names in name:
            justName = names.contents[0]
            f = open('Names.txt','a')
            f.write('\n' + justName)
            f.close()
            print justName
        print "All names added to Names.txt"


    def BoyNames():
        print "Working"
        # Collect first page of boy name list
        page = requests.get("http://www.babywonderland.co.uk/baby-names/boys-names/boys-a-z-traditional.html")

        # Create a BeautifulSoup object
        soup = BeautifulSoup(page.text, "html.parser")

        # Pull text from all instances of <a> tag within  div
        NameClass = soup.find(class_="article-content")
        name = NameClass.find_all("li")
        print "Collecting Names"

        # Create for loop to print out all boy names
        for names in name:
            justName = names.contents[0]
            f = open('Names.txt','a')
            f.write('\n' + justName + ',')
            f.close()
            print justName
        print "All names added to Names.txt"

    choice = int(raw_input("1. Girl Names\n2. Boy Names\n"))
    options = { 1 : GirlNames,
                2 : BoyNames
    }
    options[choice]()
