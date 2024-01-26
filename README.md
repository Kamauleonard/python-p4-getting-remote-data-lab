# Getting Remote Data Lab

## Learning Goals

- Practice sending GET requests using Python.
- Build a reusable class for sending requests and handling responses.

***

## Key Vocab

- **Request**: an attempt by one machine to contact another over the internet.
- **Client**: an application or machine that accesses services being provided by
  a server through the internet.
- **Web Server**: a combination of software and hardware that uses Hypertext
  Transfer Protocol (HTTP) and other protocols to respond to requests made over
  the internet.

***

## Introduction 

It is time to practice building out your own class for retrieving remote data.
In this lab, you are tasked with building a generic `GetRequester` class. This
class will be able to take in a URL on initialization and send an HTTP GET
request on command. You will also need to build a method for dealing with
requests that return JSON.

When complete, you will have a simple, but versatile class for getting
information from all kinds of sources over the internet.

***

## Instructions

All work should be completed in `lib/GetRequester.py`. Use the previous
code-along on getting data from APIs as a reference when building out your
class.

Start by creating a `GetRequester` class. This class should be able to
initialize with a string URL.

The `GetRequester` class should have a `get_response_body` method that sends a
GET request to the URL passed in on initialization. This method should return
the _body_ of the response.

The `GetRequester` class should have a `load_json` method that should use
`get_response_body` to send a request, then return a Python list or dictionary
made up of data converted from the response of that request.

The tests in this lab will use your code to send a request for some JSON data,
located at
[https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json][].
Read the test error messages for additional as you work for additional
information. Don't forget to import the necessary Python modules and classes!

[https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json]: https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json

This is a **test-driven lab**. Run `pipenv install` to create your virtual
environment and `pipenv shell` to enter the virtual environment. Then run
`pytest -x` to run your tests. Use these instructions and `pytest`'s error
messages to complete your work in the `lib/` folder.

Once all of your tests are passing, commit and push your work using `git` to
submit.

***

## Conclusion

Once you've successfully passed the tests, from this lesson's directory, you
should be able to open repl, use
`lib/GetRequester.py`, and send out some requests!

```py
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
get_requester.load_json()
#=> [{"name"=>"Daniel", "occupation"=>"LG Fridge Salesman"}, {"name"=>"Joe", "occupation"=>"WiFi Fixer"}, {"name"=>"Avi", "occupation"=>"DJ"}, {"name"=>"Howard", "occupation"=>"Mountain Legend"}]
```

This class won't work for all cases but is a good starting place to get us off
the ground. We can now augment our applications with data from the internet!
Combined with our knowledge of Python, we have all the tools we need to start
building smarter Python applications populated with real data.

***

## Resources

- [GET - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)
- [HTTP methods - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [requests](https://requests.readthedocs.io/en/latest/)
- [Python JSON](https://docs.python.org/3/library/json.html)
