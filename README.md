# About

This repository aims to wish you a merry christmas and happy holidays.

# Clone

If you want to do this on your machine, clone this repository by running the following command on your terminal:

```
cd ~
git clone https://github.com/ledwindra/merry-christmas.git
cd ./merry-christmas
```

# Run the Script

The script will produce texts which consist of a Christmas tree and the sentences. For the tree, it needs a function that produces a triangle. The first argument is needed to produce the height of the triangle. Note that the triangle is composed of a list of odd numbers, which then is translated to `#`. The second argument is a text which should be any text. That could be your name, company, etc. For example, see the following command and run on your terminal:

```
python3 src/merry_christmas.py 15 Lukman
```

I find 15 is the most pleasant to look at for the triangle. However you could modify that with any number which resembles your preference. The script will produce the following text:
 

```


        Merry Christmas and Happy Holidays!

                       #
                      ###
                     #####
                    #######
                   #########
                  ###########
                 #############
                       #
                       #
                       #

        Best regards,
        Lukman


```
