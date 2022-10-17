Timescale DB
============

TimescaleDB inherits all of PostgresSQL; what works in psql works in timescale


Hypertables and chunks -
---

> [Hypertables and chunks](https://docs.timescale.com/getting-started/latest/create-hypertable/)
> 
> ![Hypertables over chunks](https://user-images.githubusercontent.com/38424838/195527076-057bbc7e-64a4-484b-8388-59e191e64064.png)

#### Create hypertable -

> When you create a hypertable, it is automatically partitioned on the time column you provide as the second parameter to create_hypertable().
>
> Also, TimescaleDB automatically creates an index on the time column.
> 
> ![Create hypertable](https://user-images.githubusercontent.com/38424838/195527738-fc42c5a4-bce4-4e57-94fb-1a5357f75a3f.png)

Continuous Aggregates & Refresh Policy -
---

> [Continuous Aggregates](https://docs.timescale.com/api/latest/continuous-aggregates/)
> 
> [Continuous Aggregates Refresh Policy](https://docs.timescale.com/getting-started/latest/create-cagg/create-cagg-policy/)
> 
#### Manually call a refresh policy -
> CALL refresh_continuous_aggregate(
 'stock_candlestick_daily',
 now() - INTERVAL '1 week',
 now()
 );


#### Create an automatic refresh policy over sample continuous aggregate table "stock_candlestick_daily"

>> SELECT add_continuous_aggregate_policy('stock_candlestick_daily',
>> 
>> start_offset => INTERVAL '3 days',
>>
>> end_offset => INTERVAL '1 hour',
>>
>> schedule_interval => INTERVAL '1 days');
>
> * This policy runs once a day, as set by "schedule_interval".
> * When it runs, it materializes data from between 3 days ago and 1 hour ago, as set by "start_offset" and "end_offset".
> * Offset times are calculated relative to query execution time. The executed query is the one defined in the continuous aggregate stock_candlestick_daily.

Data Compression -
---

> [Compression of hypertable](https://docs.timescale.com/getting-started/latest/compress-data/)
> 
> _SELECT add_compression_policy('stocks_real_time', INTERVAL '2 weeks');_


Informational views
---

#### See all metadata and settings information for continuous aggregates -
> SELECT * FROM timescaledb_information.continuous_aggregates;

#### See all inormation about all jobs registered with the automation framework -
> SELECT * FROM timescaledb_information.jobs;

#### Remove a specific refresh policy 
> SELECT remove_continuous_aggregate_policy('table_name');

#### Call refresh policy
> CALL refresh_continuous_aggregate('table_name', '2020-01-01', '2020-02-01');
