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


def analysis(input, depth, dim_list):
    list_len = 0
    if(isinstance(input, list)):
        if(len(input) >0):
            list_len = len(input)
            
            for temp in input:
                analysis(temp, depth, dim_list)
    
    if(isinstance(input, dict)):

        tmp = 'value:%s  description:%s '%(input['value'], input['description'])

        if(len(dim_list) < depth):
            dim_list.append([])
            
        dim_list[depth-1].append(tmp)
        
        if(input.has_key('details')):
            dim_list.append([])
            analysis(input['details'], depth+1, dim_list)
    

if __name__ == '__main__':
    encodejson = json.dumps(payload)


    r = requests.post("http://10.128.208.175:9200/appcenter-test/_search?explain",
                  data=encodejson)

    decodejson = json.loads(r.text)
    
    ##print r.text
    ###print decodejson

    a = decodejson['hits']['hits']
    ##print len(a)

    res_list = []
    for tmp in a:
        b= tmp['_explanation']
        ##print b.keys()
#######################################

##        print b['value'], b['description']
        ###print len(b['details'])

        tmp = 'value:%s  description:%s '%(b['value'], b['description'])
        
        dim_list = [[]]
        dim_list[0].append(tmp)
                                   
        analysis(b['details'], 2, dim_list)  ## start the depth is 2

        res_list.append(dim_list)

#######################################

    for a in res_list:
        print '\n'
        for b in a:
            num = a.index(b)
            t=''
            for i in range(num):
                t += '\t'
            for c in b:
                print t + c


    print res_list[0]
    print res_list[0][0]
    print res_list[0][0][0]

    
        


