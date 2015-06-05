# MacVim with Skim.app #

You can get the source at http://agpy.googlecode.com/svn/trunk/macvim-skim/,
or grab the install script (which will download the relevant files) from
http://agpy.googlecode.com/svn/trunk/macvim-skim/macvim-skim-install.sh.


# What does it do? #

This plugin makes macvim and skim work together.  command-shift-click on a line in Skim to bring up the MacVim window with the .tex file open to the clicked line.  Use one of the commands below, e.g. **`,p`** , to compile the tex document and open it to the selected line in Skim.  Example:

![http://agpy.googlecode.com/svn/trunk/macvim-skim/test/Example_MacvimSkim.png](http://agpy.googlecode.com/svn/trunk/macvim-skim/test/Example_MacvimSkim.png)


# Known bugs #

WhichTab.vim uses <a href='http://vimdoc.sourceforge.net/htmldoc/eval.html#bufname()'>
bufname</a>, which will fail silently if there are multiple files with the same
name open in different buffers (e.g., if you have multiple different ms.tex
files open).

If you're not sure what's going on, try using the "debug" feature to figure it out:
`macvim-load-line ms.tex 100 debug`
It will echo the individual commands sent to VIM to the command line so you can
figure out which one is going wrong.


My .vimrc includes the following (modify as you see fit):

```
" Activate skim
map ,v :w<CR>:silent !/Applications/Skim.app/Contents/SharedSupport/displayline -r <C-r>=line('.')<CR> %<.pdf %<CR><CR>
map ,p :w<CR>:silent !pdflatex -synctex=1 --interaction=nonstopmode %:p <CR>:silent !/Applications/Skim.app/Contents/SharedSupport/displayline -r <C-r>=line('.')<CR> %<.pdf %<CR><CR>
map ,m :w<CR>:silent !make <CR>:silent !/Applications/Skim.app/Contents/SharedSupport/displayline -r <C-r>=line('.')<CR> %<.pdf %<CR><CR>
" Reactivate VIM
map ,r :w<CR>:silent !/Applications/Skim.app/Contents/SharedSupport/displayline -r <C-r>=line('.')<CR> %<.pdf %<CR>:silent !osascript -e "tell application \"MacVim\" to activate" <CR><CR>
map ,t :w<CR>:silent !pdflatex -synctex=1 --interaction=nonstopmode %:p <CR>:silent !/Applications/Skim.app/Contents/SharedSupport/displayline -r <C-r>=line('.')<CR> %<.pdf %<CR>:silent !osascript -e "tell application \"MacVim\" to activate" <CR><CR>
```