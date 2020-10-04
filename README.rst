Albion Data Python
==================

A simple wrapper for the `Albion Data Project <https://www.albion-online-data.com/>`__ API

Install
-------

Install using pip

.. code:: bash

        python3 -m pip install albion-data

Features
--------

-  check price of items

.. code:: python

    # price of t4 and t5 bag at lymhurst quality 1
    from albion_data import get_price
    get_price(["T4_BAG","T5_BAG"],"Lymhurst",1)

-  check history of item

.. code:: python

    #get daily history of t4 bag at lymhurst of quality 1
    from albion_data import get_history
    get_history("T4_BAG","Lymhurst",1,time_scale=24)

-  System for making arithemetic expressions

The values are lazy loaded.

.. code:: python

    #check if t4 leather refining is profitable in fort sterling without focus
    from albion_data import Var
    t4leather = Var("T4_LEATHER","Fort Sterling","sell_price_min")
    t4hide = Var("T4_HIDE","Fort Sterling","sell_price_min")
    t3leather = Var("T3_LEATHER","Fort Sterling","sell_price_min")
    if (2 * t4hide + t3leather) < t4leather: #triggers a single API call
        print("refine t4hide")
    else:
        print("not worth it")

NOTES
-----

-  The item ids and market names can be found
   `here <https://github.com/broderickhyman/ao-bin-dumps/tree/master/formatted>`__

-  Use &,\|,~ for logical and,or,not when making arithemetic expressions
   with Var. `why not
   and,or,not? <https://stackoverflow.com/questions/32311518/is-it-possible-to-overload-logical-and-in-python>`__

-  the PYPI name of package and all API might change until v1
