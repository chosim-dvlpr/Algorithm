-- 보호소에 들어온 동물의 이름은 몇개인지?
-- NULL은 계산 X, 중복 제거
SELECT count(DISTINCT(NAME)) AS count FROM ANIMAL_INS 
WHERE NAME IS NOT NULL;
