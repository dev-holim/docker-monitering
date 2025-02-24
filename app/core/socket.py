import time
import docker
from flask import jsonify
from flask_socketio import Namespace, emit, disconnect

from app.core.monitor import DockerMonitor


class DockerSocket(Namespace):
    def __init__(self, namespace=None, socketio_instance=None):
        super().__init__(namespace)
        self.is_active = True  # 연결 상태 플래그
        self.socketio = socketio_instance

    def on_connect(self):
        emit('server_response', {'status': "start"})
        self.is_active = True  # 연결 상태 활성화

    def on_client_event(self, response=None):
        # print(response)
        def monitor_containers():
            while self.is_active:
                try:
                    monitor = DockerMonitor()
                    data = monitor.container_list()
                    self.socketio.emit('server_response', {'status': "running",'code': 200, "data": data}, namespace='/docker')
                    time.sleep(1)  # 작업 간격
                # except docker.errors.NotFound as e:
                #     print(f"Container {container_name_or_id} not found.")
                #     break
                except docker.errors.DockerException as e:
                    print(f"Failed to connect to Docker. {e}")
                    break

        self.socketio.start_background_task(monitor_containers)

    @staticmethod
    def on_end_connection(data):
        emit('server_response', {'status': "disconnect",'message': "Disconnecting client..."})
        disconnect()

    def on_disconnect(self):
        self.is_active = False
        print("Client disconnected")