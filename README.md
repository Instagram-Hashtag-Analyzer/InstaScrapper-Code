better keep one README file here for git: 

****
python 3 without using selenium

1. cookie included in header, however chances after excessive accesses, login is required then `requests.session()` is needed

2. json str is obtained

3. parse to get the info of top posts

Dependencies: 
`BeautifulSoup`
`mysql.connector`


`python -m pip install -r requirements.txt` to install dependencies. 
I just `pip freeze` to the file, probably I should manually update `requirements.txt` to only include relevant packages.


Kindly run `mainlogic.py` as the `"__main__"` is inside there. 
