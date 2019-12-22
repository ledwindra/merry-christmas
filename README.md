# About

Ho ho ho (:santa:)! Welcome to my repository! Here, we will create a simple program that produces a Christmas wish :christmas_tree:. I hope you enjoy this, ho ho ho!

# Clone

If you want to do this on your machine, clone this repository by running the following command on your terminal:

```
cd ~
git clone https://github.com/ledwindra/merry-christmas.git
cd ./merry-christmas
```

Simple, right? Ho ho ho :santa:!

# Run the Script

The script will produce texts which consist of a Christmas tree and the sentences. For the tree, it needs a function that produces a triangle. The first argument is needed to produce the height of the triangle. Note that the triangle is composed of a list of odd numbers, which then is translated to `#`. The second and third arguments could be any texts, which will produce the end of the program. Now, let's ask :santa: to run the :snake: program, shall we? :smile:

```
python3 src/merry_christmas.py 15 Best\ regards Santa
```

I find 15 is the most pleasant to look at for the triangle. However you could modify that with any number which resembles your preference. Note that there is `\` after `Best`, which is due to the whitespace within `Best regards`. Otherwise it will be considered as different arguments, and `Santa` will not be produced. Same thing if you want to replace `Santa` with more than one word which has whitespace. The script will produce the following text:
 

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
        Santa


```

What if we replace `Best regards` with `Sincerely`? Run the following command on your terminal and see the result as follows:

```
python3 src/merry_christmas.py 15 Sincerely Santa
```

Will produce:

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

        Sincerely,
        Santa


```

Simple, right? Thank you for reading. Ho ho ho!
