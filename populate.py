import mysql.connector

#TO CHANGE ENCRYPTION OF PASSWORD
# ALTER USER 'yourusername'@'localhost' IDENTIFIED WITH mysql_native_password BY 'youpassword';

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="471-my-root",
    database= "mysocial"
)

mycursor = mydb.cursor()

insert_to_user = "INSERT INTO USER (Name, ID, IP_Address) VALUES ( %s, %s, %s )"

insert_to_logged = "INSERT INTO LOGGED_IN (Email_address, Password, Name, ID, IP_Address) VALUES (%s, %s, %s, %s, %s)"


insert_to_admin = "INSERT INTO ADMIN (Email_address, Password, Name, ID, IP_Address, Employee_ID) VALUES (%s, %s, %s, %s, %s, %s)"

insert_to_advertiser = "INSERT INTO ADVERTISER (Email_address, Password, Name, ID, IP_Address, Company_name) VALUES (%s, %s, %s, %s, %s, %s)"

inser_to_post = "INSERT INTO POST (Link, Caption, Email_address) VALUES (%s, %s, %s)"

insert_to_picture = "INSERT INTO PICTURE (Link, Caption, Resolution, Name, ID) VALUES (%s, %s, %s, %s, %s)"

insert_to_video = "INSERT INTO VIDEO (Link, Caption, Resolution, Length, Name, ID) VALUES (%s, %s, %s, %s, %s, %s)"

insert_to_ad = "INSERT INTO AD (Link, Caption, Num_views, Num_clicks, Email_address) VALUES (%s, %s, %s, %s, %s)"

insert_to_thread = "INSERT INTO THREAD (Name, Email_address) VALUES (%s, %s)"

insert_to_comment = "INSERT INTO COMMENT (CText, Name, ID, Link) VALUE(%s, %s, %s, %s)"

insert_to_contains = "INSERT INTO CONTAINS (Name, Link) VALUES (%s, %s)"

insert_to_subscribes = "INSERT INTO SUBSCRIBES_TO (Name, Email_address) VALUES (%s, %s)"

insert_to_moderates = "INSERT INTO MODERATES (Name, Email_address, Email_address2) VALUES (%s, %s)"

insert_to_follow = "INSERT INTO FOLLOW (Email_address, Email_address2) VALUES (%s, %s)"

insert_to_repost = "INSERT INTO REPOST (Link, Name, ID) VALUES (%s, %s, %s)"

insert_to_vote = "INSERT INTO VOTE (Link, Name, ID) VALUES (%s, %s, %s)"

insert_to_report = "INSERT INTO REPORT (Link, Name, ID) VALUES (%s, %s, %s)"

insert_to_tag = "INSERT INTO TAG (Link, Tagtext) VALUES (%s, %s)"

user1 = ("Aidan", 0, 314)
user2 = ("Carl", 1, 111)
user3 = ("Steven", 2, 510)
user4 = ("Carl", 3, 222)
user5 =  ("TheLegend27", 4, 333)

loggedin1 = ("someOne@gmail.com", "noTwo", "Aidan", 3, 1)
loggedin2 = ("fireman64@gmail.com", "noFires", "fire64", 1, 1)
loggedin3 = ("bubbleBlower@hotmail.com", "bubbles", "Bubble", 0, 1)
loggedin4 = ("someTwo@gmail.com", "password", "Laughable Linguist", 2, 1)

advertiser1 = ("bigCompany@company.com", "M0ney", "Buy Stuff", 0, 0, "Big Company")
advertiser2 = ("smallCorp@company.com", "adPassword", "small corp", 0, 0, "Big Company")

admin1 =("important@outlook.com", "Hard2GuessPassword", "Admin", 0, 131, 1)

post1 = ("page.text1", "Look at these words.", "someOne@gmail.com")
post2 = ("page.text2", "Who need images when you have text", "someTwo@gmail.com")
post3 = ("page.text3", "Bubbles.", "bubbleBlower@hotmail.com")
post4 = ("page.text4", "This is my second post", "someOne@gmail.com")
post5 = ("page.text5", "Don't do anything I wouldn't", "important@outlook.com")

picture1 = ("image.com/image555", "Look at this bubble", "2080x1440", "Bubble", 0) 
picture2 = ("image.com/image658", "These fires are out of control", "1000x1000", "fire64", 1) 
picture3 = ("image.com/image789", "This was a great victory", "1080x720", "TheLegend27", 4) 
picture4 = ("image.com/image111", "Haha look at this cat", "1200x1420", "Carl", 3) 

