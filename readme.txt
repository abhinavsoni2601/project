This is the source code of the Twitter Influencer Predictor developed using the Machine learning Model with the database from "PeerIndex"
Contents of the folder :
gbm.pkl : It is the pickle file of the machine learning model "Xg Boost"
scale.pkl: It is the pickle file of the standard scaler used in the preprocessing of the data 
server.py : It is the main file used for making the GUI using the Flask with connections to html files 
validator.py : It contains the python code for using the Machine Learning Model and gives the Output for the Influencer.
Templates/index.html: It contains the html code for the home page and also the asks the information that is then passed to the validator.py 
Templates/layout.html: It contains the layout of the web pages 
Templates/response.html: It contains the information that is generated from the validator.py and is presented on this page as the final output
static/images: It contains the images used in making the webpages
