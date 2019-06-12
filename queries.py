import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="471-my-root",
    database= "mysocial"
)
mycursor = mydb.cursor()

get_users_post_by_tag = "SELECT P* FROM (((POST NATURAL JOIN PICTURE) NATURAL JOIN VIDEO) NATURAL JOIN AD) AS P, TAG AS T WHERE T.tagtext = %s AND P.Email_address = %s AND P.Link IN " 
reported_posts_with_tag = "SELECT R* FROM REPORT AS R, TAG AS T, POST AS P WHERE T.tagtext = %s AND T.link = P.link AND P.link = R.link"
users_total_reports = "SELECT Name, ID, COUNT(*) FROM (USER NATURAL JOIN REPORT) GROUP BY NAME, ID"
thread_subscribers = "SELECT COUNT(*) FROM SUBSCRIBES_TO AS ST WHERE ST.Name = %s"
midVotes = "SELECT POST* FROM POST, VOTE WHERE POST.Link = VOTE.Link GROUP BY VOTE.link HAVING COUNT(*) > 100 AND COUNT(*) < 300"

user_and_tag = ("email@email.com", "tag",)
mycursor.execute(get_users_post_by_tag, user_and_tag) #fails too long, doesn't read query after certain length

#tag_text = ("sfw",)
# mycursor.execute(reported_posts_with_tag, tag_text)#fails too long, doesn't read query after certain length

#mycursor.execute(users_total_reports) #runs

#thread_name = ("threadName",)
 #mycursor.execute(thread_subscribers, thread_name) #runs

#mycursor.execute(midVotes) #fails too long, doesn't read querry after certain length


myresult = mycursor.fetchall()

for result in myresult:
    print(result)