video1 = ("youtube.com/watch/asfdsaf", "Spoilers for Avengers Endgame", "1920x1080", "13:45", "Carl", 1)
video2 = ("youtube.com/watch/ds45ad46", "", "1280x720", "5", "Laughable Linguist", 2)
video3 = ("youtube.com/watch/7fhg7g6", "So many BUBBLES", "1920x1080", "10:00:02", "Bubble", 0)
video4 = ("youtube.com/watch/r41ew354r", "Buy gold!!", "280x144", "15:10", "fire64", 1)
video5 = ("youtube.com/watch/d4was564d", "More high quality bubbless", "3840x2160", "30:40", "Bubble", 0)

ad1= ("bigcompany.com", "Check out our sweet merch", 0 , 0, "bigCompany@company.com" )
ad2= ("bigcompany.ca", "Check out our Canadian merch", 10 , 1, "bigCompany@company.com" )
ad3= ("smallcorperation.com", "Support your local businesses", 10 , 1, "bigCompany@company.com" )

comment1 = ("Who cares about bubbles when there are fires?", "fire64", 1, "youtube.com/watch/7fhg7g6") 
comment2 = ("That really was a bad fire!", "Carl", 3, "image.com/image658") 
comment3 = ("Yeah. Carl 3, it was.", "fire64", 1, "image.com/image658") 
comment4 = ("Wow, what cool products", "Steven", 2, "smallcorperation.com") 
comment5 = ("Wow text posts needing links is kinda weird.", "Aidan", 3, "page.text5") 

thread1 = ("Bubble Blowers", "bubbleBlower@hotmail.com")
thread2 = ("Fire Stoppers", "fireman64@gmail.com")
thread3 = ("Not Bubbles", "bubbleBlower@hotmail.com")
thread4 = ("Text Thread", "someTwo@gmail.com")
thread5 = ("Empty Thread", "someTwo@gmail.com")

threadpost1 = ("Bubble Blowers", "image.com/image555")
threadpost2 = ("Bubble Blowers", "youtube.com/watch/7fhg7g6")
threadpost3 = ("Bubble Blowers", "youtube.com/watch/d4was564d")
threadpost4 = ("Text Thread", "page.text1")
threadpost5 = ("Text Thread", "page.text2")
threadpost6 = ("Text Thread", "page.text3")
threadpost7 = ("Text Thread", "page.text4")
threadpost8 = ("Text Thread", "page.text5")
threadpost9 = ("Not Bubbles", "youtube.com/watch/asfdsaf")
threadpost10 = ("Not Bubbles", "page.text1")
threadpost11 = ("Not Bubbles", "bigcompany.com")
threadpost12 = ("Not Bubbles", "image.com/image111")
threadpost13 = ("Fire Stoppers", "youtube.com/watch/r41ew354r")
threadpost14 = ("Fire Stoppers", "image.com/image658")

subscribe1 = ("Fire Stoppers", "fireman64@gmail.com")
subscribe2 = ("Fire Stoppers", "someOne@gmail.com")
subscribe3 = ("Fire Stoppers", "someTwo@gmail.com")
subscribe4 = ("Not Bubbles", "fireman64@gmail.com")
subscribe5 = ("Text Thread", "someTwo@gmail.com")
subscribe6 = ("Text Thread", "bubbleBlower@hotmail.com")

moderates1 = ("Bubble Blowers", "bubbleBlower@hotmail.com", "important@outlook.com")
moderates2 = ("Fire Stoppers", "fireman64@gmail.com", "important@outlook.com")
moderates3 = ("Text Thread", "someTwo@gmail.com", "important@outlook.com")
moderates4 = ("Not Bubbles", "bubbleBlower@hotmail.", "important@outlook.com")
moderates5 = ("Empty Thread", "someTwo@gmail.com", "important@outlook.com")

follow1 =("someOne@gmail.com", "fireman64@gmail.com")
follow2 =("someOne@gmail.com", "bubbleBlower@hotmail.com")
follow3 =("someOne@gmail.com", "someTwo@gmail.com")
follow4 =("someTwo@gmail.com", "bubbleBlower@hotmail.com")
follow5 =("bubbleBlower@hotmail.com", "someTwo@gmail.com")
follow6 =("bubbleBlower@hotmail.com", "someOne@gmail.com")

repost1 = ("image.com/image789", "Bubble", 3) 

