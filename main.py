# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from import_data import *
import pandas as pd
import numpy as np
import csv

# Dataframe train
df_order_products_prior = importation_file("/Users/Ricou/Desktop/ANDRE/machine_learning/instacart/instacart-market-basket-analysis/order_products__prior.csv")
#df_order_products_prior = df_order_products_prior[['order_id','product_id']]

df_orders = importation_file("/Users/Ricou/Desktop/ANDRE/machine_learning/instacart/instacart-market-basket-analysis/orders.csv")
#df_orders = df_orders[['order_id','user_id']]
#print(df_orders[:1])
df_products = importation_file("/Users/Ricou/Desktop/ANDRE/machine_learning/instacart/instacart-market-basket-analysis/products.csv")
#df_products = df_products[['product_id','department_id']]
#print(df_products[:1])
#print(df_order_products_prior[:1])
#print(df_orders[:1])
#print(df_products[:1])

#orders_products_df=pd.merge(df_orders, df_order_products_prior, how='inner', on='order_id')#inner par défaut
#orders_products_df= pd.merge(orders_products_df, df_products,how='inner', on='product_id') #inner par défaut
#orders_products_df= orders_products_df[['user_id','order_id','product_id','department_id']]
#print(orders_products_df[:1])
#on a user_id, order_id, product_id



def read_orders(N,path="/Users/Ricou/Desktop/ANDRE/machine_learning/instacart/instacart-market-basket-analysis/orders.csv"):
    df_orders = pd.read_csv(path)
    df_orders = df_orders[['order_id','user_id']]
    return df_orders[df_orders['user_id'].isin(range(N+1))]

def read_orders_products(path="/Users/Ricou/Desktop/ANDRE/machine_learning/instacart/instacart-market-basket-analysis/order_products__prior.csv"):
    orders_products_df=pd.read_csv(path)
    return orders_products_df[['order_id','product_id']]


#Etape suivante: récupérer les order_id pour chaque user_id
#retourne les order_id pour les N premiers clients
n_clients = 100
orders_df = read_orders(n_clients)
#print(orders_df)

# retourne pour chaque client ['user_id','order_id','product_id','department_id']
orders_products_df= pd.merge(orders_df, df_order_products_prior,how='inner', on='order_id') #inner par défaut
orders_products_df= pd.merge(orders_products_df, df_products,how='inner', on='product_id') #inner par défaut
orders_products_df= orders_products_df[['user_id','order_id','department_id']]

#print(orders_products_df)

#Création d'un fichier data avec l'échantillon de clients
data = orders_products_df.to_csv("/Users/Ricou/Desktop/ANDRE/machine_learning/instacart/instacart-market-basket-analysis/merged-sample.csv",index= False)
data = orders_products_df.values

#voir le fichier test.py qui travaillent sur les n_clients déclarés








#print(order_products_prior.head(1))
#print("df_train shape",order_products_prior.shape)
