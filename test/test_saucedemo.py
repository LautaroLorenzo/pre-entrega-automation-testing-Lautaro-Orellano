import pytest
from utils.helpers import get_driver, LoginPage, InventoryPage, CartPage


@pytest.fixture
def driver():
    """Inicia el driver antes de cada test"""
    driver = get_driver()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


class TestLogin:
    """Tests de login"""
    
    def test_login_exitoso(self, driver):
        """Valida que el login sea exitoso"""
        # Hace login
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        # Verifica que llegó a la página de productos
        assert "inventory.html" in driver.current_url
        
        # Verifica que aparece el título "Products"
        inventory_page = InventoryPage(driver)
        assert inventory_page.get_title() == "Products"


class TestCatalogo:
    """Tests del catálogo de productos"""
    
    def test_titulo_pagina(self, driver):
        """Valida que el título sea 'Products'"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        inventory_page = InventoryPage(driver)
        titulo = inventory_page.get_title()
        
        assert titulo == "Products"
    
    def test_productos_visibles(self, driver):
        """Valida que haya productos visibles"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        inventory_page = InventoryPage(driver)
        cantidad = inventory_page.get_products_count()
        
        assert cantidad > 0
    
    def test_primer_producto(self, driver):
        """Obtiene nombre y precio del primer producto"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        inventory_page = InventoryPage(driver)
        producto = inventory_page.get_first_product_info()
        
        # Verifica que tiene nombre y precio
        assert producto["name"] != ""
        assert producto["price"] != ""
        
        print(f"Primer producto: {producto['name']} - {producto['price']}")


class TestCarrito:
    """Tests del carrito de compras"""
    
    def test_agregar_producto(self, driver):
        """Valida agregar un producto al carrito"""
        # Login
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        # Obtiene información del primer producto
        inventory_page = InventoryPage(driver)
        producto = inventory_page.get_first_product_info()
        nombre_producto = producto["name"]
        
        # Agrega al carrito
        inventory_page.add_first_product_to_cart()
        
        # Verifica que el contador del carrito es 1
        contador = inventory_page.get_cart_count()
        assert contador == 1
        
        # Va al carrito
        inventory_page.go_to_cart()
        
        # Verifica que el producto está en el carrito
        cart_page = CartPage(driver)
        item_en_carrito = cart_page.get_first_item_name()
        assert item_en_carrito == nombre_producto
