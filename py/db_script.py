# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 13:02:36 2019

@author: zhengjt
"""

drop table public.future_his_data;
CREATE TABLE public.future_his_data
(
    date date NOT NULL,
    future_code "varchar" NOT NULL,
    future_name "varchar",
    open numeric(20, 3),
    high numeric(20, 3),
    low numeric(20, 3),
    close numeric(20, 3),
    last_close numeric(20, 3),
    vol numeric(20, 3),
    ma5 numeric(20, 3),
    ma10 numeric(20, 3),
    ma20 numeric(20, 3),
    ma30 numeric(20, 3),
    ma40 numeric(20, 3),
    ma60 numeric(20, 3),
    ma120 numeric(20, 3),
    datatime timestamp without time zone default(now()),
    PRIMARY KEY (date, future_code)
)
WITH (
    OIDS = FALSE
);

ALTER TABLE public.future_his_data
    OWNER to postgres;
COMMENT ON TABLE public.future_his_data
    IS '期货历史数据';
    
    

INSERT INTO public.future_his_data(
	date, future_code, open)
	VALUES ('2019-06-28', 'L1909', 2333.01);
    
 'date','future_code','future_name','read_data_time','open','high','low','close','vol'   
drop table public.future_real_data;
CREATE TABLE public.future_real_data
(
    date date NOT NULL,
    future_code "varchar" NOT NULL,
    future_name "varchar",
    read_data_time "varchar" NOT NULL,
    open numeric(20, 3),
    high numeric(20, 3),
    low numeric(20, 3),
    close numeric(20, 3),
    vol numeric(20, 3),
    datatime timestamp without time zone default(now()),
    PRIMARY KEY (date, future_code, read_data_time)
)
WITH (
    OIDS = FALSE
);

ALTER TABLE public.future_real_data
    OWNER to postgres;
COMMENT ON TABLE public.future_real_data
    IS '期货实时数据';
    