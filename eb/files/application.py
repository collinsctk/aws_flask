from flask import Flask, render_template
import os
import requests

# 默认目录为当前目录的templates
template_dir = os.path.abspath('./templates')

application = Flask(__name__, template_folder=template_dir)

@application.route('/')
def index():
    instance_id = requests.get("http://169.254.169.254/latest/meta-data/instance-id").text
    availability_zone = requests.get("http://169.254.169.254/latest/meta-data/placement/availability-zone").text
    return render_template('index.html',
                           devnet_main='乾颐堂AWS测试',
                           instance_id = instance_id,
                           availability_zone = availability_zone,
                           active='首页')


if __name__ == '__main__':
    application.debug = True
    application.run()