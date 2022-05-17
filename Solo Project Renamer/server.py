from flask_app import app
from flask_app.controllers import renamers,users
# remember to add the python files from controllers
if __name__=="__main__":
    app.run(debug=True)