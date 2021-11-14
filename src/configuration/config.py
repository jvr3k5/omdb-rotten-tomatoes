import argparse
import configparser
import logging
import os


class GlobalConfiguration:
    def __init__(self, location: str) -> None:
        logging.info("Reading configuration file")
        self.content = configparser.ConfigParser()
        self.content.read(location)

    #         logging.info("====================================================================")
    #         logging.info('Loaded configuration:')
    #         [logging.info(f"{section}.{key}={self.content[section][key]}")
    #          for section in self.content.sections()
    #          for key in self.content[section]]
    #         logging.info("====================================================================")

    def get_property(self, section: str, property_name: str) -> str:
        return self.content[section][property_name]

    def add_property(self, section: str, property_name: str, value) -> None:
        if not self.content.has_section(section):
            self.content.add_section(section)

        self.content[section][property_name] = value


def read_config() -> GlobalConfiguration:
    logging.info("Using default config file.")
    config = GlobalConfiguration(f"{os.path.dirname(__file__)}/../config.ini")

    return config
