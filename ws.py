#!flask/bin/python
from __future__ import print_function
from flask import Flask, jsonify, abort, make_response,request
import sys
from Resources import comments
from Resources import posts
from Resources import photos
from Resources import todos
from Resources import users
from Resources import albums

app = Flask(__name__)


@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify({'posts': posts})


@app.route('/posts/<int:post_id>', methods=['GET'])
def get_task(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        abort(404)
    return jsonify({'post': post[0]})

@app.route('/posts', methods=['POST'])
def create_post():
    print(request.json, file=sys.stderr)
    if not request.json or not 'title' in request.json or not 'userId' in request.json or not 'body' in request.json:
        abort(400)
    post = {
        'id': posts[-1]['id'] + 1,
        'userId': request.json['userId'],
        'title': request.json['title'],
        'body': request.json['body'],
    }
    posts.append(post)
    return jsonify({'post': post}), 201

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post( post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        abort(404)
    if not request.json:
        abort(400)
    post[0]['title'] = request.json.get('title', post[0]['title'])
    post[0]['body'] = request.json.get('body', post[0]['body'])
    return jsonify({'post': post[0]})

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post( post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        abort(404)
    posts.remove(post[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)




############################### COMMENTS ####################################

@app.route('/comments', methods=['GET'])
def get_comments():

    return jsonify({'comments': comments})


@app.route('/comments/<int:comments_id>', methods=['GET'])
def get_task1(post_id):
    comment = [comment for comment in comments if comment['id'] == comment_id]
    if len(comment) == 0:
        abort(404)
    return jsonify({'comment': comment[0]})

@app.route('/comments', methods=['POST'])
def create_comment():
    print(request.json, file=sys.stderr)
    if not request.json or not 'name' in request.json or not 'email' in request.json or not 'body' in request.json:
        abort(400)
    comment = {
        'id': comments[-1]['id'] + 1,
        'name': request.json['name'],
        'email': request.json['email'],
        'body': request.json['body'],
    }
    comments.append(comment)
    return jsonify({'comment': comment}), 201

@app.route('/comments/<int:comment_id>', methods=['PUT'])
def update_comment( post_id):
    comment = [comment for comment in comments if comment['id'] == comment_id]
    if len(comment) == 0:
        abort(404)
    if not request.json:
        abort(400)
    comment[0]['title'] = request.json.get('title', comment[0]['title'])
    comment[0]['body'] = request.json.get('body', comment[0]['body'])
    return jsonify({'post': comment[0]})

@app.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment( comment_id):
    comment = [comment for comment in comments if comment['id'] == comment_id]
    if len(comment) == 0:
        abort(404)
    posts.remove(comment[0])
    return jsonify({'result': True})


############################### ALBUMS ####################################

@app.route('/albums', methods=['GET'])
def get_albums():

    return jsonify({'albums': albums})


@app.route('/albums/<int:albums_id>', methods=['GET'])
def get_task_albums(album_id):
    album = [album for album in albums if album['id'] == album_id]
    if len(album) == 0:
        abort(404)
    return jsonify({'album': album[0]})

@app.route('/albums', methods=['POST'])
def create_album():
    print(request.json, file=sys.stderr)
    if not request.json or not 'title' in request.json :
        abort(400)
    album = {
        'id': comments[-1]['id'] + 1,
        'title': request.json['title'],

    }
    albums.append(album)
    return jsonify({'album': album}), 201

@app.route('/albums/<int:album_id>', methods=['PUT'])
def update_comment( post_id):
    album = [album for album in albums if album['id'] == album_id]
    if len(album) == 0:
        abort(404)
    if not request.json:
        abort(400)
    album[0]['title'] = request.json.get('title', album[0]['title'])
    album[0]['body'] = request.json.get('body', album[0]['body'])
    return jsonify({'post': album[0]})

@app.route('/albums/<int:album_id>', methods=['DELETE'])
def delete_album( album_id):
    album = [album for album in albums if album['id'] == album_id]
    if len(album) == 0:
        abort(404)
    posts.remove(album[0])
    return jsonify({'result': True})

    ############################### USERS ####################################

    @app.route('/users', methods=['GET'])
    def get_users():

        return jsonify({'users': albums})


    @app.route('/users/<int:user_id>', methods=['GET'])
    def users(user_id):
        user = [user for user in users if user['id'] == user_id]
        if len(user) == 0:
            abort(404)
        return jsonify({'album': user[0]})

    @app.route('/users', methods=['POST'])
    def create_user():
        print(request.json, file=sys.stderr)
        if not request.json or not 'title' in request.json :
            abort(400)
        user = {
            'id': users[-1]['id'] + 1,
            'name': request.json['name'],
            'username': request.json['username'],
            'email': request.json['email'],
            'address': {
                'street': request.json['street'],
                'city': request.json['suite'],
                'zipcode': request.json['zipcode'],
                'geo':{
                    'lat': request.json['lat'],
                    'lng': request.json['lng']
                }
            }
            'phone': request.json['phone'],
            'website': request.json['website'],
            'company': {
                'name': request.json['name'],
                'catchPhrase': request.json['catchPhrase'],
                'bs': request.json['bs'],
            }

        }
        users.append(user)
        return jsonify({'user': user}), 201

    @app.route('/user/<int:auser_id>', methods=['PUT'])
    def update_user( user_id):
        user = [user for user in users if user['id'] == user_id]
        if len(user) == 0:
            abort(404)
        if not request.json:
            abort(400)
        user[0]['name'] = request.json.get('name', user[0]['name'])
        user[0]['username'] = request.json.get('username', user[0]['username'])
        user[0]['email'] = request.json.get('email', user[0]['email'])
        user[0]['address']['street'] = request.json.get('street', user[0]['address']['street'])
        user[0]['address']['suite'] = request.json.get('suite', user[0]['address']['suite'])
        user[0]['address']['city'] = request.json.get('city', user[0]['address']['city'])
        user[0]['address']['zipcode'] = request.json.get('street', user[0]['address']['zipcode'])
        user[0]['address']['geo']['lat'] = request.json.get('lat', user[0]['address']['geo']['lat'])
        user[0]['address']['geo']['lng'] = request.json.get('lng', user[0]['address']['geo']['lng'])
        user[0]['phone'] = request.json.get('phone', user[0]['phone'])
        user[0]['website'] = request.json.get('website', user[0]['website'])
        user[0]['company']['name'] = request.json.get('name', user[0]['company']['name'])
        user[0]['company']['catchPhrase'] = request.json.get('catchPhrase', user[0]['company']['catchPhrase'])
        user[0]['company']['bs'] = request.json.get('bs', user[0]['company']['bs'])



        return jsonify({'post': user[0]})

    @app.route('/albums/<int:album_id>', methods=['DELETE'])
    def delete_album( album_id):
        album = [album for album in albums if album['id'] == album_id]
        if len(album) == 0:
            abort(404)
        posts.remove(album[0])
        return jsonify({'result': True})



if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
