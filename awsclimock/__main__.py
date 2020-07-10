import sys
from awsclimock.helpers import get_command_to_mock
from awsclimock.helpers import get_mocked_security_group_data

def main():
    aws_command = get_command_to_mock()

    if aws_command == 'describe-security-group':
        print(get_mocked_security_group_data())
    elif aws_command == 'describe-instances':
        print('Lets mock data from ec2 instances')
    else:
        print('I dont know this command yet!')


if __name__ == '__main__':
    main()
