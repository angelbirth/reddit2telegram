#encoding:utf-8

subreddit = 'freegamefindings'
t_channel = '@r_freegamefindings'


def send_post(submission, r2t):
    return r2t.send_simple(submission)
