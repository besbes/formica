from troposphere import apigateway, applicationautoscaling, autoscaling, awslambda, certificatemanager, \
    cloudformation, cloudfront, cloudtrail, cloudwatch, codebuild, codecommit, codedeploy, codepipeline, config, \
    constants, datapipeline, directoryservice, dynamodb, ec2, ecr, ecs, efs, elasticache, elasticbeanstalk, \
    elasticloadbalancing, elasticsearch, emr, events, firehose, iam, iot, kinesis, kms, logs, opsworks, policies, \
    rds, redshift, route53, sqs, sns, sdb, s3, ssm, waf, workspaces, elasticloadbalancingv2, Output, Parameter, \
    Base64, FindInMap, GetAtt, GetAZs, If, Equals, And, Or, Not, Join, Sub, Select, Ref, Condition, ImportValue, \
    Export, Tags

TROPOSPHERE_MODULES = [
    apigateway,
    applicationautoscaling,
    autoscaling,
    awslambda,
    certificatemanager,
    cloudformation,
    cloudfront,
    cloudtrail,
    cloudwatch,
    codebuild,
    codecommit,
    codedeploy,
    codepipeline,
    config,
    constants,
    datapipeline,
    directoryservice,
    dynamodb,
    ec2,
    ecr,
    ecs,
    efs,
    elasticache,
    elasticbeanstalk,
    elasticloadbalancing,
    elasticloadbalancingv2,
    elasticsearch,
    emr,
    events,
    firehose,
    iam,
    iot,
    kinesis,
    kms,
    logs,
    opsworks,
    policies,
    rds,
    redshift,
    route53,
    s3,
    sdb,
    sns,
    sqs,
    ssm,
    waf,
    workspaces,
]

CLOUDFORMATION_FUNCTIONS = [
    Base64, FindInMap, GetAtt, GetAZs, If, Equals, And, Or, Not, Join, Sub, Select, Ref, Condition, ImportValue,
    Export, Tags
]

CLOUDFORMATION_DECLARATIONS = [Output, Parameter]
