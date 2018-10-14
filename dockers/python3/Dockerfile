# We will use Ubuntu for our image
FROM ubuntu

# Updating Ubuntu packages
RUN apt-get update && yes|apt-get upgrade

# Adding wget and bzip2
RUN apt-get install -y wget bzip2

# Anaconda installing
RUN wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
RUN bash Anaconda3-5.0.1-Linux-x86_64.sh -b
RUN rm Anaconda3-5.0.1-Linux-x86_64.sh

# Set path to conda
ENV PATH /root/anaconda3/bin:$PATH

# Updating Anaconda packages
RUN conda update conda
RUN conda update anaconda
RUN conda update --all

# Updating my additional packages
RUN pip install --upgrade pip
RUN pip uninstall numpy -y
RUN pip install numpy==1.14
RUN pip install pandas==0.23.4
RUN pip install scipy==1.1.0
RUN pip install scikit-learn==0.20.0
RUN pip install ipykernel==4.10.0
RUN pip install tensorflow==1.5.0
RUN pip install keras==2.2.2
RUN pip install pydub==0.23.0
RUN pip install matplotlib
RUN pip install stft

# Configuring access to Jupyter
RUN mkdir /opt/notebooks
RUN jupyter notebook --generate-config --allow-root
RUN echo "c.NotebookApp.password = u'sha1:6a3f528eec40:6e896b6e4828f525a6e20e5411cd1c8075d68619'" >> /root/.jupyter/jupyter_notebook_config.py


# Jupyter listens port and Tensorboard port: 8888 6006
EXPOSE 8888 6006
# Run Jupytewr notebook as Docker main process
CMD ["jupyter", "notebook", "--allow-root", "--notebook-dir=/opt/notebooks", "--ip='*'", "--port=8888", "--no-browser"]


