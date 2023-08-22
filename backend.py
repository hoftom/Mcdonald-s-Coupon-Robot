from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random


def __select_and_click(xpath, driver):
    scroll_distance = 500
    button = driver.find_element(By.XPATH, xpath)
    button.click()
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")



def __write_into_textfield(xpath, driver, string):
    textfield = driver.find_element(By.XPATH, xpath)
    textfield.clear()
    textfield.send_keys(string)


def __normalize_code(string):
    result = '-'.join([string[i:i + 4] for i in range(0, len(string), 4)]).upper()
    if result[-1] == "-" or result[-2] == "-":
        result = result[:-2]
    return result


def __select_options(selected_type):
    if selected_type == "Drive":
        with open('data/drive_codes.txt', 'r') as file:
            load_data = file.readlines()
    else:
        with open('data/lobby_codes.txt', 'r') as file:
            load_data = file.readlines()
    return load_data


def __delete_codeline(selected_list):
    with open('data/drive_codes.txt', 'w') as file:
        for index, w_row in enumerate(selected_list):
            if index != len(selected_list) - 1:
                file.writelines(selected_list[index + 1])




def run_program(selected_type, amount):

    selected_list = __select_options(selected_type)
    i = 0
    print(amount)


    for row in selected_list:
        if i != amount:
            if row != "\n":
                # Open browser and Get webpage
                webpage = "https://mcdonalds.fast-insight.com/voc/hu/hu"
                driver = webdriver.Chrome()
                driver.get(webpage)
                initial_page_source = driver.page_source

                # Select Delivery FALSE
                radio_delivery_xpath = '//*[@id="delivery_mo"]'
                __select_and_click(radio_delivery_xpath, driver)

                # Enter code
                code = __normalize_code(row)
                code_xpath = '//*[@id="receiptCode"]'
                __write_into_textfield(code_xpath, driver, code)


                # Click to continue
                button_xpath = '//*[@id="welcomeMessage"]/div[5]/button'
                __select_and_click(button_xpath, driver)

                time.sleep(5)
                updated_page_source = driver.page_source

                if initial_page_source == updated_page_source:
                    __delete_codeline(selected_list)
                    selected_list = __select_options(selected_type)
                else:
                    # Select the best rating
                    # A legutóbbi látogatásod alapján összességében mennyire voltál elégedett?
                    radio_first_xpath = '//*[@id="0"]/div[5]/div[1]/div[2]/span'
                    __select_and_click(radio_first_xpath, driver)

                    # Mennyire voltál elégedett a tisztasággal?
                    radio_second_xpath = '//*[@id="6"]/div[5]/div[1]/div[2]/span'
                    __select_and_click(radio_second_xpath, driver)

                    # Kollégáinkat mennyire találtad barátságosnak?

                    code_xpath = '//*[@id="receiptCode"]'
                    radio_third_xpath = '//*[@id="8"]/div[5]/div[1]/div[2]/span'
                    __select_and_click(radio_third_xpath, driver)

                    # Pontosan kaptad meg a rendelésedet?
                    radio_fourth_xpath = '//*[@id="10"]/div[5]/div[1]/div[2]/span'
                    __select_and_click(radio_fourth_xpath, driver)

                    # Hogyan értékeled a várakozási időt?
                    radio_fifth_xpath = '//*[@id="12"]/div[5]/div[1]/div[2]/span'
                    __select_and_click(radio_fifth_xpath, driver)

                    # Hogyan értékeled az általad vásárolt termékek minőségét?
                    radio_sixth_xpath = '//*[@id="14"]/div[5]/div[1]/div[2]/span'
                    __select_and_click(radio_sixth_xpath, driver)

                    # Tapasztaltál bármilyen problémát a látogatásod alatt?
                    radio_seventh_xpath = '//*[@id="56"]/div[5]/div[2]/div[2]/span'
                    __select_and_click(radio_seventh_xpath, driver)

                    # A mostani élményed alapján mennyire valószínű, hogy a következő 30 napban visszatérsz ebbe a McDonald's étterembe?
                    radio_eighth_xpath = '//*[@id="58"]/div[5]/div[1]/div[2]/span'
                    __select_and_click(radio_eighth_xpath, driver)

                    # A mostani élményed alapján mennyire valószínű, hogy ajánlani fogod ezt az éttermet egy barátnak vagy családtagnak?
                    radio_ninth_xpath = '//*[@id="35"]/div[5]/div[1]/div[2]/span'
                    __select_and_click(radio_ninth_xpath, driver)

                    # Wow! Nagyon örülünk, hogy éttermünkben ilyen kellemes élményt tudtunk szerezni Neked! Kinek, vagy minek köszönhető ez?
                    with open("data/ratings.txt", "r") as file:
                        ratings = file.readlines()

                    popup_text = random.choice(ratings)
                    text_popup_xpath = '//*[@id="21"]/div[5]/div/input'
                    __write_into_textfield(text_popup_xpath, driver, popup_text)

                    # Nemed?
                    genders = ['//*[@id="22"]/div[5]/div[1]/div[2]/span', '//*[@id="22"]/div[5]/div[2]/div[2]/span']

                    radio_tenth_xpath = random.choice(genders)
                    __select_and_click(radio_tenth_xpath, driver)

                    # Életkorod?
                    ages = ['//*[@id="23"]/div[5]/div[1]/div[2]/span', '//*[@id="23"]/div[5]/div[2]/div[2]/span',
                            '//*[@id="23"]/div[5]/div[3]/div[2]/span', '//*[@id="23"]/div[5]/div[4]/div[2]/span',
                            '//*[@id="23"]/div[5]/div[5]/div[2]/span', '//*[@id="23"]/div[5]/div[6]/div[2]/span']

                    radio_eleventh_xpath = random.choice(ages)
                    __select_and_click(radio_eleventh_xpath, driver)

                    # Milyen gyakran jársz McDonald's étterembe
                    frequency = ['//*[@id="24"]/div[5]/div[1]/div[2]/span', '//*[@id="24"]/div[5]/div[2]/div[2]/span',
                                 '//*[@id="24"]/div[5]/div[3]/div[2]/span', '//*[@id="24"]/div[5]/div[4]/div[2]/span',
                                 '//*[@id="24"]/div[5]/div[5]/div[2]/span', '//*[@id="24"]/div[5]/div[6]/div[2]/span']
                    radio_twelfth_xpath = random.choice(frequency)
                    __select_and_click(radio_twelfth_xpath, driver)

                    # Send template
                    button_submit_xpath = '//*[@id="submit-wrapper"]/div[3]/button/span'
                    button = driver.find_element(By.XPATH, button_submit_xpath)
                    button.click()

                    #Close window

                    time.sleep(5)
                    driver.close()
                    __delete_codeline(selected_list)
                    i += 1
                    print(i)

            else:
                __delete_codeline(selected_list)
                selected_list = __select_options(selected_type)





