from selenium import webdriver
from time import sleep
import os

def def_environment():
    path_to_dir = os.path.dirname(os.path.realpath(__file__))
    print("Scieszka do folderu:"+path_to_dir)
    os.environ["PATH"] += os.pathsep + path_to_dir

def def_readForLogin():
    path_to_dir = os.path.dirname(os.path.realpath(__file__))
    file_pass = "gmailPass.txt"
    file = open(path_to_dir+"/"+file_pass,'r')
    dane = file.read().split('\n')
    file.close()
    #uzywam slownika do zwrocenia wielu argumentow
    return {'username': dane[0], 'password': dane[1]}

class Google:
    def __init__(self,username,password):
        self.driver=webdriver.Firefox()
        self.driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27")
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        print("widzimy_maila")
        sleep(3)
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        #self.driver.find_element_by_name("identifier").send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get('https://youtube.com')
        sleep(4)
        self.driver.find_element_by_xpath('//*[@id="button"]/button[1]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@class="style-scope ytd-compact-link-renderer"]//*[text()="Upload video"]').click()
        sleep(3)

if __name__ == "__main__":
    def_environment()
    #userData={}
    userData=def_readForLogin()
    #print(userData)
    #print(userData['username'])
    start=Google(userData['username'],userData['password'])
