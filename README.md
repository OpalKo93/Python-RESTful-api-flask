# Python-RESTful-api-flask

<img align="right" width="100" src="https://image.flaticon.com/icons/svg/265/265682.svg">

[Live Demo](https://pages.github.com/)

## Introduction

In the different programming languages, variables can be defined, but these variables have some capacities, and sometimes we will need more capacity than the primitive variables that are provided to us.

In unsigned numbers, a number is obtained in the domain defined by the number of bits, in general it can be defined as follows:

<p align="center">
  <img src="https://i.imgur.com/S7Kjih1.png" width="220" />
</p>

However, the number of bits of the primitive variables is limited, so for example in most modern languages `unsigned long` is the largest type where you can define a negative number that is usually set to contain 32 bits. I.e. x ^ 32.

Therefore these `long numbers` are held in an **int array** at the form of each digit is a cell in the array.<br />
For example: The number: `123456789` will be represented as: `[1, 2, 3, 4, 5, 6, 7, 8, 9]`


## API explanation

### The HTTP request is done with POST method

I chose to use that method because of several reasons:

1. Even though according to many resources:

> [RFC 2616](https://tools.ietf.org/html/rfc2616) (Hypertext Transfer Protocol — HTTP/1.1) states there is no limit to the length of a query string (section 3.2.1). [RFC 3986](https://tools.ietf.org/html/rfc3986) also states there is no limit, but indicates the hostname is limited to 255 characters because of DNS limitations (section 2.3.3).

However, many web servers limit the length of the data that can be passed as part of the URL, so the GET request may break in odd ways that are hard to debug. [Resources can be found here](https://boutell.com/newfaq/misc/urllength.html)

In many cases, such as in cryptography, astronomy and in scientific/engineering subjects that require very precise units of measurement. For example the recommended number digits in [RSA (cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) is 2048.

2. Even though according to these resources, which quotes the [HTML 2.0 spec](http://jkorpela.fi/forms/methods.html), the main difference between POST and GET:

> If the processing of a form is idempotent (i.e. it has no lasting observable effect on the state of the world), then the form method should be GET. Many database searches have no visible side-effects and make ideal applications of query forms.
> 
> If the service associated with the processing of a form has side effects (for example, modification of a database or subscription to a service), the method should be POST.

Although, according to this source, our request should be in GET, because we have seen that our request can be very big and very essential and we don't want our HTTP Request to be cut in the middle, **i would still prefer to use POST**.

### Sum of two `long numbers`

In order to add two long numbers, in the POST request we need to set two variables: `num1` and `num2`, for example:

```json
{  
  "num1": "51232131233",
  "num2": "482888391"
}
```

<br />

The output will be:

<p align="center">
  <img src="https://i.imgur.com/UghYvBf.png" width="700" />
</p>

**Few notes:**
- The number of digits after sum of two unsigned numbers `X` and `Y` is at most `MaxDigits{X, Y} + 1`
- In python arrays are represtend at list, hence, we don't need to take care about allocations.

### Multiplication of two `long numbers`

In order to add two long numbers, in the POST request we need to set two variables: `num1` and `num2`, for example:

```json
{  
  "num1": "99923139",
  "num2": "99229412419"
}
```
<br />

The output will be:

<p align="center">
  <img src="https://i.imgur.com/nVNd9Kf.png" width="700" />
</p>

**Few notes:**

- The number of digits after multiplication of two unsigned numbers `X` and `Y` is: 

<p align="center">
  <img src="https://i.imgur.com/Ks9cjni.png" width="500" />
</p>

- Once again, in python arrays are represtend at list, hence, we don't need to take care about allocations.

## Unit testings

This project also supports testing which come to check that everything is working correctly and testing different end cases and the overall functioning of the system.

Some end-cases that the system examines:

* Check multiplication / addition by 0.
* Check multiplication / addition by 1.
* Check multiplication / addition between very large numbers.
* Check multiplication / addition between numbers that will always cause to carry out.
* Check multiplication / addition between numbers that never carry.
* Check end case that either num1 or num2 or both are nulls.
* Check that in case the numbers are incorrect the system will return an Exception.


Let's take a look on a arbitrary example from the unit testing class:

```python
def test_sum_with_big_nums(self):
	num1 = "8124125132532423432431433426362143342174"
	num2 = "999999243279636214334217481"
	expected_result = [8, 1, 2, 4, 1, 2, 5, 1, 3, 2, 5, 3, 3, 4, 2, 3, 4, 3, 1, 6, 7, 4, 7, 1, 3, 0, 6, 2, 5, 7, 6, 4, 7, 7, 5, 5, 9, 6, 5, 5]
	self.assertEqual(sum_strings(num1, num2), expected_result)
```


### API & Documentation 

The table below shows the various commands that can be done in Web Service, as well as an explanation of the various parameters that must be included and the expected results that can be obtained.

| Action |                                               Parameters                                              |                                                                                                         Expected Output                                                                                                         | Example |
|:------:|:-----------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------:|
|  `sum` | `num1`: should be in number represented as string.<br /><br />`num2`: should be in number represented as string. |  **In case of no errors:**<br />the output will be JSON with two fields: `data`: the numbers before the calculation.<br />`result`: int array at the form of each digit is a cell in the array.<br /><br />**In case of error:**<br />`error`: the error message | The POST request:<br /> `{num1: 55, num2:30}`<br /><br />  The output:<br /> `{"data":["55","30"],"result":[8,3]}` |
|  `mul` | `num1`: should be in number represented as string.<br /><br />`num2`: should be in number represented as string. | **In case of no errors:**<br />the output will be JSON with two fields: `data`: the numbers before the calculation.<br />`result`: int array at the form of each digit is a cell in the array.<br /><br />**In case of error:**<br />`error`: the error message | The POST request:<br /> `{num1: 5, num2:3}`<br /><br />  The output:<br /> `{"data":["5","3"],"result":[1,5]}` |


## Docker Setup

**Requirements:**

-  Docker

**Setup:**

-  clone this repo
-  from within the repo, run `docker-compose build`
-  run the app with `docker-compose up`
-  app should be available at http://0.0.0.0:5000


## Requirements
To build this project you will need Docker and Docker Compose


## Challenges

-  Working with Flask framework
-  Choosing between POST or GET.
-  Learnning about unit testing
-  Learnning how to Dockerize python project


## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDE
* [Flask](https://www.fullstackpython.com/flask.html) - Web Framework
* [Docker](https://docs.docker.com/get-started/)
* [FlatIcon](https://www.flaticon.com/) - Icon on the top made by Freepik.
