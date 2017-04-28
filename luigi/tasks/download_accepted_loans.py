import luigi

# $ pip install mechanicalsoup
import mechanicalsoup

import time

from zipfile import ZipFile
import urllib
from tempfile import mktemp
import os
class DownloadLendingClubDataSet(luigi.Task):

        
    #EMAIL = luigi.Parameter()

    #PASSWORD = luigi.Parameter()

    def run(self):

        # end whtever needs to be run
        print("Started : Creating directory for download data")
        #Create dir for download
        path = "Data/DOWNLOAD_LOAN_DATA"


        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
        print("Finished : Creating directory for download data")

        EMAIL = 'bhanushali.n@husky.neu.edu'
        PASSWORD = 'nehal123'

        #constants
        LOGIN_URL = 'https://www.lendingclub.com/account/gotoLogin.action'
        POST_LOGIN_URL ='https://www.lendingclub.com/info/download-data.action'
        #cwd = os.getcwd()
        destDir =self.output().path

        browser = mechanicalsoup.Browser() #Browser

        # request lending club login page. the result is a requests.Response object
        # http://docs.python-requests.org/en/latest/user/quickstart/#response-content
        login_page = browser.get(LOGIN_URL)

        # similar to assert login_page.ok but with full status code in case of
        # failure.
        login_page.raise_for_status()

        print("Logging in....")

        # login_page.soup is a BeautifulSoup object
        # http://www.crummy.com/software/BeautifulSoup/bs4/doc/#beautifulsoup
        # we grab the login form
        login_form = mechanicalsoup.Form(login_page.soup.select_one('#login form'))

        # specify username and password
        login_form.input({"login_email": EMAIL, "login_password": PASSWORD})

        # submit form
        page2 = browser.submit(login_form, login_page.url)


        # verify we are now logged in
        # assert will see to it that the selected object exists
        # assert page2.soup.select("ul.signed-in")
        print("Succesfully logged in to ",page2.soup.title.text," [",page2.url,"]")

        # verify we remain logged in (thanks to cookies) as we browse the rest of
        # the site
        page3 = browser.get(POST_LOGIN_URL)
        assert page3.soup.select("ul.signed-in")
        print("Successfully navigated to ",page3.soup.title.text," [",page3.url,"]")

        print("Started : Downloading download data")

        #scrape
        download_file_string = page3.soup.select("div#loanStatsFileNamesJS")[0].text

        download_file_list = download_file_string.split("|")

        initial_path = "https://resources.lendingclub.com/"

        #download
        for sec_filename in download_file_list:
            try:
                if(len(sec_filename) >0):
                    theurl = initial_path+sec_filename
        #             print(theurl)
                    filename = mktemp('.zip')
                    name, hdrs = urllib.request.urlretrieve(theurl, filename)
                    thefile=ZipFile(filename)
                    thefile.extractall(destDir)
                    thefile.close()
            except Exception as e:
                print("URL : "+sec_filename+" not found "+e)


        time.sleep(1)
        print("Finished : Downloading download data")

    def output(self):
    #save file to Data directory
        return luigi.LocalTarget('Data/DOWNLOAD_LOAN_DATA/')

# if __name__ == '__main__':
#     luigi.run()
