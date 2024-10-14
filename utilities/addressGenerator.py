import random

class AddressGenerator:
    usa_data = {
        "Maryland": {
            "province": "Maryland",
            "cities": {
                "Baltimore": "21201",
                "Annapolis": "21401",
                "Frederick": "21701",
                "Rockville": "20847"
            },
            "phone_prefix": "+1-410"
        },
        "Georgia": {
            "province": "Georgia",
            "cities": {
                "Atlanta": "30301",
                "Savannah": "31401",
                "Augusta": "30901",
                "Macon": "31201"
            },
            "phone_prefix": "+1-404"
        }
    }

    alias_types = ["Home", "Work", "Vacation", "Billing", "Shipping"]

    def generate_address(self):

        state = self.generate_state()
        city = self.generate_city(state)
        zipcode = self.generate_zipcode(state, city)
        phone = self.generate_phone(state)
        province = self.generate_province(state)


        alias = self.generate_alias()
        address_line_1 = self.generate_address_line_1()
        address_line_2 = self.generate_address_line_2()
        country = self.generate_country()


        return {
            "alias": alias,
            "address_line_1": address_line_1,
            "address_line_2": address_line_2,
            "city": city,
            "state": state,
            "province": province,
            "zipcode": zipcode,
            "country": country,
            "phone": phone
        }

    def generate_alias(self):
        return random.choice(AddressGenerator.alias_types)

    def generate_address_line_1(self):
        return f"{random.randint(100, 999)} {random.choice(['Main St', '1st Ave', 'Park Dr', 'Broadway'])}"

    def generate_address_line_2(self):
        return f"Apt {random.randint(1, 100)}" if random.random() > 0.5 else ""

    def generate_country(self):
        return "United States"

    def generate_state(self):
        return random.choice(list(AddressGenerator.usa_data.keys()))

    def generate_city(self, state):
        return random.choice(list(AddressGenerator.usa_data[state]["cities"].keys()))

    def generate_zipcode(self, state, city):
        return AddressGenerator.usa_data[state]["cities"][city]

    def generate_phone(self, state):
        phone_prefix = AddressGenerator.usa_data[state]["phone_prefix"]
        return f"{phone_prefix}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"

    def generate_province(self, state):
        return AddressGenerator.usa_data[state]["province"]


generator = AddressGenerator()
print(generator.generate_address())
