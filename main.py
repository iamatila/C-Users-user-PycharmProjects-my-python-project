from user import *
from post import Post

app_user1 = User("tt@tt.com", "Tobi Atilola", "pwd1", "Devops Engineer")
app_user1.get_user_info()

app_user2 = User("jj@jj.com", "James Bond", "supersecret", "Agent")
app_user2.get_user_info()

app_user1.change_job_title("Platform Engineer")
app_user1.get_user_info()

new_post = Post("On a secret mission today", app_user1.name)
new_post.get_post_info()