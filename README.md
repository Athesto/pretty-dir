# Pretty-dir
![LICENSE-BADGE]
 > __Pretty-dir__ or __pdir__ is a pretty print function for the dir() command.

 - It checks the size of the screen to shows a better output of dir.
As the command `ls` in Linux.
 - It uses colors to diference `public` `privated` `protected`
and `dunder/magic` elements

## How to install

```console
pip install pdir-athesto
```

## How to use
Import the command and use the syntax
```
        pdir(<data>)
        pdir(<data>, <str>)
```
where `<str>` must be `"public"` or `"protected"` or
`"private"` or `"magic"` or `"dunder"`

### Example
```python
>>> from pdir import pdir
>>> pdir(list)
__add__           __gt__             __new__           clear
__class__         __hash__           __reduce__        copy
__contains__      __iadd__           __reduce_ex__     count
__delattr__       __imul__           __repr__          extend
__delitem__       __init__           __reversed__      index
__dir__           __init_subclass__  __rmul__          insert
__doc__           __iter__           __setattr__       pop
__eq__            __le__             __setitem__       remove
__format__        __len__            __sizeof__        reverse
__ge__            __lt__             __str__           sort
__getattribute__  __mul__            __subclasshook__
__getitem__       __ne__             append
>>>
>>> pdir(list, "public")
append  copy   extend  insert  remove   sort
clear   count  index   pop     reverse
```

## Use the manual

```python
>>> help(pdir)
```
## Extra: Automatic import

As a common function you should be able to use it in any moment
without the need to import the package everytime.

So my recommendation is to use the `PYTHONSTARTUP` variable.<br>
Copy this line into your `.bashrc`

```bash
export PYTHONSTARTUP=$HOME/.pythonrc
```

and create the `.pythonrc` with your favorite editor _(*Cof, *Cof, Vim)_ and
paste this line

```python
#!/usr/bin/env python3
try:
    from pdir import pdir
except:
    pass
```
## Suggestions
- If you found something that should be there
- Or you think that the redaction needs to be more specific
- Or you think that you need something more (a feature)
- Or there is something else

Please open an [issue][issues] and tell me your idea.

## Licence
[GPLv3](LICENSE)

## Author
Hi, I'm Gustavo Mejía and if it's works to you.
Please let me know in twitter in [@im_tavo].

<!--Links-->
[@im_tavo]: twitter.com/im_tavo
[issues]: https://github.com/Athesto/pretty-pdir/issues
[LICENSE-BADGE]: https://img.shields.io/github/license/athesto/pretty-pdir?color=red
