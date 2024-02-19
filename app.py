from flask import Flask, render_template, request, jsonify

# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# import requests
# from bs4 import BeautifulSoup


# uri = "mongodb+srv://username:password@cluster0.sevu3jt.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient(uri, server_api=ServerApi("1"))
# db = client.dbsparta
# all_users = list(db.users01.find({}, {"id": False}))
# print(all_users)
# db.testpedia.insert_one({"name": "jjiia"})

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


# @app.route("/movie", methods=["POST"])
# def post_movie():
#     url = request.form["url_give"]
#     rating = request.form["rating_give"]
#     comment = request.form["comment_give"]

#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
#     }
#     data = requests.get(url, headers=headers)
#     soup = BeautifulSoup(data.text, "html.parser")

#     image = soup.select_one('meta[property="og:image"]')["content"]
#     print(image)
#     title = soup.select_one('meta[property="og:title"]')["content"]
#     print(title)
#     description = soup.select_one('meta[name="description"]')["content"]
#     print(description)

#     print("movie_detail", url, rating, comment)
#     # db.testpedia.insert_one({"name": "tia"})
#     db.imdbpedia.insert_one(
#         {
#             "image": image,
#             "title": title,
#             "description": description,
#             "rating": rating,
#             "comment": comment,
#         }
#     )
#     return jsonify({"msg": "Post method"})


# # @app.route("/movie", methods=["GET"])
# # def get_movie():
# #     movie_list = list(db.imdbpedia.find({}, {"_id": False}))
# #     return jsonify({"movies": movie_list})


# # @app.route("/mypage")
# # def myPage():
#     return "This Is My Page"


if __name__ == "__main__":
    app.run()
    # app.run("0.0.0.0", port=5000, debug=True)
