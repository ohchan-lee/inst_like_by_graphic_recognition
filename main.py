"""
Author : Ohchan Lee
Lst Modification : 2021. 02. 04.
ochan29286@gmail.com
https://github.com/ohchan-lee/inst_like_by_graphic_recognition
"""

import sys
import like_bot as lb

# 인스타 id 입력받기
id = sys.argv[1]


# 인스타 ps 입력받기
ps = sys.argv[2]

# 인스타 해시태그 입력받기
tag = sys.argv[3]

# 좋아요 버튼 파일 이름 입력받기
like_button = sys.argv[4]

# 몇 개의 게시물 누를건지 입력
click_num = int(sys.argv[5])


# 작업 수행
BOT = lb.LikeBot(like_button)

# 인스타 로그인
BOT.login(id, ps)

# 작업 수행
BOT.insta_jungdok(tag, click_num)