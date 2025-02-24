import docker
from flask import render_template, jsonify

from app.core.monitor import DockerMonitor
from app.home import blueprint

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('pages/index.html', segment='dashboard')

@blueprint.route('/real-time', methods=['GET'])
def real_time():

    return render_template('pages/real-time.html', segment='real_time')



@blueprint.route('/profile', methods=['GET'])
def profile():
    return render_template('pages/index.html', segment='profile')

# @blueprint.app_template_filter('replace_value')
# def replace_value(value, args):
#   return value.replace(args, " ").title()

@blueprint.app_template_filter('replace_value')
def replace_value(value, args):
  return value.replace(args, " ").title()


# @blueprint.route('/proc', methods=['POST'])
# def proc():
#     container_list = ["postgres", "redis"]
#
#     try:
#         monitor = DockerMonitor()
#         res = monitor.state_(container_list)
#         return jsonify({"code": 200,"data":res}), 200
#
#         # while True:
#         #     print(f"Original list: {container_list}")
#         #     shutdown_list = monitor.state_(container_list)
#         #     print(f"Remaining containers: {shutdown_list}")
#         #     time.sleep(1)
#     except docker.errors.DockerException as e:
#         print(f"Failed to connect to Docker. {e}")
