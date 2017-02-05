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



class Node:
 
    def __init__(self, data):
        self._data = data
        self._children = []
 
    def getdata(self):
        return self._data
 
    def getchildren(self):
        return self._children
 
    def add(self, node):
        self._children.append(node)
 
    def go(self, data):     ## find child node
        for child in self._children:
            if child.getdata() == data:
                return child
        return None
 
class Tree:
 
    def __init__(self):
        self._head = node('header')
 
    def linktohead(self, node):
        self._head.add(node)
 
    def insert(self, path, data):
        cur = self._head
        for step in path:
            if cur.go(step) == None:
                return False
            else:
                cur = cur.go(step)
        cur.add(node(data))
        return True
 
    def search(self, path):
        cur = self._head
        for step in path:
            if cur.go(step) == None:
                return None
            else:
                cur = cur.go(step)
        return cur


#########################################
    
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

    a = decodejson['hits']['hits']

    res_list = []
    for tmp in a:
        b= tmp['_explanation']
#######################################

##        print b['value'], b['description']
        ###print len(b['details'])

        tmp = 'value:%s  description:%s '%(b['value'], b['description'])
        
        ##dim_list = [[]]
        ##dim_list[0].append(tmp)

        node = Node(tmp)
        
        tree = Tree()

        tree.linktohead(node)
                                   
        analysis(b['details'], 2, node)  ## start the depth is 2

        res_list.append(dim_list)

#######################################



    
        


