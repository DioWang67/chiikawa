from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class ShoppingBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        
    def monitor_and_buy(self, url):
        self.driver.get(url)
        print("開始監控商品頁面...")
        
        while True:
            try:
                # 檢查直接結帳按鈕
                checkout_button = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '直接結帳')]"))
                )
                
                # 檢查加入購物車按鈕
                cart_button = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '加入購物車')]"))
                )
                
                print("找到可購買按鈕！開始購買流程...")
                
                # 選擇商品規格（如果需要）
                try:
                    spec_select = self.driver.find_element(By.XPATH, "//select[@class='spec-select']")
                    spec_select.click()
                    # 選擇第一個選項
                    spec_select.find_elements(By.TAG_NAME, "option")[1].click()
                except:
                    print("無需選擇規格或規格已選擇")
                
                # 點擊直接結帳
                checkout_button.click()
                print("已點擊直接結帳")
                
                # 等待登入頁面（如果需要）
                try:
                    login_form = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.ID, "login-form"))
                    )
                    print("請手動完成登入流程")
                    break
                except:
                    print("無需登入或已登入")
                    break
                
            except TimeoutException:
                print("按鈕尚未可用，繼續監控...")
                self.driver.refresh()
                time.sleep(1)  # 避免過於頻繁刷新
                
            except Exception as e:
                print(f"發生錯誤: {str(e)}")
                time.sleep(1)
    
    def close(self):
        self.driver.quit()

def main():
    url = "https://myship.7-11.com.tw/general/detail/GM2410245775640"
    bot = ShoppingBot()
    try:
        bot.monitor_and_buy(url)
    except KeyboardInterrupt:
        print("\n程式已停止")
    finally:
        bot.close()

if __name__ == "__main__":
    main()