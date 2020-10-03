# Albion Data Python

A simple wrapper for the [Albion Data Project](https://www.albion-online-data.com/) API

## Features

- check price of items

    ```python
    # price of t4 and t5 bag at lymhurst quality 1
    get_price(["T4_BAG","T5_BAG"],"Lymhurst",1)
    ```

- check history of item

    ```python
    #get daily history of t4 bag at lymhurst of quality 1
    get_history("T4_BAG","Lymhurst",1,time_scale=24)
    ```

## NOTES

- The item ids and market names can be found [here](https://github.com/broderickhyman/ao-bin-dumps/tree/master/formatted)
