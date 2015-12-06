# sizeupsnacks
The best of snacks, the worst of snacks.


# deploy

We are using elastic beanstalk to run and deploy the application. I used the following link to setup the project. 
(AWS Flask ElasticBeanstalk)[http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html]


First you will need the awsebcli packge to run the commands:

    pip install awsebcli


The default url for UI is: http://snacks-dev.elasticbeanstalk.com/

To install lxml on windows go to http://www.lfd.uci.edu/~gohlke/pythonlibs/ and get the latest lxml whl file.
After downloading run:
    pip install <whlFile>

Example:
    pip install lxml‑3.5.0‑cp35‑none‑win_amd64.whl