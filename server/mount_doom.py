from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from base64 import b64encode

app = Flask(__name__)

def belongs_to(ring_id):
    if ring_id < 9:
        return "No way... Sauron is watching you"
    else:
        return "Dark Lord"


@app.before_request
def basic_auth_check():
    if request.url_rule.endpoint == 'ring' and request.view_args['ring_id'] == 9:
        basic_auth_value = request.environ.get('HTTP_AUTHORIZATION', '')
        if not is_frodon(basic_auth_value):
            return abort(403)


def is_frodon(basic_auth_value):
    name = 'frodon.sacquet'
    password = 'i_m_secretly_in_love_with_my_friend_sam_gamegie'

    expected = 'Basic ' + b64encode('{0}:{1}'.format(name, password))
    return basic_auth_value == expected


@app.route('/rings/<int:ring_id>.<format>', methods=['GET'])
def ring(ring_id, format):
    precious_message = "One Ring to rule them all, One Ring to find them One Ring to bring them all and in the darkness bind them"
    message = precious_message if ring_id == 9 else ""
    if format == 'json':
        return jsonify(id=ring_id, owner=belongs_to(ring_id),
                message=message)
    else:
        return "Want it ? Contribute !"

if __name__ == '__main__':
    app.run()
