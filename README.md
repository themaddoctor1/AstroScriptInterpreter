# AstroScript
AstroScript is a very simple, interpreter-based language that I created as a personal challenge.
The idea for it came up when I was working on [3D Space Explorer](https://github.com/themaddoctor1/3D-Space-Explorer).
For the project, I created a simple interpreter-based language, after which I figured it would be interesting to try doing the same thing in Python.
As a result, I made it my mission to rewrite the language in Python.
The resulting language, which I named AstroScript in honor of the predecessor, has very little content, which makes it a very simple and easy language to learn.
However, this in turn makes it an extremely weak language, which is not capable of doing much of anything.

##Features
The list of features that AstroScript has is very small. However, the list is as follows:
* Numeric calculations
* For loops
* Text output
* Variables

##Syntax
####Indentation
All code must be indented properly, and follows essentially the same rules as in Python, where all code contained in a loop must be indented by exactly four more spaces than the loop declaration.
By default, all code must have no indentation, and rest up against the left edge of the line. See the code example provided if you wish to see how spacing works.

####Variables
Variables are written as:

```$[VARIABLE NAME]$```

They can be assigned a value by writing:

```$var$ = [YOUR VALUE HERE]```

The spacing should be written exactly as shown, or the program will not be able to interpret it. There should be one space between the equals sign and any value(s) that you place into the variable.

####Values
Currently, there is support for numeric and String values. Numeric values currently have to be assigned EXACTLY as follows:

```$var$ = #{[NUMERIC FUNCTION]}```

Numeric functions can include all PEMDAS operations (Parentheses, ^, *, /, +, -), as well as variables.
Spacing is not important, but mathematical correctness is.
Strings can be inputted by putting the desired input in quotations. For example:

```$message$ = "Hello world"```

is a properly formatted String that will output ```Hello world```. If any other data types are inserted into a variable at the same time, they will be converted into a String and concatenated onto the string. So, by doing this:

```
$var$ = "The answer to life, the Universe and Everything is " #{7 * 6}
print $var$
```

Should output ```The answer to life, the Universe and Everything is 42```.

####Output
Output is done very simply by doing this:

```print [VALUE]```

The value outputted can be any variable or value that can be inputted into a variable.
Basically, if you can assign it to a variable, you can output it, meaning that

```
$var$ = "Hello world"
print $var$
```

is the same as

```print "Hello world"```

####For loops
A for loop is written as so:

```
for [NUMER OF CYLES]
    [PROPERLY INDENTED CODE]
endfor
```

The parameter for the for statement does not need to be formatted, but it must be a base 10 number. For example:

```
for 10
    print "Hi"
endfor
```

This will output Hi ten times, and then finish.
