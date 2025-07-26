from selenium.webdriver.common.by import By
from time import sleep
from bases.base_page import BasePage
from pages import CHECKOUT_BUTTON_XPATH

class Cart_Page(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def do_findproduct(self,product_tag='T-Shirt'):
        products_description = self.find_all(By.XPATH, "//div[@class='inventory_item_description']")
        matched_products = []

        for product in products_description:
            try:
                name_element = product.find_element(By.XPATH, ".//div[@class='inventory_item_name ']")
                if product_tag in name_element.text:
                    matched_products.append(name_element)

                    # Tìm nút Add to cart tương ứng
                    add_to_cart_button = product.find_element(By.XPATH, ".//button[contains(text(), 'Add to cart')]")
                    if add_to_cart_button:
                        add_to_cart_button.click()
                        print(f"Added to cart: {name_element.text}")
                        print(add_to_cart_button)
                        sleep(1)
            except Exception as e:
                print(f"Error processing product: {e}")
        if not matched_products:
            print(f"No matching products found in: {product_tag}")
            return matched_products
        
    def click_ckeckout(self):
        self.click(By.XPATH, CHECKOUT_BUTTON_XPATH)











    #     products = self.find_all(By.XPATH, "//div[@class='inventory_item_description']//a[@href]//div")
    #     matched_products = []
    #     # Duyệt qua từng phần tử và kiểm tra tên
    #     for product in products:

    #         #print(f"Checking product: {product.text}")
    #         if product_tag in product.text:
    #          print(f"Matched: {product.text}")
    #          matched_products.append(product) 
    #          addtocard_element = (By.XPATH, "//div[@class='inventory_item_description']//button")
    #          print(addtocard_element)
    
    #     if not matched_products:
    #         print(f"No matching products found in: {product_tag}")
    #         return matched_products


    # def click_addtocart(self):
    #     self.click(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")

