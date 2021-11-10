import os
from flask import Flask
from flask import render_template
import article_list

posts = article_list.posts

app = Flask(__name__)

@app.route('/cuisine')
def cuisine():
    theme = "永續美食"
    subtitle = "彈性素食者的飲食指南"
    friend_page1_link = '/voyage'
    friend_page1 = '永續旅遊'
    friend_page2_link = '/anecdote'
    friend_page2 = 'Coding Life Anecdote'
    self_link = '/cuisine'
    posts = article_list.posts
    band = 'yellow'
    return render_template('index.html' , theme = theme, subtitle = subtitle,friend_page1_link = friend_page1_link ,friend_page1 = friend_page1, friend_page2_link = friend_page2_link, friend_page2 = friend_page2, self_link = self_link, posts = posts,band = band)

@app.route('/voyage')
def voyage():
    theme = "永續旅遊"
    subtitle = "極簡旅遊，但樂趣不減"
    friend_page1_link = '/cuisine'
    friend_page1 = '永續美食'
    friend_page2_link = '/anecdote'
    friend_page2 = 'Coding Life Anecdote'
    self_link = '/voyage'
    band = 'sliver'
    return render_template('index.html' , theme = theme, subtitle = subtitle,friend_page1_link = friend_page1_link ,friend_page1 = friend_page1, friend_page2_link = friend_page2_link, friend_page2 = friend_page2, self_link = self_link, posts = posts, band = band)

@app.route('/anecdote')
def anecdote():
    theme = "Coding Life Anecdote"
    subtitle = "Some casual stories to the way of joyful programmer"
    friend_page1_link = '/voyage'
    friend_page1 = '永續旅遊'
    friend_page2_link = '/anecdote'
    friend_page2 = 'Coding Life Anecdote'
    self_link = '/anecdote'
    band = 'green'
    return render_template('index.html' , theme = theme, subtitle = subtitle,friend_page1_link =friend_page1_link ,friend_page1 = friend_page1, friend_page2_link = friend_page2_link, friend_page2 = friend_page2, self_link = self_link, posts = posts, band = band)

@app.route('/home')
def home ():
    return render_template('home.html')

# post page series.....
@app.route('/poisson_distribution')
def poisson_distribution ():
    return render_template('/blog_article/poi_dist.html')

@app.route('/cow_carbon')
def cow_carbon ():
    return render_template('/blog_article/cow_carbon.html')

@app.route('/lemontart')
def lemontart ():
    return render_template('/blog_article/lemontart.html')

@app.route('/markenmeer')
def markenmeer ():
    return render_template('/blog_article/markenmeer.html')


app.run(debug=True, port=8000)