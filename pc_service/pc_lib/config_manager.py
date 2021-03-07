import configparser

# Instantiating a new config parser
_config = configparser.ConfigParser()
_config.read('pc_lib/config.ini')


def base_url():
    return _config['DEFAULT']['base_url']



