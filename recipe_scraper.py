from bs4 import BeautifulSoup
import urllib2
import re


req = urllib2.Request("http://www.foodnetwork.com/recipes/food-network-kitchen/almost-famous-spinach-artichoke-dip-recipe-1973257")
res = urllib2.urlopen(req)
doc = res.read()

soup = BeautifulSoup(doc, 'html.parser')
ingredients = soup.find_all(class_="o-Ingredients__a-ListItemText")



for i in ingredients:
    qty = 1
    nums = re.findall("\d\/\d|\d+", i.text)
    if(len(nums) != 0):
        if("/" in nums[0]):
            frac = nums[0];
            qty = float(float(frac[0])/float(frac[2]))
        else:
            qty = float(nums[0])

    if(len(nums) > 1):
        if("/" in nums[1]):
            frac = nums[1]
            qty += float(float(frac[0])/float(frac[2]))

    print(qty)
