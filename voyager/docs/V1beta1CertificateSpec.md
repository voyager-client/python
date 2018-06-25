# V1beta1CertificateSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acme_staging_url** | **str** | ACME server that will be used to obtain this certificate. Deprecated | [optional] 
**acme_user_secret_name** | **str** | Secret contains ACMEUser information. Secret must contain a key &#x60;email&#x60; If empty tries to find an Secret via domains if not found create an ACMEUser and stores as a secret. Secrets key to be expected:  ACME_EMAIL -&gt; required, if not provided it will through error.  ACME_SERVER_URL -&gt; custom server url to generate certificates, default is lets encrypt.  ACME_USER_DATA -&gt; user data, if not found one will be created for the provided email,    and stored in the key. | 
**challenge_provider** | [**V1beta1ChallengeProvider**](V1beta1ChallengeProvider.md) | ChallengeProvider details to verify domains | 
**domains** | **list[str]** | Tries to obtain a single certificate using all domains passed into Domains. The first domain in domains is used for the CommonName field of the certificate, all other domains are added using the Subject Alternate Names extension. | [optional] 
**email** | **str** | Deprecated | [optional] 
**http_provider_ingress_reference** | [**V1beta1LocalTypedReference**](V1beta1LocalTypedReference.md) | This is the ingress Reference that will be used if provider is http Deprecated | [optional] 
**paused** | **bool** | Indicates that the certificate is paused. | [optional] 
**provider** | **str** | Following fields are deprecated and will removed in future version. https://github.com/appscode/voyager/pull/506 Deprecated. DNS Provider. | [optional] 
**provider_credential_secret_name** | **str** | ProviderCredentialSecretName is used to create the acme kubernetes.client, that will do needed processing in DNS. Deprecated | [optional] 
**storage** | [**V1beta1CertificateStorage**](V1beta1CertificateStorage.md) | Storage backend to store the certificates currently, kubernetes secret and vault. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


