Ansible AWS Examples
====================

A collection of examples using Ansible to manage AWS resources.


## Simple Web Application

A simple web service consisting of an EC2 instance behind an ELB. Useful for testing simple services.

Resources:

- EC2
- ELB
- Security Groups


## Simple Web Application HA Configuration

A more advanced example configuring a launch configuration with auto-scaling group to provide a HA solution.

Resources:

- EC2
- ELB
- Security Groups


## Simple Database Application

A stand-alone RDS instance paired with an EC2 instance.

Resources:

- EC2
- RDS
- Security Groups


## Simple Cache Application

A simple service that reads requests and stores them in Redis.

Resources:

- EC2
- Elasticache
- Security Groups
