from selenium.webdriver.common.by import By
from time import sleep
from bases.base_page import BasePage


class Inventory_Page(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.PRODUCTS_DESCRIPTION_XPATH = "//div[@class='inventory_item_description']"
        self.PRODUCT_NAME_ELEMENT_XPATH = ".//div[@class='inventory_item_name ']"
        self.ADD_TO_CART_BUTTON_XPATH = ".//button[contains(text(), 'Add to cart')]"
        self.CART_BUTTON_XPATH = "//a[@class='shopping_cart_link']"

    def do_add_to_cart(self,product_tag):
        self.do_findproduct(product_tag)
        self.click_cart()
      

    def do_findproduct(self,product_tag):
        products_description = self.find_all(By.XPATH, self.PRODUCTS_DESCRIPTION_XPATH)
        matched_products = []

        for product in products_description:
            try:
                product_name_element = product.find_element(By.XPATH, self.PRODUCT_NAME_ELEMENT_XPATH)
                if product_tag in product_name_element.text:
                    matched_products.append(product_name_element)

                    # Tìm nút Add to cart tương ứng
                    add_to_cart_button = product.find_element(By.XPATH, self.ADD_TO_CART_BUTTON_XPATH)
                    if add_to_cart_button:
                        add_to_cart_button.click()
                        print(f"Added to cart: {product_name_element.text}")
                        print(add_to_cart_button)
                        sleep(1)
            except Exception as e:
                print(f"Error processing product: {e}")
        if not matched_products:
            print(f"No matching products found in: {product_tag}")
            return matched_products
        
    def click_cart(self):
        self.click(By.XPATH, self.CART_BUTTON_XPATH)