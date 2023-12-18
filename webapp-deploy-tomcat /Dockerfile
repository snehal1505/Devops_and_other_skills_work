FROM tomcat
ENV MAVEN_VERSION 3.3.9

RUN mkdir -p /usr/share/maven \
  && curl -fsSL http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz \
    | tar -xzC /usr/share/maven --strip-components=1 \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven

VOLUME /root/.m2
RUN mvn -v
RUN useradd -m -d /opt/tomcat -U -s /bin/false tomcat
RUN apt-get update
RUN apt-get install default-jdk
RUN java -version

WORKDIR /tmp
RUN wget https://dlcdn.apache.org/tomcat/tomcat-10/v10.0.20/bin/apache-tomcat-10.0.20.tar.gz
RUN tar xzvf apache-tomcat-10*tar.gz -C /opt/tomcat --strip-components=1
RUN chown -R tomcat:tomcat /opt/tomcat/ \ && chmod -R u+x /opt/tomcat/bin



ADD java-code-base /opt/java-code-base
WORKDIR /opt/java-code-base
#RUN cd /opt/java-code-base
RUN mvn clean package
RUN ls -ltr  ./target/
RUN cp -r /opt/java-code-base/target/maven-web-application.war /usr/opt/tomcat/webapps/
#WORKDIR /usr/local/tomcat
#ADD maven-web-application.war /usr/local/tomcat/webapps
EXPOSE 8080
CMD ["/usr/opt/tomcat/bin/catalina.sh", "run"]

