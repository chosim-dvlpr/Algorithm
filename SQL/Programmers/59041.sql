-- 이름이 없는 동물은 제외, 결과는 이름 순으로 조회
SELECT NAME, count(NAME) AS COUNT FROM ANIMAL_INS 
GROUP BY NAME
HAVING count(NAME) > 1
ORDER BY NAME ASC
;
