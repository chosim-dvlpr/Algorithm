-- ANIMAL_INS.DATETIME보다 ANIMAL_OUTS.DATETIME이 더 빠른 동물의 아이디, 이름 조회
-- ANIMAL_INS.DATETIME이 빠른 순으로 정렬
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.NAME
FROM ANIMAL_INS LEFT JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
WHERE ANIMAL_INS.DATETIME > ANIMAL_OUTS.DATETIME
ORDER BY ANIMAL_INS.DATETIME ASC;