import uuid
import json
import logging
import tempfile
import shutil
import hashlib
import os


from jinja2 import contextfilter, TemplateSyntaxError
from formica.aws import AWS

logger = logging.getLogger(__name__)




@contextfilter
def template_filter(context, package_name):
    package = context.get('deployment_packages', {}).get(package_name, None)
    if package:
        return json.dumps({
            "S3Bucket": package.s3_bucket_name,
            "S3Key": package.s3_bucket_path,
        })
    else:
        line_number = 0 # TODO where to get the line number from?
        raise TemplateSyntaxError("Undefined deployment package '%s'" % package_name, line_number)


class DeploymentPackage:

    def __init__(self, stack_name, package_name):
        self.stack_name = stack_name
        self.package_name = package_name

        zipfile = self.create_zipfile()

        with open(zipfile, "rb") as file_to_check:
            data = file_to_check.read()
            archive_hash = hashlib.md5(data).hexdigest()

        self.s3_bucket_name = ("formica-dpkg-{}-{}".format(self.stack_name[:12], archive_hash[:24])).lower()
        self.s3_bucket_path = "deployment-package-{}.zip".format(archive_hash)


    def create_zipfile(self):
        temp_file = tempfile.NamedTemporaryFile().name 
        source = self.package_name
        shutil.make_archive(temp_file, "zip", "code")
        temp_file += ".zip"
        return temp_file


    def upload(self):
        session = AWS.current_session()
        s3_client = session.client("s3")

        logger.info("Creating bucket {} ...".format(self.s3_bucket_name))
        s3_client.create_bucket(
            Bucket=self.s3_bucket_name, CreateBucketConfiguration=dict(LocationConstraint=session.region_name)
        )

        zipfile = self.create_zipfile()

        logger.info("Uploading package ...")
        s3_client.upload_file(zipfile, self.s3_bucket_name, self.s3_bucket_path)



    def cleanup(self):
        session = AWS.current_session()
        s3_client = session.client("s3")

        s3_client.delete_object(Bucket=self.s3_bucket_name, Key=self.s3_bucket_path)
        s3_client.delete_bucket(Bucket=self.s3_bucket_name)
        

