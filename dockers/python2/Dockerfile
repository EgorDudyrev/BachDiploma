# We will use Ubuntu for our image
FROM ubuntu

# Updating Ubuntu packages
RUN apt-get update && yes|apt-get upgrade

# Adding wget and bzip2
RUN apt-get install -y wget bzip2

# Anaconda installing
RUN wget https://repo.continuum.io/archive/Anaconda2-5.0.1-Linux-x86_64.sh
RUN bash Anaconda2-5.0.1-Linux-x86_64.sh -b
RUN rm Anaconda2-5.0.1-Linux-x86_64.sh

# Set path to conda
ENV PATH /root/anaconda2/bin:$PATH

# Updating Anaconda packages
RUN conda update conda
RUN conda update anaconda
RUN conda update --all

# Updating my additional packages
RUN pip install --upgrade pip
RUN conda uninstall numpy -y
RUN conda install numpy==1.14
RUN conda install pandas==0.23.4
RUN conda install matplotlib
RUN apt-get install ffmpeg -y
RUN pip install ffmpeg
RUN pip install ffprobe
RUN pip install pydub==0.23.0

# Configuring access to Jupyter
RUN mkdir /opt/notebooks
RUN jupyter notebook --generate-config --allow-root
RUN echo "c.NotebookApp.password = u'sha1:6a3f528eec40:6e896b6e4828f525a6e20e5411cd1c8075d68619'" >> /root/.jupyter/jupyter_notebook_config.py


# Jupyter listens port and Tensorboard port: 8889
EXPOSE 8889
# Run Jupytewr notebook as Docker main process
CMD ["jupyter", "notebook", "--allow-root", "--notebook-dir=/opt/notebooks", "--ip='*'", "--port=8889", "--no-browser"]


