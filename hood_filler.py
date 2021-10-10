# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 2021

@author: Govi
"""


from flask import Flask, request, jsonify
app = Flask(__name__)


#the function compute minimum number of weights to fill hood capacity
def minimum_weigths_compute(present_weights, hood_capacity):
    
    '''
    Parameters
    ----------
    S : list
        list of weights
   
    n : integer
        available capacity

    Returns
    -------
    items : list
            a list of present weights to prepare the hood minimizing the number of items
    '''
    
    
    #total number of weight
    total_weights = len(present_weights)
    
    #creating table to store intermediate results
    table = [[0 for i in range(hood_capacity + 1)]
                for i in range(total_weights + 1)]
    
    #initializing the array to maximum values
    for i in range(1, hood_capacity + 1):
        table[0][i] = 10**9 - 1
    
    #iterating over weights
    for i in range(1, total_weights + 1):
        
        #couning minimum number of weights to represent 'j' using already seen weights
        for j in range(1, hood_capacity + 1):
            
            if (present_weights[i - 1] > j):
                table[i][j] = table[i - 1][j]
            else:
                #considerint minimum of {previous sequence weights count, new sequence weights count} of j
                table[i][j] = min(table[i - 1][j],
                                table[i][j - present_weights[i - 1]] + 1)
    
    row_index = total_weights
        
    #stores computed weight sequence
    items = []
    
    #iterate over table to find the weights
    while row_index>=1:
        if table[row_index-1][hood_capacity] > table[row_index][hood_capacity]:
            items.append(present_weights[row_index-1])
            hood_capacity = hood_capacity - present_weights[row_index-1]
        else:
            row_index = row_index - 1
   
    
    return items



@app.route('/hoodfiller', methods=['POST'])
def compute_weigths():
    
    try:
        content = request.json
        hood_capacity = content['hood_capacity']
        present_weights = content['present_weights']
        
        print('hood_capacity : ', hood_capacity)
        print('present_weights : ', hood_capacity)
    
    except Exception as e:
        print('Exception raised: ', e)
        return jsonify({"Exception raised" : str(e),
                        "message" : "please check the JSON request and try again",                        
                        })
    
    #calling the core logic function for computing the weights
    items = minimum_weigths_compute(present_weights, hood_capacity)
    
    print('solution : ', items)    
    
    return jsonify({"present_weights" : items})
    
    

if __name__ == '__main__':
    app.run(debug = False)
    