vote1 =  ("youtube.com/watch/d4was564d", "Bubble", 0) 
vote2 =  ("youtube.com/watch/d4was564d", "Aidan", 3) 
vote3 =  ("image.com/image658", "Carl", 3) 

report1 = ("youtube.com/watch/r41ew354r", "TheLegend27", 4) 

tag1 =  ("youtube.com/watch/asfdsaf", "Spoilers") 

inThread= ("")
mycursor.execute(insert_to_user, user1)
mycursor.execute(insert_to_user, user2)
mycursor.execute(insert_to_user, user3)
mycursor.execute(insert_to_user, user4)

mycursor.execute(insert_to_logged, loggedin1)
mycursor.execute(insert_to_logged, loggedin2)
mycursor.execute(insert_to_logged, loggedin3)
mycursor.execute(insert_to_logged, loggedin4)

mycursor.execute(insert_to_admin, admin1)

mycursor.execute(inser_to_post, post1)
mycursor.execute(inser_to_post, post2)
mycursor.execute(inser_to_post, post3)
mycursor.execute(inser_to_post, post4)
mycursor.execute(inser_to_post, post5)

mycursor.execute(insert_to_picture, picture1)
mycursor.execute(insert_to_picture, picture2)
mycursor.execute(insert_to_picture, picture3)
mycursor.execute(insert_to_picture, picture4)

mycursor.execute(insert_to_video, video1)
mycursor.execute(insert_to_video, video2)
mycursor.execute(insert_to_video, video3)
mycursor.execute(insert_to_video, video4)
mycursor.execute(insert_to_video, video5)

mycursor.execute(insert_to_ad, ad1)
mycursor.execute(insert_to_ad, ad2)
mycursor.execute(insert_to_ad, ad3)

mycursor.execute(insert_to_comment, comment1)
mycursor.execute(insert_to_comment, comment2)
mycursor.execute(insert_to_comment, comment3)
mycursor.execute(insert_to_comment, comment4)
mycursor.execute(insert_to_comment, comment5)

mycursor.execute(insert_to_thread, thread1)
mycursor.execute(insert_to_thread, thread2)
mycursor.execute(insert_to_thread, thread3)
mycursor.execute(insert_to_thread, thread4)
mycursor.execute(insert_to_thread, thread5)

mycursor.execute(insert_to_contains, threadpost1)
mycursor.execute(insert_to_contains, threadpost2)
mycursor.execute(insert_to_contains, threadpost3)
mycursor.execute(insert_to_contains, threadpost4)
mycursor.execute(insert_to_contains, threadpost5)
mycursor.execute(insert_to_contains, threadpost6)
mycursor.execute(insert_to_contains, threadpost7)
mycursor.execute(insert_to_contains, threadpost8)
mycursor.execute(insert_to_contains, threadpost9)
mycursor.execute(insert_to_contains, threadpost10)
mycursor.execute(insert_to_contains, threadpost11)
mycursor.execute(insert_to_contains, threadpost12)
mycursor.execute(insert_to_contains, threadpost13)
mycursor.execute(insert_to_contains, threadpost14)

mycursor.execute(insert_to_subscribes, subscribe1)
mycursor.execute(insert_to_subscribes, subscribe2)
mycursor.execute(insert_to_subscribes, subscribe3)
mycursor.execute(insert_to_subscribes, subscribe4)
mycursor.execute(insert_to_subscribes, subscribe5)
mycursor.execute(insert_to_subscribes, subscribe6)

mycursor.execute(insert_to_moderates, moderates1)
mycursor.execute(insert_to_moderates, moderates2)
mycursor.execute(insert_to_moderates, moderates3)
mycursor.execute(insert_to_moderates, moderates4)
mycursor.execute(insert_to_moderates, moderates5)

mycursor.execute(insert_to_follow, follow1)
mycursor.execute(insert_to_follow, follow2)
mycursor.execute(insert_to_follow, follow3)
mycursor.execute(insert_to_follow, follow4)
mycursor.execute(insert_to_follow, follow5)
mycursor.execute(insert_to_follow, follow6)

mycursor.execute(insert_to_repost, repost1)

mycursor.execute(insert_to_vote, vote1)
mycursor.execute(insert_to_vote, vote2)
mycursor.execute(insert_to_vote, vote3)


mycursor.execute(insert_to_report, report1)

mycursor.execute(insert_to_tag, tag1)


mydb.commit()