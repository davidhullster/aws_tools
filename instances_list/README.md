```Usage: instances_list.py [OPTIONS] COMMAND [ARGS]...

  Commands for instances

Options:
  --help  Show this message and exit.

Commands:
  ip    List EC2 ip addresses
  list  List EC2 instances


instances_list dhull$ python3 instances_list.py ip --help
Usage: instances_list.py ip [OPTIONS]

  List EC2 ip addresses

Options:
  --tag TEXT      Only instances with tag (Name:<name>)
  --profile TEXT  Optional AWS profile name to specify AWS auth profile
  --az TEXT       Optional AWS Availability Zone
  --help          Show this message and exit.


instances_list dhull$ python3 instances_list.py list --help
Usage: instances_list.py list [OPTIONS]

  List EC2 instances

Options:
  --tag TEXT      Only instances for tag (Name:<name>)
  --profile TEXT  Optional AWS profile name to specify AWS auth profile
  --az TEXT       Optional AWS Availability Zone
  --help          Show this message and exit.
```
