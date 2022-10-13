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

Continuous Aggregates -
---

> [Continuous Aggregates](https://docs.timescale.com/api/latest/continuous-aggregates/)
> 
> [Continuous Aggregates Refresh Policy](https://docs.timescale.com/getting-started/latest/create-cagg/create-cagg-policy/)
