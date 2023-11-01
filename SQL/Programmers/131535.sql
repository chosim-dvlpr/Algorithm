-- 2021년 가입한 회원 중 나이가 20세 ~ 29세인 회원 몇명인지 출력
SELECT count(USER_ID) as USERS
FROM USER_INFO
WHERE YEAR(JOINED) = '2021' and AGE BETWEEN 20 and 29;
