from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.get("https://mcdonalds.fast-insight.com/voc/hu/hu")


#Select Delivery -> FALSE
radio_delivery_xpath = '//*[@id="delivery_mo"]'
radio_delivery = driver.find_element(By.XPATH, radio_delivery_xpath)
radio_delivery.click()


#Enter code
code = "OENO-NE0Y-N1P2"
code_xpath = '//input[@id="receiptCode"]'

text_code = driver.find_element(By.XPATH, code_xpath)
text_code.clear()
text_code.send_keys(code)

#Click to continue
button_xpath = '//button[@class="color-bg-main color-font-secondary"]'
button_continue = driver.find_element(By.XPATH, button_xpath)
button_continue.click()

time.sleep(5)
scroll_distance = 500


#Select the best rating
    #A legutóbbi látogatásod alapján összességében mennyire voltál elégedett?
radio_first_xpath = '//*[@id="0"]/div[5]/div[1]/div[2]/span'
radio_first = driver.find_element(By.XPATH, radio_first_xpath)
radio_first.click()
    #Mennyire voltál elégedett a tisztasággal?
radio_second_xpath = '//*[@id="6"]/div[5]/div[1]/div[2]/span'
radio_second = driver.find_element(By.XPATH, radio_second_xpath)
radio_second.click()
    #Kollégáinkat mennyire találtad barátságosnak?
driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
radio_third_xpath = '//*[@id="8"]/div[5]/div[1]/div[2]/span'
radio_third = driver.find_element(By.XPATH, radio_third_xpath)
radio_third.click()
    #Pontosan kaptad meg a rendelésedet?
driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
radio_fourth_xpath = '//*[@id="10"]/div[5]/div[1]/div[2]/span'
radio_fourth = driver.find_element(By.XPATH, radio_fourth_xpath)
radio_fourth.click()
    #Hogyan értékeled a várakozási időt?
driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
radio_fifth_xpath = '//*[@id="12"]/div[5]/div[1]/div[2]/span'
radio_fifth = driver.find_element(By.XPATH, radio_fifth_xpath)
radio_fifth.click()
    #Hogyan értékeled az általad vásárolt termékek minőségét?
driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
radio_sixth_xpath = '//*[@id="14"]/div[5]/div[1]/div[2]/span'
radio_sixth = driver.find_element(By.XPATH, radio_sixth_xpath)
radio_sixth.click()
    #Tapasztaltál bármilyen problémát a látogatásod alatt?
driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
radio_seventh_xpath = '//*[@id="56"]/div[5]/div[2]/div[2]/span'
radio_seventh = driver.find_element(By.XPATH, radio_seventh_xpath)
radio_seventh.click()
    #A mostani élményed alapján mennyire valószínű, hogy a következő 30 napban visszatérsz ebbe a McDonald's étterembe?
driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
radio_eighth_xpath = '//*[@id="58"]/div[5]/div[1]/div[2]/span'
radio_eighth = driver.find_element(By.XPATH, radio_eighth_xpath)
radio_eighth.click()
    #A mostani élményed alapján mennyire valószínű, hogy ajánlani fogod ezt az éttermet egy barátnak vagy családtagnak?
driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
radio_ninth_xpath = '//*[@id="35"]/div[5]/div[1]/div[2]/span'
radio_ninth = driver.find_element(By.XPATH, radio_ninth_xpath)
radio_ninth.click()
    #Wow! Nagyon örülünk, hogy éttermünkben ilyen kellemes élményt tudtunk szerezni Neked! Kinek, vagy minek köszönhető ez?
popup_text= "Magamnak"
radio_popup_xpath = '//*[@id="21"]/div[5]/div/input'
radio_popup = driver.find_element(By.XPATH, radio_popup_xpath)
radio_popup.clear()
radio_popup.send_keys(popup_text)
    #Nemed?
driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
radio_tenth_xpath = '//*[@id="22"]/div[5]/div[1]/div[2]/span'
radio_tenth = driver.find_element(By.XPATH, radio_tenth_xpath)
radio_tenth.click()
    #Életkorod?
driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
radio_eleventh_xpath = '//*[@id="23"]/div[5]/div[2]/div[2]/span'
radio_eleventh = driver.find_element(By.XPATH, radio_eleventh_xpath)
radio_eleventh.click()
    #Milyen gyakran jársz McDonald's étterembe
driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
radio_twelfth_xpath = '//*[@id="24"]/div[5]/div[2]/div[2]/span'
radio_twelfth = driver.find_element(By.XPATH, radio_twelfth_xpath)
radio_twelfth.click()

#Send template
button_submit_xpath = '//*[@id="submit-wrapper"]/div[3]/button/span'
button_submit = driver.find_element(By.XPATH, button_submit_xpath)
button_submit.click()


while(True):
    pass
