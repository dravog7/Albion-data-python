import requests
from typing import Union,Iterable,Optional

def exclude_keys(data: dict,keys: set):
    return {x: data[x] for x in data if x not in keys}

def reorder_price(data):
    result = dict()
    for entry in data:
        item = result.setdefault(entry["item_id"],{})
        city = item.setdefault(entry["city"],{})
        city.setdefault(entry["quality"],exclude_keys(entry,{"item_id","city","quality"}))
    return result

def get_price(item_ids: Union[str, Iterable[str]],
              locations: Optional[Union[str, Iterable[str]]]=None,
              qualities: Optional[Union[int, Iterable[int]]]=None):
    "Get the price of a set of items"

    if isinstance(item_ids,str):
        item_ids = [item_ids]
    if isinstance(locations,str):
        locations = [locations]
    if isinstance(qualities,int):
        qualities = [qualities]
    payload = {}
    if locations:
        payload["locations"] = ",".join(locations)
    if qualities:
        payload["qualities"] = ",".join(map(str,qualities))
    
    req = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/"+",".join(item_ids),
                       params=payload,
    )
    data = req.json()
    return reorder_price(data)

def reorder_history(data):
    result=dict()
    for entry in data:
        item = result.setdefault(entry["item_id"],{})
        city = item.setdefault(entry["location"],{})
        city.setdefault(entry["quality"],entry["data"])
    return result

def get_history(item_id: str,
                locations: Optional[Union[str, Iterable[str]]]=None,
                qualities: Optional[Union[int, Iterable[int]]]=None,
                date: str=None,
                time_scale: int=6):
    "Get the historical price of item_id"

    if isinstance(locations,str):
        locations = [locations]
    if isinstance(qualities,int):
        qualities = [qualities]

    payload = {
        "time-scale":time_scale,
    }
    if date:
        payload["date"] = date
    if locations:
        payload["locations"] = ",".join(locations)
    if qualities:
        payload["qualities"] = ",".join(map(str,qualities))

    req = requests.get("https://www.albion-online-data.com/api/v2/stats/History/"+item_id,
                       params=payload,
    )
    data = req.json()
    return reorder_history(data)
