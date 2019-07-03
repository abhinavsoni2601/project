from flask import Flask, request, render_template, url_for
from validator import infu

app = Flask(__name__)

@app.route("/main")
def home():
    return render_template("index.html")

@app.route("/result",methods=["POST"])
def output():                                             
    form_data = request.form    
    A_name=form_data["A_name_here"]
    B_name=form_data["B_name_here"]
    A_follower_count = form_data["A_follower_count"]                                             
    A_following_count = form_data["A_following_count"]                       
    A_listed_count = form_data["A_listed_count"]
    A_mentions_received = form_data["A_mentions_received"]
    A_retweets_received = form_data["A_retweets_received"]
    A_mentions_sent = form_data["A_mentions_sent"]
    A_retweets_send = form_data["A_retweets_send"]
    A_posts = form_data["A_posts"]
    A_network_feature_1 = form_data["A_network_feature_1"]  
    A_network_feature_2 = form_data["A_network_feature_2"]
    A_network_feature_3 = form_data["A_network_feature_3"]
    B_follower_count = form_data["B_follower_count"]
    B_following_count = form_data["B_following_count"]
    B_listed_count = form_data["B_listed_count"]
    B_mentions_received = form_data["B_mentions_received"]
    B_retweets_received = form_data["B_retweets_received"]
    B_mentions_sent = form_data["B_mentions_sent"]
    B_retweets_send = form_data["B_retweets_send"]
    B_posts = form_data["B_posts"]  
    B_network_feature_1 = form_data["B_network_feature_1"]
    B_network_feature_2 = form_data["B_network_feature_2"]
    B_network_feature_3 = form_data["B_network_feature_3"]
    status={"A_follower_count":A_follower_count,"A_following_count":A_following_count,
            "A_listed_count":A_listed_count,"A_mentions_received":A_mentions_received,
            "A_retweets_received":A_retweets_received,"A_mentions_sent":A_mentions_sent,
            "A_retweets_send":A_retweets_send,
            "A_posts":A_posts,"A_network_feature_1":A_network_feature_1,
            "A_network_feature_2":A_network_feature_2,
            "A_network_feature_3":A_network_feature_3,
            "B_follower_count":B_follower_count,"B_following_count":B_following_count,
            "B_listed_count":B_listed_count,"B_mentions_received":B_mentions_received,
            "B_retweets_received":B_retweets_received,"B_mentions_sent":B_mentions_sent,
            "B_retweets_send":B_retweets_send,
            "B_posts":B_posts,"B_network_feature_1":B_network_feature_1,
            "B_network_feature_2":B_network_feature_2,
            "B_network_feature_3":B_network_feature_3}
    
    
    
    list1=list(map(float,status.values()))    
    
        
    
    """for x in list1:
        p=float(list1[x])
        list2.append(p)"""
    ou=infu(list1)
    if (ou[0]==0):
        st=B_name
    else:
        st=A_name
    #print(status)
    return render_template("response.html",status=st)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
