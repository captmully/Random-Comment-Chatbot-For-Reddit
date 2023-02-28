import praw

# create a Reddit instance (Requires PRAW API https://praw.readthedocs.io/en/latest/getting_started/installation.html )
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')

# get the subreddit you want to use
subreddit = reddit.subreddit('[enter subreddit here]')

#Grabs random comment from sepcified subreddit
def get_random_comment():
    random_submission = subreddit.random()
    random_comment = random_submission.comments.random()
    return random_comment.body

# run the chatbot loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    bot_response = get_random_comment()
    print("Bot:", bot_response)
