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


for index, row in movies.iterrows():
    print('Index: {}'.format(index))
    row.abstract = get_abstract_query_sparql(row.title)

movies.to_csv('results.csv')
print('\n\n============= DONE.')
elapsed_time = time.time() - start_time
print('TIME: {}'.format(elapsed_time))