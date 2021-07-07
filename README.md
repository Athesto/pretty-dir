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
where `<data>` is any object and `<str>` must be `"public"` or `"protected"` or
`"private"` or `"magic"` or `"dunder"`

### Example
![pdir vs dir][image_pdir]

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
[wikipedia]: https://wikipedia.org
[image_pdir]: https://github.com/Athesto/pretty-dir/raw/main/assets/pdir_vs_dir_2.png
