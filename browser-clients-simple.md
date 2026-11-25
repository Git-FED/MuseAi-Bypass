# Client sites — simple list

One line per client: Client — for Site — URL. Live/public or official routes; availability and terms must be rechecked.

**Updated Nov 25, 2026. 126 entries (95 in the file from the Nov 7, 2026 refresh + 31 new).**
**Tested Nov 25, 2026:** original 95 URLs — 76 live, 6 redirect (site alive), 13 bot-blocked from the test VM (site live), 0 dead. New 31 candidates — 0 dead, all live or browser-verified live. Full test tables: `test-existing-92.md` and `test-new-30.md` in this folder.

## Reddit & forums
- Stack Exchange API — for Stack Overflow — https://api.stackexchange.com
- 4chan JSON API — for 4chan — https://a.4cdn.org
- Hacker News API — for Hacker News — https://hacker-news.firebaseio.com
- Lemmy API — for Lemmy — https://lemmy.world
- Discord Bot API — for Discord — https://discord.com/developers
- Desuarchive — for 4chan — https://desuarchive.org
- PieFed — for forums — https://piefed.social
- Discuit — for forums — https://discuit.net
- RedReader — for Reddit — https://github.com/QuantumBadger/RedReader
- Reddit Data API — for Reddit — https://www.reddit.com/dev/api — NEW Nov 25. Official OAuth route, 100 queries/min free. Approval required for every new client under the Nov 2025 Responsible Builder Policy; reports say new public-API requests stopped Oct 31, 2026 and remaining public access is scheduled to close Mar 2027, verify before relying.

## Social
- Bluesky Public API — for Bluesky — https://public.api.bsky.app
- Mastodon API + RSS — for Mastodon — https://mastodon.social
- X Official API — for X — https://developer.x.com — NOTE Nov 25: X moved to pay-per-use Feb 6, 2026, no subscriptions. Published rates: $0.005 per post read, $0.20 per post containing a URL.
- X oEmbed — for X — https://publish.twitter.com/oembed
- Meta Graph API — for Instagram / Facebook / Threads — https://graph.facebook.com
- Pixelfed — for Instagram alternative — https://pixelfed.org
- Primal — for Nostr — https://primal.net
- TikTok Display API — for TikTok — https://developers.tiktok.com/docs/en/display-api-get-started — NEW Nov 25. Official OAuth route to a user's own profile and video list. Gated: app review + approved scopes.
- TikTok Research API — for TikTok — https://developers.tiktok.com/products/research-api/ — NEW Nov 25. Only legitimate bulk route to public TikTok data. Academic / non-commercial only, application + 4-8 week wait.
- Instagram Graph API — for Instagram — https://developers.facebook.com/docs/instagram-api — NEW Nov 25. Business/Creator accounts, media, insights, publishing, hashtag search. Basic Display API sunset Sep 2025, this is the live route.
- Threads API — for Threads — https://developers.facebook.com/docs/threads — NEW Nov 25. Publish/read/reply-moderate/insights on graph.threads.net. Webhooks + keyword search added 2026. Free, needs Meta app + Tech Provider verification for production.
- LinkedIn API — for LinkedIn — https://learn.microsoft.com/en-us/linkedin/marketing/quick-start — NEW Nov 25. Official, heavily gated: app + product approval, partner tier for Community Management.
- Pinterest API v5 — for Pinterest — https://developers.pinterest.com/docs/getting-started/set-up-authentication-and-authorization/ — NEW Nov 25. Official OAuth API: boards, Pins, media upload, catalogs. Trial access 1,000 calls/day.
- FxEmbed feeds — for X / Bluesky — https://docs.fxembed.com/guide/advanced/rss-atom-feeds/ — NEW Nov 25. Per-profile RSS/Atom feeds, verified live Nov 20, 2026. Profile feeds only, no lists/search. MEDIUM, third-party.
- Matrix Client-Server API — for Matrix / Element — https://spec.matrix.org/v1.10/client-server-api/ — NEW Nov 25. Open federated standard, no central gatekeeper.

## Video / music
- YouTube Data API — for YouTube — https://developers.google.com/youtube/data
- YouTube oEmbed — for YouTube — https://www.youtube.com/oembed
- Twitch Helix API — for Twitch — https://dev.twitch.tv
- Vimeo API — for Vimeo — https://developer.vimeo.com
- TMDB API — for movies / TV metadata — https://www.themoviedb.org
- Spotify Web API — for Spotify — https://developer.spotify.com
- SoundCloud API — for SoundCloud — https://developers.soundcloud.com
- Dailymotion Data API — for Dailymotion — https://api.dailymotion.com
- PeerTube — for federated video — https://joinpeertube.org
- JustWatch — for streaming availability — https://www.justwatch.com
- Trakt API — for streaming metadata — https://trakt.tv

