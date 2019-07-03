#import numpy as np
#
#def credit_card(card_no):
#    reg = r'[456]+(\d{15}|\d{3}-(\d{4}-?){3})'
#    chk = re.match(reg,card_no)
#    rep = re.search(r'(\d)\1{3,}',card_no.replace('-',''))
#    if chk and not rep:
#        return "Valid"
#    else:
#        return "Invalid"


 
import numpy as np
import pickle

def infu(ls):
    with open("scale.pkl",'rb') as file:
        x1=pickle.load(file)
    with open("gbm.pkl",'rb') as file:
        x2=pickle.load(file)
    ls=np.array(ls)
    ls=ls.reshape(1,-1)
    ls2=x1.transform(ls)
    pred=x2.predict(ls2)
    return (pred)
   

