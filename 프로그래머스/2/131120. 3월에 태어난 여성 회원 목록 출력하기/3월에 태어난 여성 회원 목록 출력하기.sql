-- 코드를 입력하세요
SELECT MEMBER_ID,MEMBER_NAME,GENDER,DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH from MEMBER_PROFILE 
where GENDER='W' 
AND SUBSTR(DATE_OF_BIRTH,6,2)='03'
AND TLNO IS NOT NULL
ORDER BY MEMBER_ID ASC