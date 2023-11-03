-- CAR_RENTAL_COMPANY_CAR에서 여러 옵션 중 하나 이상의 옵션이 포함된 자동차 조회
-- 자동차 종류 별로 몇 대인지 출력
-- 자동차 종류 기준 오름차순
SELECT CAR_TYPE, count(CAR_TYPE) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%통풍시트%' OR
OPTIONS LIKE '%열선시트%' OR 
OPTIONS LIKE '%가죽시트%'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE ASC;
