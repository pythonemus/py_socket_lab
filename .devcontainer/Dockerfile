# Use the official Red Hat UBI as the base image
FROM registry.access.redhat.com/ubi8/ubi

# Set metadata
LABEL maintainer="Your Name <your.email@example.com>"

# Install necessary packages
RUN yum install -y python3 python3-pip

# Set Python 3.12 as the default python interpreter
RUN alternatives --set python /usr/bin/python3

# Upgrade pip and install required Python packages
RUN pip3 install --upgrade pip
RUN pip3 install \
    python-socketio

# Set the default working directory
WORKDIR /workspace

# Specify entry point
CMD ["bash"]
