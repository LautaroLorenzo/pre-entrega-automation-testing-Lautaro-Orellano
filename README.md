# Pre-Entrega Automation Testing - SauceDemo

## ¿Qué es esto?

Un proyecto de automatización de pruebas para el sitio **saucedemo.com** usando Selenium y Pytest.

## ¿Qué hace?

Automatiza 3 funcionalidades principales:
1. **Login** - Hacer login en la página
2. **Catálogo** - Ver productos, nombre y precio
3. **Carrito** - Agregar producto al carrito

## ¿Qué necesito?

- Python 3.8 o superior
- pip (gestor de paquetes)

## Cómo instalarlo

1. Abre terminal en esta carpeta

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Cómo ejecutar los tests

Copia y pega esto en la terminal:

```bash
pytest tests/test_saucedemo.py -v
```

O para generar un reporte HTML:

```bash
pytest tests/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html
```

## ¿Qué verás?

Si todo funciona bien, verás en la terminal:

```
tests/test_saucedemo.py::TestLogin::test_login_exitoso PASSED
tests/test_saucedemo.py::TestCatalogo::test_titulo_pagina PASSED
tests/test_saucedemo.py::TestCatalogo::test_productos_visibles PASSED
tests/test_saucedemo.py::TestCatalogo::test_primer_producto PASSED
tests/test_saucedemo.py::TestCarrito::test_agregar_producto PASSED

================= 5 passed in 28.43s =================
```

## Estructura del proyecto

```
├── tests/
│   └── test_saucedemo.py      (los tests)
├── utils/
│   └── helpers.py             (funciones para los tests)
├── requirements.txt           (dependencias)
└── README.md                  (este archivo)
```

## ¿Cómo funciona?

### Estructura de clases

**LoginPage** - Para el login:
- `login(username, password)` - Hace login

**InventoryPage** - Para la página de productos:
- `get_title()` - Obtiene el título
- `get_products_count()` - Cuenta productos
- `get_first_product_info()` - Obtiene nombre y precio
- `add_first_product_to_cart()` - Agrega al carrito
- `get_cart_count()` - Cuenta items en carrito
- `go_to_cart()` - Va al carrito

**CartPage** - Para la página del carrito:
- `get_cart_items_count()` - Cuenta items
- `get_first_item_name()` - Obtiene nombre del primer item

### Estructura de tests

Hay 3 clases de tests:

1. **TestLogin** (1 test)
   - test_login_exitoso - Valida que puedas hacer login

2. **TestCatalogo** (3 tests)
   - test_titulo_pagina - Valida que el título sea "Products"
   - test_productos_visibles - Valida que haya productos
   - test_primer_producto - Obtiene nombre y precio del primer producto

3. **TestCarrito** (1 test)
   - test_agregar_producto - Agrega producto y verifica en carrito

## Credenciales para probar

Usuario: `standard_user`
Contraseña: `secret_sauce`

(Estas credenciales están hardcodeadas en los tests)

## Si algo no funciona

**Error: "Module not found"**
```bash
pip install -r requirements.txt
```

**Error: "ChromeDriver not found"**
- Verifica que tengas internet (se descarga automáticamente)
- Espera e intenta de nuevo

**Los tests tardan mucho o se cuelgan**
- El sitio puede estar lento
- Intenta más tarde o verifica tu conexión

## Autor

Proyecto de pre-entrega del curso de Automation Testing
