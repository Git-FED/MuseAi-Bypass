# Web clients — categorized catalog

This is a condensed, compliance-oriented catalog derived from the supplied Nov. 7, 2026 refresh. `LOW` generally means official/public or licensed; `MEDIUM` means third-party or fragile; `HIGH` means a route may circumvent a block or conflict with terms and is retained for completeness only. `UNVERIFIED` means do not claim current availability without a fresh check.

## Reddit and forums

- Stack Exchange API — `https://api.stackexchange.com/2.3/` — official public reads; LOW.
- Hacker News Firebase / Algolia APIs — `https://hacker-news.firebaseio.com/v0/`, `https://hn.algolia.com/api/v1/` — LOW.
- 4chan JSON API — `https://a.4cdn.org/` — public board/thread data; LOW-MEDIUM.
- Lemmy per-instance API — `https://<instance>/api/v3/` — public reads; LOW.
- Discord Bot API — `https://discord.com/developers` — invited servers only; LOW when compliant.
- Discourse JSON endpoints — `/t/{id}.json`, `/search.json` — per-forum public reads; LOW.
- Desuarchive / Palanq — public archive routes; MEDIUM.
- Redlib, Quetre, and similar mirrors — fragile and potentially ToS-conflicting; HIGH/UNVERIFIED, not recommended.

## Social

- Bluesky public AT Protocol API — `https://public.api.bsky.app` — LOW.
- Mastodon instance API and RSS — public profile/post surfaces; LOW.
- X official API and oEmbed — `https://developer.x.com`, `https://publish.twitter.com/oembed` — official, permissioned; LOW.
- Meta Graph APIs — `https://graph.facebook.com` — own-account/Page permissions; LOW and narrow.
- Pixelfed and Nostr web clients — separate federated networks, not mirrors of Instagram/X; LOW.
- FxTwitter, Imginn, Urlebird, Nitter instances, and similar viewers — third-party and fragile; MEDIUM-HIGH/HIGH.

## Video, music, and streaming

- YouTube Data API / oEmbed — official metadata routes; LOW.
- Twitch Helix — official API; app token required; LOW.
- Vimeo API and oEmbed — official metadata/embed routes; LOW.
- Dailymotion Data API — public reads available; LOW.
- PeerTube per-instance API and Sepia search — federated public video; LOW.
- TMDB, JustWatch, Trakt, and Reelgood — metadata/availability, not playback; LOW-MEDIUM.
- Spotify, SoundCloud, and Apple Music APIs — official, gated, and limited; LOW.
- Invidious, Piped, Grayjay, NewPipe, and yt-dlp — local/third-party clients; inspect terms and current instance health.
- Netflix, Disney+, Hulu, and similar SVOD playback — no compliant playback mirror; use the service's account and DRM player.

## Finance and payments

- Plaid, Yodlee, Finicity, MX, Akoya, and SnapTrade — user-authorized aggregation; LOW when consented.
- Schwab Trader API and Robinhood Crypto API — official, scoped account APIs; LOW.
- PayPal, Square, Stripe, and exchange APIs — merchant or account-owner scope; LOW.
- Banks, IRS personal accounts, SSA, Venmo personal accounts, and Cash App P2P — login/identity-gated; no agent-login alternative.

## News, search, and archives

- NYT Developer API, Guardian Open Platform, GDELT, Brave Search, Exa, Tavily, Firecrawl, NewsAPI, and Google News RSS — metadata/headlines or licensed/open content; verify quotas.
- BBC/NPR/Substack/Medium RSS — headline or feed content according to each publisher's terms.
- Internet Archive / Wayback — archived public pages; not a paywall-bypass route.
- Library access, PressReader, Libby, subscriptions, and publisher-authorized access — LOW and preferred for paywalled content.
- Paywall-removal sites, shared-session services, and archive tricks — HIGH and not recommended; hard paywalls remain hard stops.

## Shopping, travel, developer, government, and jobs

- eBay Browse, Etsy Open API, Shopify Storefront API, Ticketmaster Discovery, Duffel, and official partner APIs — gated official routes; LOW.
- Inside Airbnb — published research snapshots only; do not re-scrape; LOW for research.
- GitHub, GitLab, npm, PyPI, Hugging Face, Cloudflare, AWS, Azure, and GCP APIs/CLIs — official developer routes; LOW.
- CourtListener, govinfo, Justia Dockets, CMS, openFDA, ClinicalTrials.gov, EIA, and public court portals — public/open data; LOW within applicable rules.
- Greenhouse, Lever, Ashby, USAJOBS, Adzuna, The Muse, RemoteOK, Remotive, and Arbeitnow — public or key-gated job feeds; LOW within rate and attribution terms.
- LinkedIn, Indeed, Glassdoor, CoStar, Apartments.com, dating services, and patient portals — hard gates or no public route; do not scrape or automate around them.

## Research status

The supplied refresh reports approximately 372 category returns, about 160 carried-live entries, about 15 dead/degraded entries, about 182 additions, and about 72 unverified flags. These are worker-return sums, not deduplicated unique-client counts. Re-check current primary sources before relying on any entry.

