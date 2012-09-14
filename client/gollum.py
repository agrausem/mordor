import spyre

spec_filepath = '../server/lord_of_the_ring.json'

gollum_client = spyre.new_from_spec(
        spec_filepath,
        base_url="http://localhost:5000")

gollum_client.enable('auth.Basic', username="gollum",
    password="i_killed_my_cousin_for_the_precious_true_story")

while True:
    try:
        response = gollum_client.get_precious(format='json')
        assert(response.status==403)
        print 'I want my precious'
    except (Exception, KeyboardInterrupt) as e:
        print "\n\nYOU'RE SUCH A BAD GUY ! MY PRECIOUS ! HE'S MINE !"
        break
