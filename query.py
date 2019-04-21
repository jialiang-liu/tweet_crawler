from elasticsearch import Elasticsearch

es = Elasticsearch(['localhost:9200'])
#dsl = {
#        'query' : {
#            'match' : {
#                'time' : '2019'
#                }
#            }
#        }
result = es.search(index = "idx_twp",doc_type = "twitter_twp",body = {"query":{"match_all":{}}})
for hit in result['hits']['hits']:
    print(hit)

#doc = {
#            'size' : 10000,
#                'query': {
#                            'match_all' : {}
#                                }
#                }
#
#res = es.search(index="idx_twp", doc_type='twitter_twp', body=doc,scroll='1m')
#scroll = res['_scroll_id']
#res2 = es.scroll(scroll_id = scroll, scroll = '1m')
#print(res2)
