import pyautogui
import time
import keyboard
import configparser
import os

class PositionRecorder:
    def __init__(self):
        self.config_file = 'config.ini'
        self.config = configparser.ConfigParser()
        self.actions = []
        print("按 'p' 鍵記錄點擊位置，按 'o' 鍵滾輪向下滾動300並記錄滾動，按 'q' 鍵保存並退出")

    def record_actions(self):
        scroll_count = 0
        while True:
            if keyboard.is_pressed('p'):
                pos = pyautogui.position()
                self.actions.append(f"click:{pos[0]},{pos[1]}")
                print(f"記錄點擊位置: {pos}")
                time.sleep(0.5)

            elif keyboard.is_pressed('o'):
                scroll_count += 1
                self.actions.append("scroll:300")
                pyautogui.scroll(-300)  # 滾動300像素
                print(f"滾動了300像素，累計滾動次數: {scroll_count}")
                time.sleep(0.5)

            elif keyboard.is_pressed('q'):
                if not self.config.has_section('Actions'):
                    self.config.add_section('Actions')
                
                # 保存所有動作至 config.ini
                for idx, action in enumerate(self.actions):
                    self.config.set('Actions', f'action_{idx}', action)
                
                with open(self.config_file, 'w') as configfile:
                    self.config.write(configfile)
                
                print("動作已保存至 config.ini 檔案")
                break

def main():
    recorder = PositionRecorder()
    recorder.record_actions()

if __name__ == "__main__":
    main()
