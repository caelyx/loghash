Log Hash
========

Basic tamper evidence for logs, written in python. 

Uses a chained SHA1 hash to spot if a line in a file has been altered. 

Notes on use
------------

* Replace the SALT in both `loghash.py` and `verify.py` with a random value of your choosing. This doesn't mildly reduces the likelihood that a rainbow table could be used against your instance.
* At present, this works only on files named input.txt and emits output.txt.  Adaptation to arbitrary files and/or streams should be easy, but hasn't been done.

Sample output
-------------

Given this input file and the default SALT: 

```
This is a logfile that we would like to secure.
We want to detect whether
anything
is changed later, after the log has been created.
But specifically, which lines.
```

`loghash.py` will emit:

```
844cde87865f882399dcffcecb002e5397f9d177 This is a logfile that we would like to secure. 
64aa566e3d94bca509cb22cfea8eaca15836e77c We want to detect whether 
bd97b82302e7125f717a22ad64c681a4017b0337 something 
81b075cb6bf2e45851c60f68d0e6a9adc47a7038 is changed later, after the log has been created. 
9d8e91ce9685f01402b8892c7e4bd6c3a3ba6b5f But specifically, which lines. 
6f3fe424feae01dbdfb17c4c0d1784e3a743dcb3 -
```

and `verify.py` will report: 

```
+ This is a logfile that we would like to secure. 
+ We want to detect whether 
+ something 
+ is changed later, after the log has been created. 
+ But specifically, which lines. 
```

The `+` at the start of each line indicates that it verified successfully. 

If, though, output.txt is tampered, e.g. to replace 'something' with 'anything'
in line three, `verify.py` will report:

```
+ This is a logfile that we would like to secure. 
+ We want to detect whether 
!!! anything 
+ is changed later, after the log has been created. 
+ But specifically, which lines. 
```

And the `!!!` at the start of that line indicates that it was tampered.
