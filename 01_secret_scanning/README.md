# Secret Scanning

Secret scanning is a feature that scans repositories for secrets, such as API keys, that have been accidentally exposed. When a secret is found, GitHub will send an alert to the repository owner and the user who committed the code.

## GitHub: Configuring secret scanning for your repositories

You can enable secret scanning alerts for users for any free public repository that you own. Once enabled, secret scanning scans for any secrets in your entire Git history on all branches present in your GitHub repository.

- [Enabling secret scanning alerts for users](https://docs.github.com/en/code-security/secret-scanning/configuring-secret-scanning-for-your-repositories)

The `01_api_call.py` file contains a secret key. Try to push this file to your repository and see what happens. Enable secret scanning alerts for users and see how GitHub alerts you about the secret key.


## detect-secrets tool demo
detect-secrets is an aptly named module for detecting secrets within a code base. Unlike other similar packages that solely focus on finding secrets, this package is designed with the enterprise client in mind: providing a backwards compatible means to prevent new secrets from entering the code base.

- https://github.com/Yelp/detect-secrets
- https://github.com/gitleaks/gitleaks