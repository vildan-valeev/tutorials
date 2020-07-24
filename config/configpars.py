import configparser

config = configparser.ConfigParser()

video = input()

config.read('config.ini')
print(config.sections())
print(config['media']['video'])
config['media']['video'] = video

with open('config.ini', 'w') as configfile:
    config.write(configfile)
