from functions import get_path_text, get_unique_usernames, count_users_post, get_commenters, get_op, count_comment_karma


post_path = "posts/post.txt"
text = get_path_text(post_path)

def main():
    get_unique_usernames(text)
    count_users_post(text)
    get_op(text)
    get_commenters(text)
    count_comment_karma(text)
    #print(text)








main()