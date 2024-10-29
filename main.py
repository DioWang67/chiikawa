from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# 启动Chrome浏览器
driver = webdriver.Chrome()

# 打开Google网站
driver.get("https://www.google.com")

# 显式等待搜索框加载完成
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)

# 在搜索框中输入关键词并点击搜索按钮
search_box.send_keys("寬宏售票系統")  # 替换为你要搜索的购票网站的名称
search_box.send_keys(Keys.RETURN)

# 显式等待搜索结果加载完成
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'寬宏售票系統')]"))
)

# 在搜索结果中点击购票网站的链接
link = driver.find_element(By.XPATH, "//h3[contains(text(),'寬宏售票系統')]")  # 替换为购票网站名称的文本
link.click()

# 进行其他操作，比如登录、选择票种、填写订单等
# 需要根据具体网站的操作流程进行定制

# 创建一个ActionChains对象
action_chains = ActionChains(driver)

# 将鼠标移动到页面的空白处（假设坐标为(100, 100)）
action_chains.move_by_offset(100, 100)

# 在空白处点击一下
action_chains.click()

# 执行操作
action_chains.perform()


# 在搜索结果中点击购票网站的链接
link = driver.find_element(By.XPATH, "//*[@id="show-area"]/div[2]/div/a[3]/img")  # 替换为购票网站名称的文本
link.click()

# 等待用户手动关闭浏览器
input("Press Enter to close the browser...")

# 关闭浏览器
# driver.quit()
