# - * - coding: utf-8 - * -
from selenium import webdriver

EXECUTABLE_PATH = "C:\\FirefoxProfile\\geckodriver.exe"

driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)

url = 'http://hotel.meituan.com/beijing/xj6'
driver.get(url)
p = 'http://bj.meituan.com/meishi/api/poi/getPoiList?cityName=北京&cateId=17&areaId=0&sort=&dinnerCountAttrId=&page=3&userId=&uuid=566661aefae84b7d9ce1.1537924397.1.0.0&platform=1&partner=126&originUrl=http://bj.meituan.com/meishi/c17/pn3/&riskLevel=1&optimusCode=1'
_token = driver.execute_script("return window.Rohr_Opt.reload()", p)

print _token