SELECT ANIMAL_TYPE, count(ANIMAL_TYPE) AS count FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE ASC;