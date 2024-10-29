import pyautogui
import time
import configparser
import os

class ActionExecutor:
    def __init__(self):
        self.config_file = 'config.ini'
        self.config = configparser.ConfigParser()
        self.actions = []
        # 動作名稱和圖片文件名稱對應的列表
        self.actions_name = ["直接購買", "購買流程1", "下一步", "填寫購買資料", "送出結帳"]
        self.image_files = [f'purchase_button_{i + 1}.png' for i in range(len(self.actions_name))]

    def load_actions(self):
        # 讀取 config.ini 中的動作
        if not self.config.read(self.config_file):
            print("找不到配置檔案 config.ini，請先執行紀錄腳本")
            return False

        if 'Actions' in self.config:
            for key in sorted(self.config['Actions'], key=lambda x: int(x.split('_')[1])):
                self.actions.append(self.config['Actions'][key])
            print("動作已讀取完成")
            return True
        else:
            print("配置檔案中無動作數據")
            return False

    def execute_step(self, actions):
        scroll_accumulation = 0  # 用於累積 scroll 數值
        for action in actions:
            if action.startswith("scroll"):
                # 累積 scroll 的距離
                _, distance = action.split(":")
                scroll_accumulation += int(distance)
                print(f"累積滾動距離: {scroll_accumulation} 像素")

            elif action.startswith("click"):
                # 執行累積的 scroll 動作
                if scroll_accumulation != 0:
                    pyautogui.scroll(-scroll_accumulation)  # 向下滾動累積的距離
                    print(f"執行累積滾動: {scroll_accumulation} 像素")
                    scroll_accumulation = 0  # 重置累積

                # 執行 click 動作
                _, pos = action.split(":")
                x, y = map(int, pos.split(","))
                pyautogui.click(x, y)
                print(f"已點擊位置: ({x}, {y})")
                time.sleep(0.5)  # 等待0.5秒以模擬人類操作

    def wait_for_buttons_and_execute(self):
        action_idx = 0
        # 依序檢查 actions_name 和 image_files 中的每個項目
        for idx, (action_name, image_file) in enumerate(zip(self.actions_name, self.image_files)):
            print(f"正在等待『{action_name}』按鈕...")

            # 確認該步驟的按鈕圖像
            while True:
                try:
                    button_location = pyautogui.locateOnScreen(image_file, confidence=0.8)
                    if button_location:
                        print(f"已找到『{action_name}』按鈕，位置: {button_location}")
                        # 執行該按鈕之前的所有動作，直到下一個 click
                        actions_to_execute = []
                        while action_idx < len(self.actions):
                            action = self.actions[action_idx]
                            actions_to_execute.append(action)
                            action_idx += 1
                            if action.startswith("click"):
                                break
                        # 執行累積的動作
                        self.execute_step(actions_to_execute)
                        break  # 跳出內層循環，繼續檢測下一步的按鈕
                    time.sleep(1)  # 每1秒檢查一次
                except Exception as e:
                    print(f"等待網頁開啟，發生錯誤：{e}")

        print("所有按鈕已確認並依次點擊，完成自動化操作")

def main():
    executor = ActionExecutor()
    if executor.load_actions():
        # 依序檢測各步驟的按鈕並依次執行動作
        executor.wait_for_buttons_and_execute()

if __name__ == "__main__":
    main()
