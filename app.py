from selenium import webdriver
from time import sleep
import subprocess
import shlex


email = input("Enter mail receiver : ")
sujet = input("Enter le Sujet : ")
lettre : input("Entrez Votre message : ")

#username = input("Enter Github username : ")
#password = input("Enter Github password : ")
password = "IKRAM.hiba2004"

#link = "https://github.com/Ayoubkassi/"+project_name+".git"


class MailBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://accounts.google.com/signin/v2/identifier?hl=fr&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        sleep(2)
        login_field = self.driver.find_element_by_xpath(
            '//*[@id="identifierId"]').send_keys(username)

        login_butt = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()

        sleep(5)
        pass_field = self.driver.find_element_by_xpath(
            '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)

        next_butt = self.driver.find_element_by_xpath(
            '//*[@id="passwordNext"]/div/button/span').click()
        sleep(5)

        self.driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
        sleep(2)

        self.driver.execute_script("document.getElementById(':su').value=arguments[0]",(email))
        




        # to_field = self.driver.find_element_by_name('to')
        # to_field.send_keys(email)
        #
        # subject_field = self.driver.find_element_by_name('subjectbox')
        # subject_field.send_keys(sujet)
        #
        # body_field = self.driver.find_element_by_css_selector('.Am.Al.editable.LW-avf.tS-tW')
        # body_field.send_keys(lettre)
        #
        #
        # send_btn = self.driver.find_element_by_css_selector('.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3')
        # send_btn.click()
        #
        # time.sleep(5)











        # email_field = self.driver.find_element_by_xpath(
        #     '//*[@id=":pi"]/div/div[3]/div/div/div/div/span').text = email
        # check_butt = self.driver.find_element_by_xpath(
        #     '//*[@id="repository_auto_init"]').click()
        # sleep(2)
        # create_butt = self.driver.find_element_by_xpath(
        #     '//*[@id="new_repository"]/div[4]/button').click()
        # sleep(4)
        #self.driver.close()


my_bot = MailBot('ayoub.kassi@uit.ac.ma', password)
#subprocess.call(['bash', 'github.sh', link, project_name])
