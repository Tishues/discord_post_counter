import re

# use the given path to open the text file
def get_path_text(path):
    with open(path, 'r') as file:
        return file.read()
    
    
# get all usernames for all other functions to use
def get_usernames(text):
    find_op = re.findall(r'OP\n \w+', text)
    find_usernames_pm = re.findall(r'PM]\w+', text)
    find_usernames_am = re.findall(r'AM]\w+', text)
    find_usernames = find_usernames_pm + find_usernames_am + find_op
    user_list = []
    for user in find_usernames:
        if user.startswith('PM]') or user.startswith('AM]') or user.lstrip('OP\n '):
            user = user.lstrip('PM]')
            user = user.lstrip('AM]')
            user = user.lstrip('OP\n ')
            user_list.append(user)
    return user_list


# find who commented on the post
def get_commenters(text):
    find_usernames_pm = re.findall(r'PM]\w+', text)
    find_usernames_am = re.findall(r'AM]\w+', text)
    usernames = find_usernames_pm + find_usernames_am
    commenters = []
    for user in usernames:
        if user.startswith('PM]') or user.startswith('AM]'):
            user = user.lstrip('PM]')
            user = user.lstrip('AM]')
            commenters.append(user)
    return commenters
    

# find the original poster
def get_op(text):
    op = set()
    find_op = re.findall(r'OP\n \w+', text)
    for user in find_op:
        if user.startswith('OP'):
            user = user.lstrip('OP\n ')
            op.add(user)
    print(f"OP: {op}")


# gets unique usernames
def get_unique_usernames(text):
    names = get_usernames(text)
    names = set(names)
    print(f"Users: {names}")   
    

# count total posts & posts for each user
def count_users_post(text):
    total_count = 0
    names = {}
    usernames = get_usernames(text)
    for name in usernames:
        total_count += 1
        if name in names:
            names[name] += 1
        else:
            names[name] = 1
    print(f"User Posts: {names}")
    print(f"Total Posts: {total_count}")


# count expected karma points from Boot.dev's Discord help threads
def count_comment_karma(text):
    total_count = 0
    names = {}
    usernames = get_commenters(text)
    for name in usernames:
        total_count += 1
        if name in names:
            names[name] += 1
        else:
            names[name] = 1
    print("Karma Expected:")
    for key in names:
        print(f"{key} = {(names[key] / total_count) * 200}")
        