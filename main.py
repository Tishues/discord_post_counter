from functions import (
    get_path_text,
    count_users_post,
    get_op,
    count_comment_karma,
    
    )

post_path = "posts/post.txt"
text = get_path_text(post_path)


def main():
    count_users_post(text)
    get_op(text)
    count_comment_karma(text)





main()