## Finance
- Plaid — for banks — https://plaid.com
- SnapTrade — for brokerages — https://snaptrade.com
- Schwab Trader API — for Schwab — https://developer.schwab.com
- Robinhood Crypto API — for Robinhood crypto — https://docs.robinhood.com/crypto/trading
- PayPal API — for PayPal — https://developer.paypal.com
- Square API — for merchant payments — https://developer.squareup.com/us/en
- Stripe API — for Stripe — https://stripe.com/docs/api
- Coinbase API — for Coinbase — https://docs.cdp.coinbase.com
- SEC EDGAR APIs — for US public companies — https://www.sec.gov/edgar/search/ — NEW Nov 25. Every US public filing as JSON at data.sec.gov, full-text search at efts.sec.gov. No key. Descriptive User-Agent header is mandatory.
- FRED API — for US + global macro data — https://fred.stlouisfed.org/docs/api/fred/overview.html — NEW Nov 25. 800k+ economic series. Free key, instant signup.
- World Bank Indicators API — for global development data — https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation — NEW Nov 25. About 16,000 indicators for 200+ economies, no key.

## News / search
- NYT API — for NYT — https://developer.nytimes.com
- Guardian Open Platform — for Guardian — https://open-platform.theguardian.com
- Substack RSS — for Substack — https://substack.com/feed
- Google News RSS — for Google News — https://news.google.com/rss
- Brave Search API — for search — https://brave.com/search/api/
- NewsAPI — for news — https://newsapi.org
- GDELT — for news data — https://www.gdeltproject.org
- Internet Archive — for archives — https://web.archive.org
- BBC RSS — for BBC — https://feeds.bbci.co.uk
- NPR RSS — for NPR — https://www.npr.org

## Shopping / travel
- eBay API — for eBay — https://developer.ebay.com
- Etsy API — for Etsy — https://developer.etsy.com
- Shopify Storefront API — for Shopify — https://shopify.dev/docs
- Inside Airbnb — for Airbnb data — https://insideairbnb.com
- Ticketmaster Discovery API — for Ticketmaster — https://developer.ticketmaster.com
- Duffel — for flights and stays — https://duffel.com

## Developer / cloud
- GitHub API — for GitHub — https://api.github.com
- GitLab API — for GitLab — https://gitlab.com/api/v4
- npm registry — for npm — https://registry.npmjs.org
- Hugging Face API — for Hugging Face — https://huggingface.co
- Ollama — for local models — https://ollama.com
- Cloudflare API — for Cloudflare — https://developers.cloudflare.com
- AWS CLI — for AWS — https://aws.amazon.com/cli/
- Google Cloud SDK — for GCP — https://cloud.google.com/sdk

## Government / courts / health
- CourtListener — for courts — https://www.courtlistener.com
- govinfo — for federal documents — https://www.govinfo.gov
- Justia — for dockets — https://dockets.justia.com
- IRS TEOS — for nonprofits — https://www.irs.gov/charities-non-profits/tax-exempt-organization-search
- ProPublica Nonprofit Explorer — for nonprofits — https://projects.propublica.org/nonprofits
- openFDA — for FDA data — https://open.fda.gov/apis/
- ClinicalTrials.gov API — for trials — https://clinicaltrials.gov/data-api/api
- CMS open data — for Medicare / Medicaid — https://data.cms.gov
- EIA API — for energy data — https://www.eia.gov/opendata

## Messaging / creator
- Telegram Bot API — for Telegram — https://core.telegram.org/bots/api
- Slack API — for Slack — https://api.slack.com
- Gmail API — for Gmail — https://developers.google.com/workspace/gmail/api/guides
- Microsoft Graph — for Outlook — https://learn.microsoft.com/en-us/graph
- Patreon API — for Patreon — https://docs.patreon.com
- DeviantArt API — for DeviantArt — https://www.deviantart.com/developers
- Gumroad API — for Gumroad — https://api.gumroad.com
- WhatsApp Cloud API — for business messaging — https://developers.facebook.com/docs/whatsapp/cloud-api

## Gaming / sports
- Steam Web API — for Steam — https://api.steampowered.com
- SteamDB — for Steam metadata — https://steamdb.info
- IGDB — for games — https://api.igdb.com
- The Odds API — for sports odds — https://the-odds-api.com
- Polymarket Gamma API — for Polymarket — https://gamma-api.polymarket.com
- Kalshi API — for Kalshi — https://docs.kalshi.com/welcome
- ESPN public data — for ESPN — https://www.espn.com
- IMDb Datasets — for IMDb — https://datasets.imdbws.com
- OMDb API — for movie metadata — https://www.omdbapi.com

## Jobs / housing / education
- Greenhouse API — for jobs — https://developers.greenhouse.io
- Lever Postings API — for jobs — https://github.com/lever/postings-api
- USAJOBS API — for federal jobs — https://developer.usajobs.gov
- Adzuna API — for jobs — https://developer.adzuna.com
- The Muse API — for jobs — https://www.themuse.com/developers/api/v2
- RemoteOK feed — for remote jobs — https://remoteok.com/api
- Remotive API — for remote jobs — https://remotive.com/api
- Arbeitnow API — for jobs — https://arbeitnow.com/api/job-board-api
- Redfin Data Center — for aggregate housing data — https://www.redfin.com/news/data-center
- Census ACS API — for housing enrichment — https://api.census.gov/data.html

