/***************************
Author: eeysirhc
Date written: 2022-02-09
Objective: pull all liquidity pair pricing over time
***************************/


\copy (
SELECT
pool_id,
a_x.ticker as x_ticker,
x_amount/POWER(10,a_x.decimals) as x_amount,
a_y.ticker as y_ticker,
y_amount/POWER(10,a_y.decimals) as y_amount,
(x_amount/POWER(10,a_x.decimals))*(y_amount/POWER(10,a_y.decimals)) as k,
(y_amount/POWER(10,a_y.decimals))/(x_amount/POWER(10,a_x.decimals)) as price,
a_x.ticker || '/' || a_y.ticker as ticker,
gindex as global_index

FROM pools p
LEFT JOIN assets a_x ON a_x.id = p.x_id
LEFT JOIN assets a_y ON a_y.id = p.y_id

/* erg/sigusd: remove bug data */
WHERE gindex not in (12981672,12979979) 

ORDER BY gindex ASC) to 'price-data.csv' with csv header

;
