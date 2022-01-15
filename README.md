# Data Scraping Assesment

### Meta-Data

* Library(s) : Scrapy🧹
* WebSite : chewy.com 🌐
* Tasks:

1. How do you extract categories of dog food from the page ([https://www.chewy.com/b/dog-288](https://www.chewy.com/b/dog-288)). Explain and write a python script.
2. write a python script to get each product url in for dog food , wet-food category ([https://www.chewy.com/b/dog-288](https://www.chewy.com/b/dog-288))
3. write a function to detect how many pages of products in a category. So given the category url the function should output the number of pages
4. Write a python script for extracting the following attributes in a product url, for example [https://www.chewy.com/pedigree-adult-complete-nutrition/dp/141438](https://www.chewy.com/pedigree-adult-complete-nutrition/dp/141438)

### **Task 1:**

Script name : categories.py
Extraction Fields : Categories, Total Products in perticular category, category url
Output File : Category-data.json

**How to run spider:**

**Run scrapy runspider [Spider name] ..E.g**

`scrapy runspider categories.py`

**For storing the data into json file you can run ..E.g**

`scrapy runspider categories.py -o category-data.json`


### Task 2 and 3:

Script name : wetfoods.py
Extraction Fields : Product Name, Product Url
Output File : productsurls.json

**How to run spider:**

**Run scrapy runspider[Spider name] ..E.g**

`scrapy runspider wetfoods.py`

**For storing the data into json file you can run ..E.g**

`scrapy runspider wetfoods.py -o productsurls.json `

*Note: Total Pages count is in the same script you can check out scripts line 18-20*


### Task 4:

Script name: productdataspy.py

Extraction Fields :

```
            ProductName 
            Price 
            Description 
            Attributes 
            Brand
            Brand_url
            ingredients 
            Key Benefits
            Guaranteed Analysis
            Images
```

Output File : data.json


**How to run spider:**

**Run scrapy runspider [Spider name] ..E.g**

`scrapy runspider productdataspy.py`

**For storing the data into json file you can run ..E.g**

`scrapy runspider productdataspy.py -o data.json `


### **Bonus🎁:**

I have created scrapy project which extracts all the doog food data available on the site within few minitues.
Path : `/dogfoodspy `
Extraction Fields :

```
            ProductName 
            Price 
            Description 
            Attributes 
            Brand
            Brand_url
            ingredients 
            Key Benefits
            Guaranteed Analysis
            Images
```

Output File : allfoods.json

**How to run spider:**

**Run scrapy crawl [Spider name] ..E.g**

`scrapy crawl chweyspy`

**For storing the data into json file you can run ..E.g**

`scrapy crawl chweyspy -o allfoods.json `


📱📞

For any quries you can reach to me you can find contact information on my Github Profile
