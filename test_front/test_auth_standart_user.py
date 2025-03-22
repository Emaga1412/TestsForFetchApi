def open_website(page):
    page.goto('https://www.saucedemo.com/')


def search_field_login_and_enter(page):
    page.locator("#user-name").fill('standard_user')


def search_field_password_and_enter(page):
    page.locator("#password").fill('secret_sauce')


def click_the_login_button(page):
    page.locator("#login-button").click()



def test_auth_standart_user(page):
    open_website(page)
    search_field_login_and_enter(page)
    search_field_password_and_enter(page)
    click_the_login_button(page)


