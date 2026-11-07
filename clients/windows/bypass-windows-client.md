# Windows client plan

## Safe implementation boundary

A Windows client may provide bookmarking, read-only catalog search, RSS/API consumption, local notes, and links to official providers. It must not automate login to another person's account, defeat a paywall or CAPTCHA, intercept DRM, rotate IPs to evade blocks, or send requests faster than the provider permits.

## Suggested components

- Static HTML/Markdown catalog for the interface.
- Official provider SDKs or HTTPS clients with least-privilege tokens.
- Windows Credential Manager or environment variables for local secrets.
- Explicit consent and an audit log for user-authorized integrations.
- Clear error handling that stops on `401`, `403`, CAPTCHA, MFA, or rate-limit responses.

