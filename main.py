from flask import Flask, json,jsonify,request
import csv

all_movies=[]

with open("movie.csv",encoding="utf-8")as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]

likedmovie=[]
didnotlikemovie=[]
didnotwatchmovie=[]

app=Flask(__name__)
@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data":all_movies[0], 
        "status":"success"
    })

@app.route("/liked-movie",methods=["POST"])
def liked_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    likedmovie.append(movie)
    return jsonify({
        "status":"success"
    }),201
    
@app.route("/did-not-like-movie",methods=["POST"])
def did_not_like_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    didnotlikemovie.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/did-not-watch-movie",methods=["POST"])
def did_not_watch_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    didnotwatchmovie.append(movie)
    return jsonify({
        "status":"success"
    }),201

if __name__=="__main__":
    app.run()