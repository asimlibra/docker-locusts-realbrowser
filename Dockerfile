FROM hakobera/locust
RUN apt-get update -y && apt-get install -y python-pip git
RUN pip install selenium 
RUN pip install --upgrade --ignore-installed urllib3
RUN git clone https://github.com/asimlibra/realbrowserlocusts.git
RUN cd realbrowserlocusts && python setup.py install && cd -

# Add a user for running applications.
RUN useradd apps
RUN mkdir -p /home/apps && chown apps:apps /home/apps


# Install wget.
RUN apt-get install -y wget unzip
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Install Chrome.
RUN apt-get update && apt-get -y install google-chrome-stable
RUN wget https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/bin/

ADD ./test /test
ENV SCENARIO_FILE /test/locustfile.py
