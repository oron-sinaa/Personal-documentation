Any kind of document
====================

### Rename workspaces

`gsettings set org.gnome.desktop.wm.preferences workspace-names "['Browser', 'Terminal', 'Word', 'Games','Settings']"`


### Restore workspace names

`gsettings reset org.gnome.desktop.wm.preferences workspace-names`


### Markdown and good practices

> [Markdown basic syntax](https://www.markdownguide.org/basic-syntax/)


### Task Manager in Linux

`top`
*or*
`sudo apt-get install htop`
`htop`

> [Datetime to string formatting e.g. %d-%M-%Y](https://www.ibm.com/docs/en/app-connect/11.0.0?topic=function-formatting-parsing-datetimes-as-strings)


### ">" operator:

">" redirects output to a file (but it can be to a device).
">>" to append.

If number is not specified, the standard output stream is assumed, but you can also redirect errors:

"> file"  - redirects *stdout* to file

"1> file" - redirects *stdout* to file

"2> file" - redirects *stderr* to file

"&> file" - redirects *stdout* and stderr to file

"> file 2>&1" - redirects *stdout and stderr* to file

"/dev/null" is the null device it takes any input you want and throws it away. It can be used to suppress any output.

Note: "> file 2>&1" is an older syntax which still works, &> file is neater, but would not have worked on older systems.
