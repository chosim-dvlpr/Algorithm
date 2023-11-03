-- ANIMAL_OUTS의 DATETIME은 있지만 ANIMAL_INS의 DATETIME은 없는 동물 찾기
-- LEFT JOIN으로 생성 후 ANIMAL_INS에 DATETIME이 없는 것만 찾음
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
FROM ANIMAL_OUTS LEFT JOIN ANIMAL_INS ON ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
WHERE ANIMAL_INS.ANIMAL_ID IS NULL
ORDER BY ANIMAL_ID
