from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def get_element(self, locator):
        """Obtiene un elemento de la página"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator):
        """Hace click en un elemento"""
        element = self.get_element(locator)
        element.click()
    
    def type_text(self, locator, text):
        """Escribe texto en un elemento"""
        element = self.get_element(locator)
        element.clear()
        element.send_keys(text)


class LoginPage(BasePage):
    
    # Localizadores
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    def login(self, username, password):
        """Realiza el login en la página"""
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
        # Espera a que cargue la página de productos
        self.wait.until(EC.url_contains("inventory.html"))


class InventoryPage(BasePage):
    
    # Localizadores
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    
    def get_title(self):
        """Obtiene el título de la página"""
        element = self.get_element(self.PRODUCTS_TITLE)
        return element.text
    
    def get_products_count(self):
        """Obtiene la cantidad de productos"""
        products = self.driver.find_elements(*self.PRODUCT_ITEMS)
        return len(products)
    
    def get_first_product_info(self):
        """Obtiene nombre y precio del primer producto"""
        products = self.driver.find_elements(*self.PRODUCT_ITEMS)
        first_product = products[0]
        
        name = first_product.find_element(*self.PRODUCT_NAME).text
        price = first_product.find_element(*self.PRODUCT_PRICE).text
        
        return {"name": name, "price": price}
    
    def add_first_product_to_cart(self):
        """Agrega el primer producto al carrito"""
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        buttons[0].click()
    
    def get_cart_count(self):
        """Obtiene el número de items en el carrito"""
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except:
            return 0
    
    def go_to_cart(self):
        """Navega al carrito"""
        self.click_element(self.CART_LINK)
        self.wait.until(EC.url_contains("cart.html"))


class CartPage(BasePage):
    
    # Localizadores
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    
    def get_cart_items_count(self):
        """Obtiene la cantidad de items en el carrito"""
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)
    
    def get_first_item_name(self):
        """Obtiene el nombre del primer item en el carrito"""
        items = self.driver.find_elements(*self.CART_ITEMS)
        if items:
            return items[0].find_element(*self.ITEM_NAME).text
        return None


def get_driver():
    """Crea e inicializa el driver de Chrome"""
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    return driver
