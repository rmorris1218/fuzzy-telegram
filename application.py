from app import create_app, get_db

app = create_app()
db = get_db(app)

# from models import Result

if __name__ == '__main__':
    app.run(debug=True)