## Maps / geo — NEW SECTION Nov 25
- Overpass API — for OpenStreetMap — https://overpass-api.de/api/ — NEW Nov 25. Query the whole OSM planet by tag/location/proximity. Read-only, free, self-hostable.
- Nominatim — for OpenStreetMap geocoding — https://nominatim.openstreetmap.org/search — NEW Nov 25. Free forward + reverse geocoding, no key. Max 1 req/sec, identifying User-Agent required, no bulk/autocomplete on the public instance.

## Knowledge / research — NEW SECTION Nov 25
- Wikimedia APIs — for Wikipedia / Wikidata — https://www.mediawiki.org/wiki/API:Wikidata — NEW Nov 25. MediaWiki Action API at en.wikipedia.org/w/api.php plus Wikidata API + SPARQL at query.wikidata.org. Free, keyless. Note: SPARQL endpoint blocks some datacenter IPs.
- OpenAlex API — for scholarly research — https://help.openalex.org/api/ — NEW Nov 25. 250M+ works, free, no key, all data CC0.
- Crossref REST API — for DOI metadata — https://api.crossref.org — NEW Nov 25. 140M+ works, free, no key.
- Semantic Scholar Academic Graph API — for scholarly research — https://www.semanticscholar.org/product/api/tutorial — NEW Nov 25. 200M+ papers, free, optional free key for higher limits.
- OpenCitations API — for scholarly citations — https://api.opencitations.net/index/v2 — NEW Nov 25. Open citation edges, free, no key.
- arXiv API — for preprints — https://info.arxiv.org/help/api/user-manual.html — NEW Nov 25. Free, keyless Atom API over 2M+ preprints.
- PubMed E-utilities — for biomedicine — https://www.ncbi.nlm.nih.gov/books/NBK25500/ — NEW Nov 25. Search + fetch 38 NCBI databases at eutils.ncbi.nlm.nih.gov. Free, free API key raises the rate.

## Weather / space — NEW SECTION Nov 25
- National Weather Service API — for US weather — https://www.weather.gov/documentation/services-web-api — NEW Nov 25. Official US forecasts, alerts, observations as GeoJSON at api.weather.gov. Free, no key, just a User-Agent.
- Open-Meteo API — for global weather — https://open-meteo.com/ — NEW Nov 25. Free, keyless JSON forecasts + ERA5 history back to 1940. 10k calls/day free non-commercial.
- NASA Open APIs — for NASA — https://api.nasa.gov/ — NEW Nov 25. APOD, Mars rover photos, Earth imagery, asteroids/NEO, space weather. Free key signup, DEMO_KEY for testing.

## Books / publishing — NEW SECTION Nov 25
- Open Library API — for books — https://openlibrary.org/dev/docs/api/books — NEW Nov 25. 20M+ book records, free, no key.
- Gutendex — for public-domain ebooks — https://gutendex.com/ — NEW Nov 25. 75k+ public-domain ebooks with direct links to full text. Free, no key.
- Google Books API — for Google Books — https://developers.google.com/books/docs/v1/using — NEW Nov 25. Full-text search + volume metadata. Public data needs only an API key.
- WordPress REST API — for WordPress — https://developer.wordpress.org/rest-api/reference/posts/ — NEW Nov 25. Every WP site exposes /wp-json/wp/v2/. Public posts readable keyless.
- Ghost Content + Admin APIs — for Ghost CMS — https://ghost.org/docs/ — NEW Nov 25. Read-only Content API for published posts, JWT Admin API for full read/write.
- Medium RSS feeds — for Medium — https://medium.com/feed/@username — NEW Nov 25. RSS only, NOT an API: Medium stopped issuing new integration tokens Jan 1, 2025.

## Feeds / tooling — NEW SECTION Nov 25
- RSSHub — for any site without a feed — https://docs.rsshub.app/ — NEW Nov 25. Open-source, self-host via Docker. Turns sites without feeds into standard RSS/Atom. Public demo exists but is rate-limited, recommend self-hosting. A format bridge, not an access bypass.

## Fragile routes — status Nov 25, 2026 (do not present as working)
- Nitter — DEAD. nitter.net answers 410 Gone (Nov 20, 2026) after X Corp cease-and-desist letters Aug 24 + Sep 8, 2026. Do not add.
- Redlib — DEGRADED. Comment pages blocked since Oct 20, 2026; no working public instance found Nov 9, 2026. Keep HIGH / UNVERIFIED.
- Invidious — ALIVE, DEGRADED. Release v2.20261114.0, Nov 14, 2026. Only 4 public instances left. Self-host only.
- Piped — ALIVE, SELF-HOST ONLY. 7 of 15 listed instances gone Nov 4, 2026. Do not list any specific public instance as working.
- ProxiTok, Farside, Hyperpipe, SafeTwitch — DEAD / discontinued. Do not add.

Total: 126 catalog entries. This packaged list is intentionally compliance-filtered and may not retain unsafe or dead entries.
