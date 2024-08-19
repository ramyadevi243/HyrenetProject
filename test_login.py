import pytest
from pages.login_page import Login_Page


@pytest.mark.parametrize("username, password", [
    ("hyrenet+bugathon@guvi.in", "hyrenettest@123")
])
def test_login(driver, username, password):
    login_page = Login_Page(driver)
    login_page.boot()
    login_page.login(username, password)


@pytest.mark.parametrize("username, password", [
    ("hyrenet+bugathon@guvi.in", "hyrenettest@123")
])
def test_create_test(driver, username, password):
    login_page = Login_Page(driver)
    login_page.boot()
    login_page.login(username, password)
    login_page.create_test()
    login_page.logout()


@pytest.mark.parametrize("username, password", [
    ("hyrenet+bugathon@guvi.in", "hyrenettest@123")
])
def test_disable_test(driver, username, password):
    login_page = Login_Page(driver)
    login_page.boot()
    login_page.login(username, password)
    login_page.disable_test()
    login_page.logout()


@pytest.mark.parametrize("username, password", [
    ("hyrenet+bugathon@guvi.in", "hyrenettest@123")
])
def test_archive_test(driver, username, password):
    login_page = Login_Page(driver)
    login_page.boot()
    login_page.login(username, password)
    login_page.archive_test()
    login_page.logout()


@pytest.mark.parametrize("username, password", [
    ("hyrenet+bugathon@guvi.in", "hyrenettest@123")
])
def test_create_template(driver, username, password):
    login_page = Login_Page(driver)
    login_page.boot()
    login_page.login(username, password)
    login_page.create_template()
    login_page.logout()


@pytest.mark.parametrize("username, password", [
    ("hyrenet+bugathon@guvi.in", "hyrenettest@123")
])
def test_create_library(driver, username, password):
    login_page = Login_Page(driver)
    login_page.boot()
    login_page.login(username, password)
    login_page.create_library()
    login_page.logout()
