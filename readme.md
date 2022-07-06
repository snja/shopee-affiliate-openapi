# Shopee Affiliate Open API (Unofficial)
---- 
### Example Report:
```python
from datetime import datetime, timedelta
from shopee_affiliate import ShopeeAffiliate


appid = "" # Your appid
secret = "" # Your secret
# report yesterday
startdate = datetime.now() - timedelta(days=1)
enddate = datetime.now() - timedelta(days=1)

sa = ShopeeAffiliate(appid, secret)
res = sa.report(startdate, enddate)
conversion, estimation, startdate_, enddate_ = res
print("conversion:", conversion)
print("estimation:", estimation)
```
### Example Shortlink:
```python
from shopee_affiliate import ShopeeAffiliate
appid = "" # Your appid
secret = "" # Your secret
sa = ShopeeAffiliate(appid, secret)
res = sa.generateShortLink("https://www.shopee.co.id/mall")
print("shortlink:", res)
```
