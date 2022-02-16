/***************************
Author: eeysirhc
Date written: 2022-02-09
Last updated: 2022-02-15
Objective: pull all liquidity pair pricing over time
***************************/

CREATE VIEW price_data AS 
SELECT
pool_id,
a_x.ticker as x_ticker,
x_amount/POWER(10,a_x.decimals) as x_amount,
a_y.ticker as y_ticker,
y_amount/POWER(10,a_y.decimals) as y_amount,
(x_amount/POWER(10,a_x.decimals))*(y_amount/POWER(10,a_y.decimals)) as k,
a_x.ticker || '/' || a_y.ticker as ticker,
(y_amount/POWER(10,a_y.decimals))/(x_amount/POWER(10,a_x.decimals)) as price,
a_y.ticker || '/' || a_x.ticker as yx_ticker,
(y_amount/POWER(10,a_y.decimals))/(x_amount/POWER(10,a_x.decimals)) as yx_price,
a_x.ticker || '/' || a_y.ticker as xy_ticker,
(x_amount/POWER(10,a_x.decimals))/(y_amount/POWER(10,a_y.decimals)) as xy_price,
gindex as global_index
FROM pools p
LEFT JOIN assets a_x ON a_x.id = p.x_id
LEFT JOIN assets a_y ON a_y.id = p.y_id

/* erg/sigusd: remove bug data */
WHERE gindex not in (12981672,12979979) 

;