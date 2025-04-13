-- 코드를 입력하세요
SELECT count(USER_ID)
from USER_INFO
where AGE between 20 and 29 
and substr(JOINED,1,4)='2021'