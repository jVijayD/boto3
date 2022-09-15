import boto3


def ses():
    client = boto3.client('ses')
    response = client.list_identities(IdentityType='EmailAddress')
    dd = response['Identities']
    # print(dd)
    response1 = client.get_identity_verification_attributes(
        Identities=dd)
    bda = response1['VerificationAttributes']
    for dda in r['VerificationStatus']:
        print(dda)


ses()
