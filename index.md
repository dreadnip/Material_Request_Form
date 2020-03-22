# Material Request Form
### I've been smoking on gitbash all day bby

Here's my baby, I've been working on her for a long time. I've gotten this far. There is still a long way to go. At this point I can use it at work. The biggest speed increase for works sake is: sometimes we send out 20 items to the vendor. Each item has been hand typed for 15 years!<br/>
 I just added all the essential files to a "MAIN" folder as seen on the repository. I don't know if this #$%$ed everything up or not.<br/><br/> I also went back and wrote the paths that I had hard coded as `os.getcwd()`, so I think the program should work on someone else's machine. If you don't have excel (I assume you use some sort of sick hippy free dev master linux l33t trash) I don't know if the `openpyxl` module will work for you. So maybe just read through my code and see where I'm especially a gaper.<br/><br/> I'll list the additions I want to make later in the post.

__It should be noted: use 'b-0325' and 'a6258' as gage_id queries as test IDs__
## Questions for Sandy:
My first question is the largest. I think I'll eventually answer it by reading the "fucking manual", but maybe you can point me in the right direction. I'll try to be as concise as possible.

This chunk of code is from Main.py
```python
if choice == '1':
    # instantiate new item
    new_item = Item(index, *query.fetch(IO.get_gage_id()), IO.get_price(), IO.get_quantity())
    # add item to list of items to print for user
    items.append(new_item.to_list())
    # add item in stupid MRF formatting to xliste
    xliste.append(new_item.mrf_list_format())
    # increment the index
    index += 1
    continue
```
I specifically want to discuss: <br/>
`new_item = Item(index, *query.fetch(IO.get_gage_id()), IO.get_price(), IO.get_quantity()`

This is where I instantiate a new object.
* The index is for formatting within the excel document.
* The `*query.fetch(IO.get_gage_id())` is querying the DB with the gage ID the user enters.
The query instantiates:`self.gage_id, self.model_num, self.serial_num, self.mfg, self.desc, self.company, self.cert_template`
* Then `IO.get_price()` and `IO.get_quantity()` the user must input because this depends the quote from the manufacturer and the quanity.


Having the Item object is nice because I can use the methods from the class in the next two lines to move parts of the information around so that it can be easily read by the user and written to the excel document in the stupid corporate antiquated way (ie `Item.mrf_list_format()`)

But I am left lacking in the next few lines when I want to call the new_item object. See below:

```python
elif choice == '4':
    # xl.write_mrf_details(vendor, requestor, RMA, shipping info, date requested, date required, cert_type, interval, cal to mfg specs)
    # todo: why cant I write new_item.gage_id(), new_item.company()??
    #xl.write_project(index, new_item.gage_id(), new_item.company())
    xl.write_mrf_details('asc')
    xl.write_item(xliste)
    continue
```
Here I would like to use the new_item.gage_id() to fill out a cell in excel. But when I try to use this, pycharm rips a:
 ```python
Traceback (most recent call last):
  File "C:/Users/*User*/Documents/otv_v2/MAIN/Main.py", line 76, in <module>
    xl.write_project(index, new_item.gage_id(), new_item.company())
TypeError: 'str' object is not callable
```
When I use the de-bugger, I know that I overwrite new_item everytime I add a new item. This is probing at my misunderstanding of OOP. In the text book I have, they seem to always instantiate in terms of: `item1 = Item(arg1, arg2, arg3...)` `item2 = Item(arg1, arg2, arg3...)`

Then they can say `item1.method1()` `item2.method2` or whatever.

In my case, since I am overwriting the new_item everytime I instantiate, I can no longer act on item1 if I create item2. __This is my fundamental breakdown of how OOP fits into my program.__

luckily, we can only make an MRF for one company at a time. So item1 and item(n) will always have the same company. And, as I've written in the xl fucntion (from ExcelWrite.py):

```python
@staticmethod
def write_project(index, gageid, company):
    """writes the company name and gageid cells."""
    ws['D6'] = company
    # if there are more than one gageids being passed, write "multiple"
    if index > 0:
        ws['D7'] = 'MULTIPLE'
    else:
        ws['D7'] = str(gageid)
```

if there is more than one item, write 'MULTIPLE' in the cell. This is a dumb feature of the form. __A lot of this form is unnecessary__ but it is a good coding project to try to fit the bill to force me to solve the problem as is instead of reinventing the problem and solving it more gracefully.
## Desired Additions:
1. User login. The program would ask for initials and full name upon start. It would save this information in a pickled file within the run folder. The next time you use the program on that computer, it would see the pickled file and just read right out of that instead of asking you your name (with a choice of being able to change your user info). I tried to begin this process by creating a User object in Data.py but haven't gotten very far.

2. Dictionary list of {vendor:address}. This will be used to fill address the item is being sent to. (auto-fill vendor name?)

3. Dictionary list of {company:shipping acct #}. This will be used to obtain the UPS/Fedex shipping numbers of the company sending the items out to vendor. If this isn't filled then it would be CES's code or "Groud Ship Prepaid & Add"

4. Auto email. Send an email with pywin. attach the most recently added MRF from the designated file folder. Tell abbas to suck it.

5. other stuff I cant think of
