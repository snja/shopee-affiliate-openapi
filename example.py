from datetime import datetime, timedelta
from shopee_affiliate import ShopeeAffiliate

sa = ShopeeAffiliate("<appid>","<secret>")
res = sa.report(datetime.now()-timedelta(days=5))
conversion, estimation, startdate, enddate = res
print("conversion:", conversion)
print("estimation:", estimation)
