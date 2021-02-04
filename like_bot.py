"""
Author : Ohchan Lee
Lst Modification : 2021. 02. 04.
ochan29286@gmail.com
https://github.com/ohchan-lee/inst_like_by_graphic_recognition
"""

from selenium import webdriver
import pywinmacro as pw
import pyautogui as pg
import time

class LikeBot:
    def __init__(self, like_button):
        self.like_button = like_button
        self.tag_url = "https://instagram.com/explore/tags/"
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")

    def login(self, id, ps):
        # 로그인 페이지로 이동
        self.driver.get("https://www.instagram.com/accounts/login")

        # 로그인
        time.sleep(5)
        pw.key_press_once("tab")
        pw.typing(id)
        pw.key_press_once("tab")
        pw.typing(ps)
        pw.key_press_once("enter")
        time.sleep(5)

    def kill(self):
        self.driver.quit()

    def refresh(self):
        pw.key_press_once("f5")

    def search_tag(self, tag):
        self.driver.get(self.tag_url + tag)
        time.sleep(5)

    def select_picture(self):
        # 탭 키를 20번정도 누르기
        for i in range(12):
            pw.key_press_once("tab")

        # 엔터 누르기
        pw.key_press_once("enter")

        # 좋아요 누르는 함수
    def press_like(self):
        like_location = pg.locateCenterOnScreen(self.like_button)
        # print(like_location)
        if like_location:
            pw.click(like_location)
            time.sleep(3)

    def insta_jungdok(self, tag, click_num):
        self.search_tag(tag)
        self.select_picture()
        for i in range(click_num):
            self.press_like()
            pw.key_press_once("right_arrow")
            time.sleep(3)
