$ python3.6
Python 3.6.9 (default, Oct  8 2020, 12:12:24) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from lightfm import LightFM
>>> from lightfm.datasets import fetch_movielens
>>> from lightfm.evaluation import precision_at_k
>>> data = fetch_movielens(min_rating=5.0)
>>> model = LightFM(loss='warp')
>>> model.fit(data['train'], epochs=30, num_threads=2)
<lightfm.lightfm.LightFM object at 0x7f43ca9f59e8>
>>> precision_at_k(model, data['test'], k=5).mean()
0.051783357
>>> import pandas as pd
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pandas'
>>> df = pd.read_csv("data/candy.csv")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pd' is not defined
>>> df.sample(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'df' is not defined
>>> exit()
$ python3.6 -m pip install pandas
Collecting pandas
  Downloading pandas-1.1.5-cp36-cp36m-manylinux1_x86_64.whl (9.5 MB)
     |████████████████████████████████| 9.5 MB 8.0 MB/s 
Requirement already satisfied: numpy>=1.15.4 in /usr/local/lib/python3.6/dist-packages (from pandas) (1.19.5)
Collecting python-dateutil>=2.7.3
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
     |████████████████████████████████| 229 kB 66.6 MB/s 
Collecting pytz>=2017.2
  Downloading pytz-2026.2-py2.py3-none-any.whl (510 kB)
     |████████████████████████████████| 510 kB 67.9 MB/s 
Requirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil>=2.7.3->pandas) (1.11.0)
Installing collected packages: python-dateutil, pytz, pandas
Successfully installed pandas-1.1.5 python-dateutil-2.9.0.post0 pytz-2026.2
WARNING: You are using pip version 20.2.4; however, version 25.0.1 is available.
You should consider upgrading via the '/usr/bin/python3.6 -m pip install --upgrade pip' command.
$ ls data/
candy.csv  stars.csv
$ python3.6 << 'EOF'
> import pandas as pd
> import numpy as np
> import scipy.sparse as sp
> from sklearn.preprocessing import LabelEncoder
> from lightfm import LightFM
> from lightfm.cross_validation import random_train_test_split
> from lightfm.evaluation import precision_at_k
> 
> # Step 2: Load candy data
> df = pd.read_csv('data/candy.csv')
> print('=== Sample of candy data (5 rows) ===')
> print(df.sample(5))
> print()
> print('=== Single user zjohnson ===')
> print(df[df['user'] == 'zjohnson'])
> print()
> print('=== Unique items/users ===')
> print('Items shape:', df['item'].unique().shape)
> print('Users shape:', df['user'].unique().shape)
> print()
> 
> # Step 3: Build sparse matrix
> ratings = np.array(df['review'])
> users = np.array(df['user'])
> items = np.array(df['item'])
> 
> # Step 4: Encode strings to integers
> user_encoder = LabelEncoder()
> item_encoder = LabelEncoder()
> u = user_encoder.fit_transform(users)
> i = item_encoder.fit_transform(items)
> lu = len(np.unique(u))
> li = len(np.unique(i))
> print('=== Label Encoded ===')
> print('Number of unique users:', lu)
> print('Number of unique items:', li)
> print('First 10 item classes:', item_encoder.classes_[:10])
> print('First 10 user classes:', user_encoder.classes_[:10])
> 
> matrix = sp.coo_matrix((ratings, (u, i)), shape=(lu, li))
> print()
> print('=== Sparse matrix shape ===')
> print(matrix.shape)
> 
> # Step 5: Train/test split and model
> train, test = random_train_test_split(matrix, test_percentage=0.2)
> model = LightFM()
> model.fit(train)
> print()
> print('=== Model precision@10 ===')
> print(precision_at_k(model, test, k=10).mean())
> 
> # Step 6: Predict for a user
> user = 'zsmith'
> user_id = user_encoder.transform([user])[0]
> all_candy_ids = list(range(len(item_encoder.classes_)))
> preds = model.predict(user_id, all_candy_ids)
> 
> candies = pd.DataFrame(zip(item_encoder.classes_, preds), columns=['item','prediction']).sort_values('prediction', ascending=False)
> print()
> print('=== Top 10 candy recommendations for', user, '===')
> print(candies.head(10))
> 
> tried = df[df['user'] == user]['item'].values
> top5_new = list(candies[~candies['item'].isin(tried)]['item'].values[:5])
> print()
> print('=== Top 5 new candies (not yet tried) for', user, '===')
> print(top5_new)
> EOF
=== Sample of candy data (5 rows) ===
                                                    item  ... review
