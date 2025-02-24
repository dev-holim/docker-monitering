from app import create_app, create_socketio

app = create_app()
socketio = create_socketio(app)

if __name__ == '__main__':
    app.run(socketio, debug=True)