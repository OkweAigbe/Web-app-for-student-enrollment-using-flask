import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x81\xdaS6\xf75\xe4riss\xfb\x0c[\xbb\x9b'

    MONGODB_SETTING = {'db' : 'HTA_Enrollment'}