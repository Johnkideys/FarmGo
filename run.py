from FlaskBlog import create_app

app = create_app() #no need to pass argument as the default argument is already set to Config (in __init__.py)

#import os
#x = os.environ.get('EMAIL_USER')
#print(f'{x}')

if __name__ == '__main__':
    app.run()
