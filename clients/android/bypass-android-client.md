# Android client plan

A compliant Android client can present public feeds, official APIs, local datasets, and links to provider apps. For account access, use provider OAuth or the provider's own app. Do not use accessibility automation, patched clients, linked-device impersonation, cookie import, certificate interception, or download features to defeat a service's controls.

Recommended controls: minimal permissions, encrypted local storage, user-visible consent, revocable tokens, no background scraping, backoff on `429`, and immediate stop on authentication or anti-bot challenges.

