from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import pyrebase

sites = [
    {
        'url' : 'https://www.k-startup.go.kr/common/announcement/announcementList.do?mid=30004&bid=701&searchAppAt=A#none;',
        'class' : {
            'before' : 'ul.ann_list > li >',
            'title' : ' h4 > a',
            'date' : 'ul > li:nth-child(3)',
            'note' : 'h4 > span.ann_list_group02 '
        }
    }
]
class Main_process:
    def __init__(self):
        self.sites = sites
        self.rows = []
        self.control_tower()

    def __str__(self):
        return self.result

    def control_tower(self):
        # for ( 1 - 10 ) :
        # self.make_j()
        self.selenium()

    def make_j(self):
        config = {
          'apiKey': "AIzaSyCHS-_sUiQrnGsoiExzudhC93EUtoDNG5M",
          'authDomain': "start-up-web-info.firebaseapp.com",
          'projectId': "start-up-web-info",
          'storageBucket': "start-up-web-info.appspot.com",
          'messagingSenderId': "286249457073",
          'appId': "1:286249457073:web:13420494889765e86c1990",
          'measurementId': "G-PHFNZBV4FF"
        }
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database
        return

    def selenium(self):
        url = self.sites[0]['url']
        driver = self.selenium_config()
        driver.get(url)
        html = driver.page_source
        self.bs4(html)
        print(self.rows)

    def selenium_config(self):
        # options = webdriver.ChromeOptions()
        # options.add_argument("--headless")

        # Use the `install()` method to set `executabe_path` in a new `Service` instance:
        service = Service(executable_path=ChromeDriverManager().install())

        # Pass in the `Service` instance with the `service` keyword:
        driver = webdriver.Chrome(service=service)
        # service = Service(executable_path=ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(3)
        return driver

    def bs4(self, html):
        classes = self.sites[0]['class']
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one( self.make_class(classes, 'title') ).text
        if ( title == self.j ):
            return 0
        else:
            date = soup.select_one( self.make_class(classes, 'date') ).text
            note = soup.select_one( self.make_class(classes, 'note') ).text
            this_one = [ title, date, note ]
            self.rows.append(this_one)
            return 1

    def make_class(self, classes, target):
        return classes['before'] + classes[target]
