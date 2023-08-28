import random
import time
from playwright.sync_api import sync_playwright


def __select_options(selected_type):
    if selected_type == "Drive":
        with open('data/drive_codes.txt', 'r') as file:
            load_data = file.readlines()
    else:
        with open('data/lobby_codes.txt', 'r') as file:
            load_data = file.readlines()
    print("Sikeres adatbetöltés, kiválasztott típus: " + selected_type)
    return load_data

def __normalize_code(string):
    result = '-'.join([string[i:i + 4] for i in range(0, len(string), 4)]).upper()
    if result[-1] == "-" or result[-2] == "-":
        result = result[:-2]
    print(f"Felhasznált kód: {result}")
    return result

def __delete_codeline(selected_list):
    with open('data/drive_codes.txt', 'w') as file:
        for index, w_row in enumerate(selected_list):
            if index != len(selected_list) - 1:
                file.writelines(selected_list[index + 1])


def run_program(selected_type, asked_amount):
    selected_list = __select_options(selected_type)
    successful_upload_number = 0
    print(f"Kivánt feltöltési mennyigés: {asked_amount}")

    for row in selected_list:
        if successful_upload_number + 1 <= asked_amount:
            if row != "\n":

                # Open browser and Get webpage
                with sync_playwright() as p:
                    browser = p.chromium.launch(headless=False)
                    page = browser.new_page()

                    initial_url = "https://mcdonalds.fast-insight.com/voc/hu/hu"
                    page.goto(initial_url)
                    initial_content = page.content()

                    time.sleep(2)

                    # Select Delivery FALSE
                    radio_button_xpath = '//*[@id="delivery_mo"]'
                    page.click(radio_button_xpath)

                    # Enter code
                    code = __normalize_code(row)
                    text_field_xpath = '//*[@id="receiptCode"]'
                    page.fill(text_field_xpath, code)

                    # Click to continue
                    main_button_xpath = '//*[@id="welcomeMessage"]/div[5]/button'
                    page.click(main_button_xpath)

                    time.sleep(5)
                    updated_content = page.content()
                    if initial_content != updated_content:
                        # A legutóbbi látogatásod alapján összességében mennyire voltál elégedett?
                        first_radio_button_xpath = '//*[@id="0"]/div[5]/div[1]/div[2]/span'
                        page.click(first_radio_button_xpath)

                        # Mennyire voltál elégedett a tisztasággal?
                        second_radio_button_xpath = '//*[@id="6"]/div[5]/div[1]/div[2]/span'
                        page.click(second_radio_button_xpath)

                        # Kollégáinkat mennyire találtad barátságosnak?
                        third_radio_button_xpath = '//*[@id="8"]/div[5]/div[1]/div[2]/span'
                        page.click(third_radio_button_xpath)

                        # Pontosan kaptad meg a rendelésedet?
                        fourth_radio_button_xpath = '//*[@id="10"]/div[5]/div[1]/div[2]/span'
                        page.click(fourth_radio_button_xpath)

                        # Hogyan értékeled a várakozási időt?
                        fifth_radio_button_xpath = '//*[@id="12"]/div[5]/div[1]/div[2]/span'
                        page.click(fifth_radio_button_xpath)

                        # Hogyan értékeled az általad vásárolt termékek minőségét?
                        sixth_radio_button_xpath = '//*[@id="14"]/div[5]/div[1]/div[2]/span'
                        page.click(sixth_radio_button_xpath)

                        # Tapasztaltál bármilyen problémát a látogatásod alatt?
                        seventh_radio_button_xpath = '//*[@id="56"]/div[5]/div[2]/div[2]/span'
                        page.click(seventh_radio_button_xpath)

                        # A mostani élményed alapján mennyire valószínű, hogy a következő 30 napban visszatérsz ebbe a McDonald's étterembe?
                        eighth_radio_button_xpath = '//*[@id="58"]/div[5]/div[1]/div[2]/span'
                        page.click(eighth_radio_button_xpath)

                        # A mostani élményed alapján mennyire valószínű, hogy ajánlani fogod ezt az éttermet egy barátnak vagy családtagnak?
                        ninth_radio_button_xpath = '//*[@id="35"]/div[5]/div[1]/div[2]/span'
                        page.click(ninth_radio_button_xpath)

                        # Wow! Nagyon örülünk, hogy éttermünkben ilyen kellemes élményt tudtunk szerezni Neked! Kinek, vagy minek köszönhető ez?
                        with open("data/ratings.txt", "r") as file:
                            ratings = file.readlines()

                        popup_text = random.choice(ratings)
                        popup_text_field_xpath = '//*[@id="21"]/div[5]/div/input'
                        page.fill(popup_text_field_xpath, popup_text)

                        # Nemed?
                        genders = ['//*[@id="22"]/div[5]/div[1]/div[2]/span', '//*[@id="22"]/div[5]/div[2]/div[2]/span']

                        tenth_radio_button_xpath = random.choice(genders)
                        page.click(tenth_radio_button_xpath)

                        # Életkorod?
                        ages = ['//*[@id="23"]/div[5]/div[1]/div[2]/span', '//*[@id="23"]/div[5]/div[2]/div[2]/span',
                                '//*[@id="23"]/div[5]/div[3]/div[2]/span', '//*[@id="23"]/div[5]/div[4]/div[2]/span',
                                '//*[@id="23"]/div[5]/div[5]/div[2]/span', '//*[@id="23"]/div[5]/div[6]/div[2]/span']

                        eleventh_radio_button_xpath = random.choice(ages)
                        page.click(eleventh_radio_button_xpath)

                        # Milyen gyakran jársz McDonald's étterembe
                        frequency = ['//*[@id="24"]/div[5]/div[1]/div[2]/span',
                                     '//*[@id="24"]/div[5]/div[2]/div[2]/span',
                                     '//*[@id="24"]/div[5]/div[3]/div[2]/span',
                                     '//*[@id="24"]/div[5]/div[4]/div[2]/span',
                                     '//*[@id="24"]/div[5]/div[5]/div[2]/span',
                                     '//*[@id="24"]/div[5]/div[6]/div[2]/span']

                        twelfth_radio_button_xpath = random.choice(frequency)
                        page.click(twelfth_radio_button_xpath)

                        #Beküldés
                        time.sleep(60)
                        submit_button_xpath = '//*[@id="submit-wrapper"]/div[3]/button/span'
                        page.click(submit_button_xpath)

                        #Close window
                        time.sleep(5)
                        __delete_codeline(selected_list)
                        successful_upload_number += 1
                        print(f"Sikeres bevitel! Bevitelek száma: {successful_upload_number}")
                        browser.close()

                    else:
                        # Delete the wrong code
                        __delete_codeline(selected_list)
                        selected_list = __select_options(selected_type)
                        print("Hibás kód! Ok: Korábban már kitöltött/hibásan bevitt")
                        browser.close()
            else:
                __delete_codeline(selected_list)
                selected_list = __select_options(selected_type)
                print("Hibás kód! Ok: Üres sor")
                browser.close()