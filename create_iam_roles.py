import boto3

iam = boto3.client('iam')

def create_role(role_name, policy_arns, trust_policy):
    try:
        print(f"Creating role: {role_name}")
        iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=trust_policy
        )
        for policy_arn in policy_arns:
            iam.attach_role_policy(RoleName=role_name, PolicyArn=policy_arn)
    except iam.exceptions.EntityAlreadyExistsException:
        print(f"Role {role_name} already exists.")

# Trust policies
lambda_trust = '''{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"Service": "lambda.amazonaws.com"},
    "Action": "sts:AssumeRole"
  }]
}'''

codebuild_trust = '''{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"Service": "codebuild.amazonaws.com"},
    "Action": "sts:AssumeRole"
  }]
}'''

codepipeline_trust = '''{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"Service": "codepipeline.amazonaws.com"},
    "Action": "sts:AssumeRole"
  }]
}'''

# Create roles
create_role("LambdaCICDExecutionRole", [
    "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
], lambda_trust)

create_role("LambdaCICDCodeBuildRole", [
    "arn:aws:iam::aws:policy/AWSCodeBuildDeveloperAccess"
], codebuild_trust)

create_role("LambdaCICDCodePipelineRole", [
    "arn:aws:iam::aws:policy/AWSCodePipelineFullAccess",
    "arn:aws:iam::aws:policy/AWSLambdaFullAccess",
    "arn:aws:iam::aws:policy/AWSCodeBuildDeveloperAccess"
], codepipeline_trust)
