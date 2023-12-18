FROM python:3
RUN mkdir python-container
ADD helloworld.py /python-container
RUN cd python-container
WORKDIR /python-container
#RUN apt-get -y install touch
RUN touch output.txt
#EXPOSE 3333
CMD [ "python", "-u", "helloworld.py", ">", "output.txt"] 
#CMD ["/helloworld-output.sh"]
