# HelpingSanta
Implemented a **Flask based API** which takes hood capacity and available weights as request and returns the minimum number of weights to fill hood capacity

**Steps to run the APP**
  1. install python
  2. install <b>flask</b> package using the command <b>pip intall flask</b> in command prompt
  3. open command prompt and go to the directory where <b>hood_filler.py</b> resides
  4. run the command : <b>python hood_filler.py</b> and will see that code running on http://127.0.0.1:5000/
  5. post the request through postman or any other client; <b>URL</b> : http://localhost:5000/hoodfiller
  6. It will return the response in json format : {
    "present_weights": [
        10,
        10,
        10,
        5,
        2,
        2,
        2
    ]
}
 
 Note : Here is the attached screenshot : <b>reques_and_response.PNG</b> contains request and response from postman
