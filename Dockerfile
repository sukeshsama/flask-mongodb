FROM registry.access.redhat.com/ubi8/python-38

# Add application sources with correct permissions for OpenShift
USER 0
ADD src /opt/app/
COPY requirements.txt /opt/app/requirements.txt
RUN chown -R 1001:0 ./
USER 1001

WORKDIR /opt/app

# Install the dependencies
RUN pip install -U "pip>=19.3.1" && \
    pip install -r ./requirements.txt

ENTRYPOINT [ "python" ]

# Run the application
CMD [ "app.py" ]
