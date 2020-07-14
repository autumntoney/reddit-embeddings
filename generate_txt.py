"""
1.extract all json comment
2.clean
3. keep ones length>=10, without website link
"""

import json
import html
import re
import string
import random

def generate_txt(year):
    """
    generate text file for one year.
    """
    txt_lst = []
    t_name = 'comment_'+str(year)+'.txt'
    translator = str.maketrans(string.punctuation, ''*len(string.punctuation))

    N = 2500000*3
    N = 1

    for i in range(1,13):

        sample = []

        if i<10:
            file_path = 'RC_'+str(year)+'-0'+str(i)
        else:
            file_path = 'RC_'+str(year)+'-'+str(i)

        print(file_path+" start")

        with open(file=file_path,encoding='utf-8') as f, open(file=t_name,mode='a',encoding='utf-8') as t:
            for idx,line in enumerate(f):

                # if idx < N:

                comment_line = json.loads(line)
                comment = comment_line["body"]
                # comment = comment.encode('ascii','ignore').decode('ascii')
                if comment != '[deleted]' and comment != '[removed]':

                    comment = comment.replace("&gt;","")
                    comment = comment.replace("&amp;","")
                    comment = comment.replace("&lt;","")
                    comment = comment.replace("&quot;","")
                    comment = comment.replace("&apos;","")
                    # comment = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', comment)
                    # comment = ' '.join(comment.splitlines())
                    comment = comment.lower()
                    comment = comment.translate(translator)

                    spl = comment.split()
                    if (len(spl) >=10) and ('http' not in spl) and ('www' not in spl):
                        comment = ' '.join(spl)
                        t.write(comment+' \n')



def check_double(year,month):
    """
    check with duplicated comments exist
    """
    file_path = 'RC_'+str(year)+'-'+month
    comment_lst = ['09asx']
    with open(file=file_path,encoding='utf-8') as f:
        for line in f:
            comment_line = json.loads(line)
            comment = comment_line['id']
            if comment != '[deleted]' and comment != '[removed]':
                # comment = comment[-min(len(comment),50):]

                if comment in comment_lst:
                    print(comment)
                    # break

                comment_lst.append(comment)




if __name__ == '__main__':
    generate_txt(2006)
    # generate_txt(2013)
    # generate_txt(2014)

    # generate_txt(2007)
    # check_double(year=2006,month='05')