12519                    Hershey's Kisses Milk Chocolate  ...      4
15979  Bouquet of Fruits Valentine Chocolate Dipped S...  ...      5
14457                                  Brachs Candy Corn  ...      5
3891                Starburst Tropical Fruit Chews Candy  ...      2
5832                    Reese's Peanut Butter Cups White  ...      5

[5 rows x 3 columns]

=== Single user zjohnson ===
                                     item      user  review
2186                  Skittles Sour Candy  zjohnson       5
6022   Haribo Sour Gold Bears Gummi Candy  zjohnson       5
7919       Starburst Original Fruit Chews  zjohnson       5
8382                Sour Patch Watermelon  zjohnson       5
12304               Sour Patch Kids Candy  zjohnson       4

=== Unique items/users ===
Items shape: (142,)
Users shape: (2531,)

=== Label Encoded ===
Number of unique users: 2531
Number of unique items: 142
First 10 item classes: ['3 Musketeers Candy Bar' '3 Musketeers Miniature Bars' '5 Gum'
 'Airheads Bites Fruit' 'Airheads White Mystery'
 'Airheads Xtremes Sweetly Sour Candy Rainbow Berry'
 'Almond Joy Snack Size Bites' 'Altoids Curiously Strong Cinnamon Mints'
 'Bouquet of Fruits Valentine Chocolate Dipped Strawberries'
 'Brachs Candy Corn']
First 10 user classes: ['aaron67' 'aaron68' 'aaron73' 'abarker' 'abigail04' 'abigailwashington'
 'abigailwilcox' 'abrown' 'aclarke' 'acostanoah']

=== Sparse matrix shape ===
(2531, 142)

=== Model precision@10 ===
0.027780678
Traceback (most recent call last):
  File "<stdin>", line 57, in <module>
  File "/usr/local/lib/python3.6/dist-packages/lightfm/lightfm.py", line 830, in predict
    if len(user_ids) != len(item_ids):
TypeError: object of type 'numpy.int64' has no len()
$ python3.6 << 'EOF'
> import pandas as pd
> import numpy as np
> import scipy.sparse as sp
> from sklearn.preprocessing import LabelEncoder
> from lightfm import LightFM
> from lightfm.cross_validation import random_train_test_split
> from lightfm.evaluation import precision_at_k
> 
> df = pd.read_csv('data/candy.csv')
> ratings = np.array(df['review'])
> users = np.array(df['user'])
> items = np.array(df['item'])
> 
> user_encoder = LabelEncoder()
> item_encoder = LabelEncoder()
> u = user_encoder.fit_transform(users)
> i = item_encoder.fit_transform(items)
> lu = len(np.unique(u))
> li = len(np.unique(i))
> matrix = sp.coo_matrix((ratings, (u, i)), shape=(lu, li))
> train, test = random_train_test_split(matrix, test_percentage=0.2)
> model = LightFM()
> model.fit(train)
> 
> # Step 6: Predict
> user = 'zsmith'
> user_id = int(user_encoder.transform([user])[0])
> all_candy_ids = np.arange(len(item_encoder.classes_))
> preds = model.predict(user_id, all_candy_ids)
> 
> candies = pd.DataFrame({'item': item_encoder.classes_, 'prediction': preds}).sort_values('prediction', ascending=False)
> print('=== Top 10 candy recommendations for', user, '===')
> print(candies.head(10))
> 
> tried = df[df['user'] == user]['item'].values
> top5_new = list(candies[~candies['item'].isin(tried)]['item'].values[:5])
> print('=== Top 5 new candies (not tried yet) ===')
> print(top5_new)
> EOF
=== Top 10 candy recommendations for zsmith ===
                                                  item  prediction
134                                               Twix    1.356064
108                             Snickers Chocolate Bar    1.331948
140            Werther's Original Caramel Hard Candies    1.282892
74                         M&Ms Peanut Chocolate Candy    1.257335
72                           M&Ms Milk Chocolate Candy    1.201024
53   Jolly Rancher Hard Candy Original Flavors Asso...    1.188398
39                     Hershey's Kisses Milk Chocolate    1.157233
16                     Creme Savers Strawberries Rolls    1.142571
0                               3 Musketeers Candy Bar    1.136981
139                   Warheads Extreme Sour Hard Candy    1.110595
=== Top 5 new candies (not tried yet) ===
['Twix', 'Snickers Chocolate Bar', "Werther's Original Caramel Hard Candies", 'M&Ms Peanut Chocolate Candy', 'M&Ms Milk Chocolate Candy']