from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import time

def get_abstract_query_sparql(query):
    
    search = query
    if "'" in search:
        search = search.replace("'", '')
    search = search.replace(' ', '_')
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    print("---> QUERY: {}".format(search))
    
    sparql.setQuery("""

        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
        PREFIX dbpprop: <http://dbpedia.org/property/>

        SELECT DISTINCT 
            ?name
            ?abstract
            ?alternateTitle

        WHERE {
            ?instance a <http://dbpedia.org/ontology/Film>.
            ?instance foaf:name ?name .
            FILTER REGEX (?name, '^""" + search + """$', 'i').
            OPTIONAL {
                ?instance dbpedia-owl:abstract ?abstract .
                FILTER (LANG(?abstract) = 'en').
            }
            OPTIONAL {
                ?instance dbpprop:alternateTitle ?alternateTitle
            }
        }
    """)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    final_result = ''
    
    if len(results['results']['bindings']) is not 0:
        if len(results['results']['bindings'][0]['abstract']) is not 0:
            final_result = results['results']['bindings'][0]['abstract']['value']
        else:
            final_result = 'Found movie, but there is no ABSTRACT on DBpedia.'
    else:
        final_result = 'Movie not found on DBpedia by query title.'
    
    return final_result

start_time = time.time()

movies = pd.read_csv('ml-latest-small/movies.csv', low_memory=False)

movies['year'] = movies['title'].apply(lambda x: x[-5:-1])
movies['title'] = movies['title'].apply(lambda x: x[:-7])
movies['genres'] = movies['genres'].apply(lambda x: x.replace('|',', '))
movies['abstract'] = ''

aux_df = movies.copy()




aux = aux_df[0:1000]

for index, row in aux.iterrows():
    print('Index: {}'.format(index))
    aux.loc[index,'abstract'] = get_abstract_query_sparql(row.title)

aux.to_csv('results.csv')
print('\n\n============= DONE results.csv ')
elapsed_time = time.time() - start_time
print('TIME: {}'.format(elapsed_time))




aux = aux_df[1000:2000]

for index, row in aux.iterrows():
    print('Index: {}'.format(index))
    aux.loc[index,'abstract'] = get_abstract_query_sparql(row.title)

aux.to_csv('results_01.csv')
print('\n\n============= DONE results_01.csv ')
elapsed_time = time.time() - start_time
print('TIME: {}'.format(elapsed_time))




aux = aux_df[2000:3000]

for index, row in aux.iterrows():
    print('Index: {}'.format(index))
    aux.loc[index,'abstract'] = get_abstract_query_sparql(row.title)

aux.to_csv('results_02.csv')
print('\n\n============= DONE results_02.csv ')
elapsed_time = time.time() - start_time
print('TIME: {}'.format(elapsed_time))




aux = aux_df[3000:4000]

for index, row in aux.iterrows():
    print('Index: {}'.format(index))
    aux.loc[index,'abstract'] = get_abstract_query_sparql(row.title)

aux.to_csv('results_03.csv')
print('\n\n============= DONE results_03.csv ')
elapsed_time = time.time() - start_time
print('TIME: {}'.format(elapsed_time))




aux = aux_df[4000:5000]

for index, row in aux.iterrows():
    print('Index: {}'.format(index))
    aux.loc[index,'abstract'] = get_abstract_query_sparql(row.title)

aux.to_csv('results_04.csv')
print('\n\n============= DONE results_04.csv ')
elapsed_time = time.time() - start_time
print('TIME: {}'.format(elapsed_time))




aux = aux_df[5000:6000]

for index, row in aux.iterrows():
    print('Index: {}'.format(index))
    aux.loc[index,'abstract'] = get_abstract_query_sparql(row.title)

aux.to_csv('results_05.csv')
print('\n\n============= DONE results_05.csv ')
elapsed_time = time.time() - start_time
print('TIME: {}'.format(elapsed_time))




aux = aux_df[6000:7000]

for index, row in aux.iterrows():
    print('Index: {}'.format(index))
    aux.loc[index,'abstract'] = get_abstract_query_sparql(row.title)

aux.to_csv('results_06.csv')
print('\n\n============= DONE results_06.csv ')
elapsed_time = time.time() - start_time
print('TIME: {}'.format(elapsed_time))




aux = aux_df[7000:8000]

for index, row in aux.iterrows():
    print('Index: {}'.format(index))
    aux.loc[index,'abstract'] = get_abstract_query_sparql(row.title)

aux.to_csv('results_07.csv')
print('\n\n============= DONE results_07.csv ')
elapsed_time = time.time() - start_time
print('TIME: {}'.format(elapsed_time))




aux = aux_df[8000:9000]

for index, row in aux.iterrows():
    print('Index: {}'.format(index))
    aux.loc[index,'abstract'] = get_abstract_query_sparql(row.title)

aux.to_csv('results_08.csv')
print('\n\n============= DONE results_08.csv ')
elapsed_time = time.time() - start_time
print('TIME: {}'.format(elapsed_time))




aux = aux_df[9000:]

for index, row in aux.iterrows():
    print('Index: {}'.format(index))
    aux.loc[index,'abstract'] = get_abstract_query_sparql(row.title)

aux.to_csv('results_09.csv')
print('\n\n============= DONE results_09.csv ')
elapsed_time = time.time() - start_time
print('TIME: {}'.format(elapsed_time))