import names
import random
import csv

mail = ['gmail.com', 'hotmail.com', 'yahoo.com']
store = ['Parkshopping', 'Canoas Shopping', 'Canoas', 'Porto Alegre', 'Iguatemi', 'Shopping Total', 'Praia de Belas', 'Bourbon Country', 'Zaffari Canoas', 'Conjunto Comercial', 'Moinhos de Vento', 'São Leopoldo', 'Aeroporto', 'Sapucaia', 'Esteio']

csv_consumer_file = open('../data/mock_consumer.csv','w', newline='', encoding='utf-8')
csv_store_file = open('../data/mock_store.csv','w', newline='', encoding='utf-8')
csv_brand_file = open('../data/mock_brand.csv','w', newline='', encoding='utf-8')



def generate_name():

    csv_consumer_file.write('consumer_id,first_name,last_name,email,brand_id,store_id\n')

    for names_index in range(200):
        consumer_id = names_index
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        email = first_name + last_name + '@' + random.choice(mail)
        brand_id = random.randint(0, 10)
        store_id = random.randint(0, 10)

        csv_consumer_file.write(str(consumer_id) + ',' + first_name + ',' + last_name + ',' + email + ',' + str(brand_id) + ',' + str(store_id) +'\n')

        names_index+=1

def generate_store():
    csv_store_file.write('brand_id,store_id,store_name,total_purchase_amount\n')

    for store_index in range(10):
        brand_id = random.randint(0,10)
        store_id = store_index
        store_name = str(names.get_last_name()) + ' ' + random.choice(store)
        total_purchase_amount = random.randint(0,10000)

        csv_store_file.write(str(brand_id) + ',' + str(store_id) + ',' + store_name + ',' +str(total_purchase_amount) + '\n')

generate_store()
generate_name()