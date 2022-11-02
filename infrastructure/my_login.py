import applications.login as login
import config

def my_login():
    return login.login(config.API_KEY, config.API_SECRET)

