import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "6H'-=4@8LAXR2N5ON3+REZI&LRFYPG@D_LG1OB2J/A)C*5&A8ZF8\\#WM\\2#W$XCG"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgres://qnwpgnurknhiub:5c6d63f0e383521bf2d39a401ca5aa6542ee3083bfe916a8ad560e69d8ecb4a8@ec2-54-246-92-116.eu-west-1.compute.amazonaws.com:5432/daqmle0p2g06lq"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
