# SAST into a simple web app

This repo is a fork [macloo/basic-flask-app](rom https://github.com/macloo/basic-flask-app) to which containerization and a simple SAST was introduced

## Containerization

In order to provide a working flask environment that can successfully serve our simple flask application, the uwsgi & nginx path was selected. 
`tiangolo/uwsgi-nginx-flask` was selected as the parent image and the application source is copied into the container. No additional container hardening 
was implemented as it seemed out of scope of this technical assessment.

In order to spin up the application a simple script was introduced that groups together `docker build` and `docker run`:

```bash
$ ./start.sh
```
Will expose the application to local port 8000 (http://127.0.0.1:8000).

## SAST

In order to introduce static security testing to the repo the open source [semgrep](https://semgrep.dev/) analyzer is employed. 

As a CI/CD mimicking tool, a Docker's Compose was employed by introducing semgrep's container and the containerized application as two services. Semgrep provides a scanning mode
which is suitable for CI integration which exits with a non 0 return code if something is wrong. As such, the docker compose can depend on this functionality
when building the services. 

First the source code is being scanned and if any problems arise it will exit with a non 0 code. The build of the web app depends on a successful completion of the 
SAST service. As such deployment will fail if any non-informational vulnerabilities arise.

To run a *"deployment"*: 

```bash
$ docker-compose up
```
An XSS vulnerability was introduced into `main.py` by rendering unsanitized GET parameter in the DOM under route hello:
```python
@app.route('/hello')
def hello():
    return render_template_string("<div>Hello: %s</div>" % request.args.get("name"))
```
To demonstrate the vulnerability, start the application with `start.sh` script(which bypasses the SAST) and visit: http://127.0.0.1:8000/hello?name=%3Cscript%3Ealert(%22hire%20me%20\;\)%22)%3C/script%3E

When running in our CI/CD mimicking pipeline, semgrep identifgies the problems and exits as a result the application's container is not built and the deployment of vulnerable application version is averted.
