from datetime import datetime

from bs4 import BeautifulSoup
import json
import requests
import time

class WGGesucht(object):
    def __init__(self):
        # setup params
        with open("./config.json", "r") as js_file:
            self.config = json.load(js_file)
        self.mail = self.config["mail"]
        self.password = self.config["password"]
        self.offer_id = self.config["offerId"]
        self.intervall = self.config["intervall"]

    def log(self, text):
        timestamp = "[{}]".format(datetime.now().strftime("%H:%M:%S.%f")[:-3])
        print(timestamp, text)

    def setup_session(self):
        # setup session
        self.s = requests.Session()
        self.s.headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36]"

    def login(self):
        url = "https://www.wg-gesucht.de/ajax/api/Smp/api.php?action=login"
        data = {"login_email_username": self.mail,
                "login_password": self.password,
                "login_form_auto_login":"1",
                "display_language":"de"}

        response = self.s.post(url, json=data)
        if response.status_code is 200:
            self.log("Logged in to {}".format(self.mail))
            return True
        return False

    def update_offer(self):
        url = "https://www.wg-gesucht.de/angebot-bearbeiten.html?action=update_offer&offer_id={}".format(self.offer_id)
        response = self.s.get(url)
        soup = BeautifulSoup(response.text, "lxml")

        user_id = soup.find("a", {"class": "logout_button"}).get("data-user_id")

        # optional options
        options = soup.find("select", {"id": "category"})
        if options.find("option", selected=True):
            category = options.find("option", selected=True).get("value")
        else:
            category = options.find("option").get("value")

        options = soup.find("select", {"id": "rent_type"})
        if options.find("option", selected=True):
            rent_type = options.find("option", selected=True).get("value")
        else:
            rent_type = options.find("option").get("value")

        options = soup.find("select", {"id": "house_type"})
        if options.find("option", selected=True):
            house_type = options.find("option", selected=True).get("value")
        else:
            house_type = options.find("option").get("value")

        options = soup.find("select", {"id": "floor_level"})
        if options.find("option", selected=True):
            floor_level = options.find("option", selected=True).get("value")
        else:
            floor_level = options.find("option").get("value")

        options = soup.find("select", {"id": "flatshare_friendly"})
        if options.find("option", selected=True):
            flatshare_friendly = options.find("option", selected=True).get("value")
        else:
            flatshare_friendly = options.find("option").get("value")

        options = soup.find("select", {"id": "parking_option"})
        if options.find("option", selected=True):
            parking_option = options.find("option", selected=True).get("value")
        else:
            parking_option = options.find("option").get("value")

        options = soup.find("select", {"id": "flatshare_females"})
        if options.find("option", selected=True):
            flatshare_females = options.find("option", selected=True).get("value")
        else:
            flatshare_females = options.find("option").get("value")

        options = soup.find("select", {"id": "flatshare_males"})
        if options.find("option", selected=True):
            flatshare_males = options.find("option", selected=True).get("value")
        else:
            flatshare_males = options.find("option").get("value")

        options = soup.find("select", {"id": "searching_for_gender"})
        if options.find("option", selected=True):
            searching_for_gender = options.find("option", selected=True).get("value")
        else:
            searching_for_gender = options.find("option").get("value")

        options = soup.find("select", {"id": "smoking_is_allowed"})
        if options.find("option", selected=True):
            smoking_is_allowed = options.find("option", selected=True).get("value")
        else:
            smoking_is_allowed = options.find("option").get("value")

        options = soup.find("select", {"id": "energy_certificate_type"})
        if options.find("option", selected=True):
            energy_certificate_type = options.find("option", selected=True).get("value")
        else:
            energy_certificate_type = options.find("option").get("value")

        options = soup.find("select", {"id": "energy_source"})
        if options.find("option", selected=True):
            energy_source = options.find("option", selected=True).get("value")
        else:
            energy_source = options.find("option").get("value")

        options = soup.find("select", {"id": "energy_efficiency_class"})
        if options.find("option", selected=True):
            energy_efficiency_class = options.find("option", selected=True).get("value")
        else:
            energy_efficiency_class = options.find("option").get("value")

        options = soup.find("select", {"id": "green_energy"})
        if options.find("option", selected=True):
            green_energy = options.find("option", selected=True).get("value")
        else:
            green_energy = options.find("option").get("value")

        options = soup.find("select", {"id": "heating"})
        if options.find("option", selected=True):
            heating = options.find("option", selected=True).get("value")
        else:
            heating = options.find("option").get("value")

        options = soup.find("select", {"id": "internet_dsl_speed"})
        if options.find("option", selected=True):
            internet_dsl_speed = options.find("option", selected=True).get("value")
        else:
            internet_dsl_speed = options.find("option").get("value")

        options = soup.find("select", {"id": "bath_availability"})
        if options.find("option", selected=True):
            bath_availability = options.find("option", selected=True).get("value")
        else:
            bath_availability = options.find("option").get("value")

        options = soup.find("select", {"id": "kitchen_availability"})
        if options.find("option", selected=True):
            kitchen_availability = options.find("option", selected=True).get("value")
        else:
            kitchen_availability = options.find("option").get("value")

        # setting data
        data = {
            "ad_title": soup.find("input", {"id": "ad_title"}).get("value"),
            "autocompinp": soup.find("input", {"id": "autocompinp"}).get("value"),
            "country_code": soup.find("input", {"id": "country_code"}).get("value"),
            "countrymanuel": soup.find("input", {"id": "countrymanuel"}).get("value"),
            "city_name": soup.find("input", {"id": "city_name"}).get("value"),
            "city_id": soup.find("input", {"id": "city_id"}).get("value"),
            "category": category,
            "rent_type": rent_type,
            "ad_type": soup.find("input", {"id": "ad_type"}).get("value"),
            "display_language": soup.find("input", {"id": "display_language"}).get("value"),
            "csrf_token": soup.find("input", {"class": "csrf_token"}).get("value"),
            "privacy_statement_wg_gesucht": soup.find("input", {"name": "privacy_statement_wg_gesucht"}).get("value"),
            "district_id": soup.find("select", {"id": "district_id"}).find("option", selected=True).get("value"),
            "district_custom": soup.find("input", {"id": "district_custom"}).get("value"),
            "no_districts_found": soup.find("input", {"id": "no_districts_found"}).get("value"),
            "district": soup.find("input", {"id": "district"}).get("value"),
            "street": soup.find("input", {"id": "street"}).get("value"),
            "postcode": soup.find("input", {"id": "postcode"}).get("value"),
            "available_from_Day": soup.find("select", {"id": "available_from_Day"}).find("option", selected=True).get("value"),
            "available_from_Month": soup.find("select", {"id": "available_from_Month"}).find("option", selected=True).get("value"),
            "available_from_Year": soup.find("select", {"id": "available_from_Year"}).find("option", selected=True).get("value"),
            "available_from_day": soup.find("select", {"id": "available_from_Day"}).find("option", selected=True).get("value"),
            "available_from_month": soup.find("select", {"id": "available_from_Month"}).find("option", selected=True).get("value"),
            "available_from_year": soup.find("select", {"id": "available_from_Year"}).find("option", selected=True).get("value"),
            "available_to_Day": soup.find("select", {"id": "available_to_Day"}).find("option", selected=True).get("value"),
            "available_to_Month": soup.find("select", {"id": "available_to_Month"}).find("option", selected=True).get("value"),
            "available_to_Year": soup.find("select", {"id": "available_to_Year"}).find("option", selected=True).get("value"),
            "available_to_day": soup.find("select", {"id": "available_to_Day"}).find("option", selected=True).get("value"),
            "available_to_month": soup.find("select", {"id": "available_to_Month"}).find("option", selected=True).get("value"),
            "available_to_year": soup.find("select", {"id": "available_to_Year"}).find("option", selected=True).get("value"),
            "date_from_before_to": soup.find("input", {"id": "date_from_before_to"}).get("value"),
            "house_type": house_type,
            "floor_level": floor_level,
            "property_size": soup.find("input", {"id": "property_size"}).get("value"),
            "flatshare_property_size": soup.find("input", {"id": "flatshare_property_size"}).get("value"),
            "handicap_accessible": soup.find("select", {"id": "handicap_accessible"}).find("option", selected=True).get("value"),
            "number_of_rooms": soup.find("input", {"id": "number_of_rooms"}).get("value"),
            "flatshare_friendly": flatshare_friendly,
            "parking_option": parking_option,
            "public_transport_in_minutes": soup.find("input", {"id": "public_transport_in_minutes"}).get("value"),
            "rent_costs": soup.find("input", {"id": "rent_costs"}).get("value"),
            "utility_costs": soup.find("input", {"id": "utility_costs"}).get("value"),
            "bond_costs": soup.find("input", {"id": "bond_costs"}).get("value"),
            "equipment_costs": soup.find("input", {"id": "equipment_costs"}).get("value"),
            "other_costs": soup.find("input", {"id": "other_costs"}).get("value"),
            "flatshare_inhabitants_total": soup.find("select", {"id": "flatshare_inhabitants_total"}).find("option", selected=True).get("value"),
            "flatshare_females": flatshare_females,
            "flatshare_males": flatshare_males,
            "flatshare_size": soup.find("input", {"id": "flatshare_size"}).get("value"),
            "flatmates_aged_from": soup.find("input", {"id": "flatmates_aged_from"}).get("value"),
            "flatmates_aged_to": soup.find("input", {"id": "flatmates_aged_to"}).get("value"),
            "flatmates_age": soup.find("input", {"id": "flatmates_age"}).get("value"),
            "searching_for_gender": searching_for_gender,
            "searching_for_age_from": soup.find("input", {"id": "searching_for_age_from"}).get("value"),
            "searching_for_age_to": soup.find("input", {"id": "searching_for_age_to"}).get("value"),
            "searching_age": soup.find("input", {"id": "searching_age"}).get("value"),
            "smoking_is_allowed": smoking_is_allowed,
            "flatshare_types": soup.find("input", {"id": "flatshare_types"}).get("value"),
            "flatshare_type_1": soup.find("input", {"id": "flatshare_type_1"}).get("value"),
            "flatshare_type_12": soup.find("input", {"id": "flatshare_type_12"}).get("value"),
            "lang_de": soup.find("input", {"id": "lang_de"}).get("value"),
            "lang_en": soup.find("input", {"id": "lang_en"}).get("value"),
            "lang_es": soup.find("input", {"id": "lang_es"}).get("value"),
            "freetext_property_description": soup.find("textarea", {"id": "freetext_property_description"}).text,
            "freetext_area_description": soup.find("textarea", {"id": "freetext_area_description"}).text,
            "freetext_flatshare": soup.find("textarea", {"id": "freetext_flatshare"}).text,
            "freetext_other": soup.find("textarea", {"id": "freetext_other"}).text,
            "freetexts": soup.find("input", {"id": "freetexts"}).get("value"),
            "offer_telephone": soup.find("input", {"id": "offer_telephone"}).get("value"),
            "offer_mobile": soup.find("input", {"id": "offer_mobile"}).get("value"),
            "i_am": soup.find("select", {"id": "i_am"}).find("option", selected=True).get("value"),
            "energy_certificate_type": energy_certificate_type,
            "energy_consumption": soup.find("input", {"id": "energy_consumption"}).get("value"),
            "energy_source": energy_source,
            "energy_building_year": soup.find("input", {"id": "energy_building_year"}).get("value"),
            "energy_efficiency_class": energy_efficiency_class,
            "green_energy": green_energy,
            "heating": heating,
            "internet_dsl": soup.find("input", {"id": "internet_dsl"}).get("value"),
            "internet_wlan": soup.find("input", {"id": "internet_wlan"}).get("value"),
            "internet_dsl_speed": internet_dsl_speed,
            "furnished": soup.find("input", {"id": "furnished"}).get("value"),
            "bath_availability": bath_availability,
            "bath": soup.find("input", {"id": "bath"}).get("value"),
            "kitchen_availability": kitchen_availability,
            "laminate": soup.find("input", {"id": "laminate"}).get("value"),
            "washing_machine": soup.find("input", {"id": "washing_machine"}).get("value"),
            "dishwasher": soup.find("input", {"id": "dishwasher"}).get("value"),
            "balcony": soup.find("input", {"id": "balcony"}).get("value"),
            "cellar": soup.find("input", {"id": "cellar"}).get("value"),
        }

        # add timestamp as change
        other = data["freetext_other"]
        splitted = other.split("¯\_(ツ)_/¯")
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        signature = "https://github.com/iamnotturner/keepMeUp"
        data["freetext_other"] = splitted[0].strip() + "\n\n\n¯\_(ツ)_/¯ {ts}\n{sig}".format(ts=ts, sig=signature)

        # update offer
        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Host": "www.wg-gesucht.de",
            "Origin": "https://www.wg-gesucht.de",
            "Referer": url,
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "X-Authorization": "Bearer " + self.s.cookies["X-Access-Token"],
            "X-Client-Id": "wg_desktop_website",
            "X-Dev-Ref-No": self.s.cookies["X-Dev-Ref-No"],
            "X-Requested-With": "XMLHttpRequest",
            "X-User-Id": user_id
        }
        self.s.headers.update(headers)
        url = "https://www.wg-gesucht.de/api/offers/{oid}/users/{uid}".format(oid=self.offer_id, uid=user_id)

        response = self.s.put(url, json=data)
        if response.status_code is 200:
            self.log("Successfully updated offer https://www.wg-gesucht.de/{}.html".format(self.offer_id))
            return True
        return False

    def run(self):
        while True:
            self.setup_session()
            login_state = self.login()
            if login_state:
                update_state = self.update_offer()
                if update_state:
                    self.log("Sleeping {} seconds until logging in and updating the offer again!".format(self.intervall))
                    time.sleep(self.intervall)
                else:
                    self.log("Cannot update offer {}. Quitting!".format(self.offer_id))
                    quit()
            else:
                self.log("Cannot login to account {}. Quitting!".format(self.mail))
                quit()

if __name__ == "__main__":
    wgg = WGGesucht()
    wgg.run()