from flask import Flask, request, abort, render_template
import subprocess

app = Flask(__name__)

@app.before_request
def filter_ips():
    # limit to localhost and 192.168.1.0/8
    allowed_ips = ["192.168.1.", "127.0.0.1"]
    for ip in allowed_ips:
        if ip in request.remote_addr:
            return
        
    abort(403)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/switch/<mode>", methods = ['POST'])
def switch(mode):
    if mode.lower() == 'mac':
        subprocess.run(["/bin/sh", "./switch_to_mac.sh"])
        return f'Switching to Mac mode.'
    elif mode.lower() == 'pc':
        subprocess.run(["/bin/sh", "./switch_to_pc.sh"])
        return f'Switching to PC mode.'
    else:
        return f'Unknown mode.'

if __name__ == '__main__':
    app.run(debug=False, port=9000, host="0.0.0.0")