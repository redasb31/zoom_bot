from config import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import signal
import os



def join(meet, password,name):

    print(name)
    driver = webdriver.Chrome('/home/izouss/Downloads/ChromeDriver/chromedriver_linux64/chromedriver')
    driver.get(f'https://us04web.zoom.us/wc/join/{ZOOM_MEETING_LINK}?')    
    time.sleep(4)

    driver.find_element(By.ID, "inputname").send_keys(name)
    try:
        driver.find_element(By.ID, "inputpasscode").send_keys(passcode)
    except:
        print("passcode not required")
    driver.find_element(By.ID, "joinBtn").click()
    
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "preview-join-button").click()
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "footer-chat-button").click()
    for message in CHAT_MESSAGES:
        time.sleep(TIME_BETWEEN_MESSAGES)
        driver.find_element(By.CLASS_NAME, "chat-box__chat-textarea").send_keys(f'{message}\n')
    time.sleep(duration)
    #You can comment this section
    driver.stop_client()
    

def main():
    for i in range(len(BOT_NAMES)):
        newpid = os.fork()
        if newpid == 0:
            join(ZOOM_MEETING_LINK,ZOOM_MEETING_PASSWORD,BOT_NAMES[i])
            os._exit(0)

    remaining_bots = len(BOT_NAMES)
    while remaining_bots > 0:
        try:
            # Wait for child process to terminate
            pid, status = os.wait()
            remaining_bots -= 1
            print(f"Child {pid} terminated with status {status}")
        except KeyboardInterrupt:
            # Handle keyboard interrupt
            print("\nKeyboard interrupt received.")
            os.killpg(os.getpgid(0), signal.SIGINT)
            break
    if remaining_bots == 0:
        print("All child processes terminated.")

if __name__=="__main__":
    main()