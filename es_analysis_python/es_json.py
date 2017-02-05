#!/usr/bin/python  
#-*-coding:utf-8-*-


import json
import requests

payload ={
  "from" : 0,
  "size" : 1,
  "query" : {
    "bool" : {
      "must" : {
        "bool" : {
          "should" : [ {
            "multi_match" : {
              "query" : "app Manager",
              "fields" : [ "name*^100", "name_pinyin*^10", "description*^10"],
              "type" : "phrase_prefix"
            }
          }, {
            "multi_match" : {
              "query" : "app Manager",
              "fields" : [ "name*^100", "name_pinyin*^10", "description*^10"]
            }
          } ]
        }
      }
    }
  },
  "fields" : [ "id", "name" ]
}


def analysis(input, depth):
    list_len = 0
    if(isinstance(input, list)):
        if(len(input) >0):
            list_len = len(input)
            ##print len(input)
            for temp in input:
                analysis(temp, depth+1)
    
    if(isinstance(input, dict)):
        a=''
        for i in range(depth):
            a += '\t'
        print a + 'value:%s  description:%s '%(input['value'], input['description'])
        if(input.has_key('details')):
            analysis(input['details'], depth+1)
    

if __name__ == '__main__':
    encodejson = json.dumps(payload)

    ##print encodejson
    ##print '\n\n\n\n\n'

    r = requests.post("http://10.128.208.175:9200/appcenter-test/_search?explain",
                  data=encodejson)

    decodejson = json.loads(r.text)
    
    ##print r.text
    ###print decodejson

    a = decodejson['hits']['hits']
    ##print len(a)

    for tmp in a:
        b= tmp['_explanation']
        ##print b.keys()
#######################################

        print b['value'], b['description']
        ###print len(b['details'])
        analysis(b['details'], 1)


