#Stuck?

##What should you do when you are stuck?

###Don't be so stuck prone.
+ use functions for control and modularity
    > Breaking a large program into smaller functions creates natural checkpoints for debugging. If a function is not working, there are three possibilities to consider:
        <br>- There is something wrong with the arguments the function is getting; a precondition is violated.
        <br>- There is something wrong with the function; a postcondition is violated.
        <br>- There is something wrong with the return value or the way it is being used. ([TP:Ch6.9][Ch6.9])
<hr>
    > It may not be clear why it is worth the trouble to divide a program into functions. There are several reasons:
        <br>- Creating a new function gives you an opportunity to name a group of statements, which makes your program easier to read and debug.
        <br>- Functions can make a program smaller by eliminating repetitive code. Later, if you make a change, you only have to make it in one place.
        <br>- Dividing a long program into functions allows you to debug the parts one at a time and then assemble them into a working whole.
        <br>- Well-designed functions are often useful for many programs. Once you write and debug one, you can reuse it. ([TP:Ch3.12][Ch3.12])

+ remember: it is **not magic**
+ comment as you develop (you have a limited range of focus and working memory)
    + externalizing your memory and directing your focus through comments helps
+ take the directions and turn into pseudocode
+ incremental development
    + test and print along the way

        > The goal of incremental development is to avoid long debugging sessions by adding and testing only a small amount of code at a time. ([TP:Ch6.2][Ch6.2])
+ before introducing code found on StackOverflow, test in a new environment to **confirm you know what it does**
+ these words are special - Python keywords:
    + `and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield`
+ do not use these as names for variables (or you overwrite the built-in function) ([Built-in Functions][BinF]):
    + `abs(), divmod(), input(), open(), staticmethod(), all(), enumerate(), int(), ord(), str(), any(), eval(), isinstance(), pow(), sum(), basestring(), execfile(), issubclass(), print(), super(), bin(), file(), iter(), property(), tuple(), bool(), filter(), len(), range(), type(), bytearray(), float(), list(), raw_input(), unichr(), callable(), format(), locals(), reduce(), unicode(), chr(), frozenset(), long(), reload(), vars(), classmethod(), getattr(), map(), repr(), xrange(), cmp(), globals(), max(), reversed(), zip(), compile(), hasattr(), memoryview(), round(), __import__(), complex(), hash(), min(), set(), delattr(), help(), next(), setattr(), dict(), hex(), object(), slice(), dir(), id(), oct(), sorted()`

###Debugging ([TP:Appendix A][AppA])
> Make sure that the code you are looking at is the code you are running. If you’re not sure, put something like print 'hello' at the beginning of the program and run it again. If you don’t see hello, you’re not running the right program! ([TP:Ch3.14][Ch3.14])

+ bisection ([TP:Ch7.7][Ch7.7])
    + split the code in half and verify everything is working correctly at that m
+ print statements
    + print the values of variables

        > For debugging this kind of error, my first move is to print the values of the indices immediately before the line where the error appears. ([TP:Ch8.11][Ch8.11])

    + print the types of variables
    + print the repr() of variables
+ review patterns in code from previous assignments
+ read the stack trace, line numbers, and exception type and message

    > In general, error messages tell you where the problem was discovered, but that is often not where it was caused. ([TP:Ch5][Ch5])

+ write out code, variables, test cases
+ draw the flow of execution
+ comment out blocks of code (to isolate problem)
+ lists
    
    > Don’t forget that most list methods modify the argument and return None.([TP:Ch10.13][Ch10.13])
+ dictionaries ([TP:Ch11.8][Ch11.8])



+ so, yes, walk through your code line by line
    #BUT: 
    + **you** are not a Python interpreter/parser/compiler
    + don't think the code isn't doing what you are telling it to do
        + it is doing EXACTLY what you are telling it to do
    + so break it down, piece-by-piece
        + isolate the problem area
        + **test it** in a fresh script
        + or test it in the interpreter
    + it is **not magic**



###Resources
+ [StackOverflow][SO]
    + Google: `python site:http://stackoverflow.com [terms]`
+ Python documentation
    + the docs
        + [The Python Language Reference][reference]
        + [The Python Standard Library][library]
    + [The Python Tutorial][pythontutorial]
+ Google the error message (include "python"); Example:
    + Google: `python [error type] [error message]`
+ Think Python
    + Google: `site:http://www.greenteapress.com/thinkpython/html/ [terms]`

###Other
+ discuss w/ imaginary friend
+ nap, walk around, go on a run, eat a donut
+ `import this`

[Ch3.14]: http://www.greenteapress.com/thinkpython/html/thinkpython004.html#toc37
[Ch3.12]: http://www.greenteapress.com/thinkpython/html/thinkpython004.html#toc35
[Ch5]: http://www.greenteapress.com/thinkpython/html/thinkpython006.html#toc63
[Ch6.9]: http://www.greenteapress.com/thinkpython/html/thinkpython007.html#toc74
[Ch6.2]: http://www.greenteapress.com/thinkpython/html/thinkpython007.html#toc67
[Ch7.7]: http://www.greenteapress.com/thinkpython/html/thinkpython008.html#toc83
[Ch8.11]: http://www.greenteapress.com/thinkpython/html/thinkpython009.html#toc96
[Ch10.13]: http://www.greenteapress.com/thinkpython/html/thinkpython011.html#toc118
[Ch11.8]: http://www.greenteapress.com/thinkpython/html/thinkpython012.html#toc128
[AppA]: http://www.greenteapress.com/thinkpython/html/thinkpython021.html
[reference]: https://docs.python.org/2.7/reference/index.html
[library]: https://docs.python.org/2.7/library/index.html#library-index
[BinF]: https://docs.python.org/2/library/functions.html#built-in-functions
[pythontutorial]: https://docs.python.org/2/tutorial/
[SO]: http://stackoverflow.com/questions/tagged/python