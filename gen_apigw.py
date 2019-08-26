import urllib, subprocess, os

urllib.urlretrieve ("https://raw.githubusercontent.com/fmontezuma/terraform-generate-apigw-modules/master/generate_tf_apigw_modules.py", "generate_tf_apigw_modules.py")
urllib.urlretrieve ("https://raw.githubusercontent.com/fmontezuma/terraform-generate-apigw-modules/master/generate_tf_apigw.py", "generate_tf_apigw.py")

subprocess.call(["python", "generate_tf_apigw_modules.py",  "./config.json"])

os.remove("generate_tf_apigw_modules.py")
os.remove("generate_tf_apigw.py")

     
     