![Wizard!](wizard.png)

Print a wizard in your shell.

Because you are a **Wizard**.

# Cast your Wizard spell

    $ serverless deploy
    Serverless: Installing requirements of requirements.txt in .serverless...
    Serverless: Packaging service...
    Serverless: Excluding development dependencies...
    Serverless: Injecting required Python packages to package...
    Serverless: Uploading CloudFormation file to S3...
    Serverless: Uploading artifacts...
    Serverless: Uploading service .zip file to S3 (17.37 MB)...
    Serverless: Validating template...
    Serverless: Updating Stack...
    Serverless: Checking Stack update progress...
    ....................
    Serverless: Stack update finished...
    Service Information
    service: wizard-as-a-service
    stage: dev
    region: us-east-1
    stack: wizard-as-a-service-dev
    api keys:
    None
    endpoints:
    GET - https://19omnllgei.execute-api.us-east-1.amazonaws.com/dev/
    GET - https://19omnllgei.execute-api.us-east-1.amazonaws.com/dev/wip
    functions:
    magicspell: wizard-as-a-service-dev-magicspell
    wipspell: wizard-as-a-service-dev-wipspell

    $ curl https://19omnllgei.execute-api.us-east-1.amazonaws.com/dev

> Shazaaamm
