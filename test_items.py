from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_button_add_to_basket_exist(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket')))
    assert browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket'), 'на странице товара нет кнопки добавления в корзину'

