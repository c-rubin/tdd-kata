# tdd-kata

## Step 1

firstly, I created a test class, and just made sure it worked correctly <br><br>

made new test, to check if api exists (ran it and failed it, as TDD demands)

successfuly passed the existing test (http code must be different from 404) <br><br>

made new test to check if api is successfuly responding (http code = 200)

successfuly passed above test <br><br>

in the next test, I will actually check if the response is a valid json

made the test pass <br><br>

now, I will actually test the contents of the json. I will use `https://binlist.net/` for assigning values.

It seems that the BinList has a limit of 5 requests/hour, so I made a mock class for it and also separated the data gathering logic away from api.py

made the test pass (also updated some of the previous tests) <br><br>

## Step 2

For this step I created a new test file

Now I will repeat some of the tests that I did in the previous test file (which I'm not commenting) and will change the code so that it passes the tests <br><br>

finally, at the json attributes test, I will check that the json is returned as wanted <br><br>

Now I will check for multiple requests made <br><br>

Now I will calculate the payload size. I checked the size of the previous test's payload online and it was 45B. Hopefully this is correct, so I set it as checking value.

Fortunately the online calculator proved to be correct and the test passed <br><br>

Finally, the last part of this step is to store the information on a file. I will be using serialization for this, so that data is saved even after stopping the program. However, this would require to change previous tests as well after changing the code to pass this current test.

Actually it didn't require changes for previous tests because I used a mock (which I deleted afterwards) <br><br>

## Containerization

Lastly, I created a dockerfile, where I execute the tests (which execute the apis)

To run it, open terminal in current directory and run these commands

`docker build -t <name> .`

`docker run -p 5000:5000 <name>`

First, the tests will be run, afterwards the APIs, which can be accessed through

`http://localhost:5000//api/card-scheme/verify/<cardNum>>`



`http://localhost:5000//api/card-scheme/stats?start=<num>&limit=<num>`

<br>

Example:

`http://localhost:5000//api/card-scheme/verify/45717361`



`http://localhost:5000//api/card-scheme/stats?start=1&limit=1`
