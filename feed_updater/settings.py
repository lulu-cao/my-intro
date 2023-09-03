'''
all configutation variables are stored in this file
'''

# config = {
#     'endpoint': 'https://zenquotes.io/api/today',
#     'title': 'title',
#     'url': {
#         'pattern': 'https://zenquotes.io/api/{}/{}',
#         'keys': ['today', ''],
#     }
# }
config = {
    'endpoint': 'https://alirezayahyapour.pythonanywhere.com/api/v1/posts',
    'title': 'title',
    'url': {
        'pattern': 'https://alirezayahyapour.pythonanywhere.com/{}/{}',
        'keys': ['lang', 'slug'],
    }
}
