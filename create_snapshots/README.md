# create_snapshots

## About

 This is a demo project to display info from EC2 instances.
 It uses the AWS credentials stored on your computer

   `python3 create_snapshots.py`

## Configuring create_snapshots

  create_snapshots uses the aws configuration file created by the AWS cli

  `aws configure --profile default`

## Running

  `python2 create_snapshots.py <command> <--name=TAG>`

  *command* includes: list, start, or stop
  *tag* is optional, and can be a wildcard character
