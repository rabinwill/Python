

import NewWidgetTest_v2_J as sidekick
import IglooFinder_J as finder
import mobile_test_J as mobile

# =======================================================
# Here is the start of the actual Wolvarine Implementation Test
# =======================================================
sites = ['http://www.cnn.com/','http://www.yahoo.com/']
p_codes = ['1YL858QRNM','QICCYN009N']
product_list = ["inline_ad","dynamic_group_money","dynamic_group_weather_wide"]
mobile_product_list = ['']
deal='More #### Domains'
# Product List:
if(product_list != ['']):
    sidekick.test(sites,p_codes,product_list,deal)
if(mobile_product_list != ['']):
    mobile.test(sites,p_codes,mobile_product_list)
