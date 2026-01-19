import configparser

from datetime import datetime

config = configparser.RawConfigParser()
config.read("./config/config.ini")


# from datetime import datetime
# import random
#
# config = configparser.RawConfigParser()
# config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('common info', 'baseURL')

    @staticmethod
    def getEmail():
        return config.get('common info', 'email')

    @staticmethod
    def get_verification_code():
        return config.get('common info', 'verification_code')

    # @staticmethod
    # def get_new_email():
    #     return config.get('common info', 'new_user_email')

    @staticmethod
    def get_new_email():
        """
        Generates a dynamic email using timestamp
        Example: vivek+20241125143022@arcitech.ai
        """
        base = config.get('common info', 'base_email')
        domain = config.get('common info', 'email_domain')
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        new_email = f"{base}+{timestamp}@{domain}"
        return new_email

    @staticmethod
    def get_first_name():
        return config.get('common info', 'first_name')

    @staticmethod
    def get_last_name():
        return config.get('common info', 'last_name')

    @staticmethod
    def get_phone_number():
        return config.get('common info', 'phone_number')

    @staticmethod
    def get_location():
        return config.get('common info', 'location')

    @staticmethod
    def get_project_name():
        return config.get('common info', 'project_name')

    @staticmethod
    def get_client_name():
        return config.get('common info', 'client_name')

    @staticmethod
    def get_total_area():
        return config.get('common info', 'total_area')

    @staticmethod
    def get_estimated_budget():
        return config.get('common info', 'estimated_budget')

    @staticmethod
    def get_district_code():
        return config.get('common info', 'district_code')

    @staticmethod
    def get_location_p():
        return config.get('common info', 'location_p')
