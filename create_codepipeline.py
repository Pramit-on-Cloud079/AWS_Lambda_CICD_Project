import boto3

codepipeline = boto3.client('codepipeline')

pipeline_name = "LambdaCICDPipeline"
github_owner = "Pramit-on-Cloud079"
repo_name = "AWS_Lambda_CICD_Project"
branch_name = "master"  # or 'main' if your repo uses that
github_token = "xxxxxxxxxxxxxxx"  # Create a GitHub personal access token (classic)

response = codepipeline.create_pipeline(
    pipeline={
        'name': pipeline_name,
        'roleArn': 'arn:aws:iam::231299271232:role/CodePipelineServiceRole',
        'artifactStore': {
            'type': 'S3',
            'location': 'codepipeline-artifacts-pramit'
        },
        'stages': [
            {
                'name': 'Source',
                'actions': [
                    {
                        'name': 'SourceAction',
                        'actionTypeId': {
                            'category': 'Source',
                            'owner': 'ThirdParty',
                            'provider': 'GitHub',
                            'version': '1'
                        },
                        'outputArtifacts': [{'name': 'SourceOutput'}],
                        'configuration': {
                            'Owner': github_owner,
                            'Repo': repo_name,
                            'Branch': branch_name,
                            'OAuthToken': github_token
                        },
                        'runOrder': 1
                    }
                ]
            },
            {
                'name': 'Build',
                'actions': [
                    {
                        'name': 'BuildAction',
                        'actionTypeId': {
                            'category': 'Build',
                            'owner': 'AWS',
                            'provider': 'CodeBuild',
                            'version': '1'
                        },
                        'inputArtifacts': [{'name': 'SourceOutput'}],
                        'outputArtifacts': [{'name': 'BuildOutput'}],
                        'configuration': {
                            'ProjectName': 'LambdaCodeBuildProject'
                        },
                        'runOrder': 1
                    }
                ]
            }
        ],
        'version': 1
    }
)

print("✅ CodePipeline created:", response['pipeline']['name'])
