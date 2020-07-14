#!/usr/bin/env python3
"""
1.extract all json comment
2.clean
3. keep ones length>=10
"""

import bz2
import json
import html
import os
import re
import string
import random

from url import remove_urls

def generate_txt(year, directory="."):
    """
    generate text file for one year.
    """
    txt_lst = []
    t_name = 'comment_'+str(year)+'.txt'
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    regex = re.compile(r'[^\w\s]')

    N = 2500000*3
    N = 1

    suffix = ".bz2"

    for i in range(1,13):

        sample = []

        if i<10:
            file_path = os.path.join(directory, 'RC_'+str(year)+'-0'+str(i)+suffix)
        else:
            file_path = os.path.join(directory, 'RC_'+str(year)+'-'+str(i)+suffix)

        print(file_path+" start")

        with bz2.open(file_path) as f, open(t_name,mode='a',encoding='utf-8') as t:
            for idx,line in enumerate(f):
                comment_line = json.loads(line)
                comment = comment_line["body"]
                if comment != '[deleted]' and comment != '[removed]':

                    comment = comment.replace("&gt;","")
                    comment = comment.replace("&amp;","")
                    comment = comment.replace("&lt;","")
                    comment = comment.replace("&quot;","")
                    comment = comment.replace("&apos;","")
            
                    comment = comment.lower()
                    comment = remove_urls(comment)
                    comment = regex.sub('',comment)

                    spl = comment.split()
                    if (len(spl) >=10):
                        comment = ' '.join(spl)
                        t.write(comment+' \n')




if __name__ == '__main__':
    generate_txt(2012, "comments")


