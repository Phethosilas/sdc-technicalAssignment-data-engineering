# Assignment: NEWSAPI

An assignment which leverages NEWSAPI. A news api for getting breaking news headlines and searching articles from news sources and blogs around the world.
By Phetho Silas Mokgalapa

Basic app overview
![app.drawio.png](..%2Fimages%2Fapp.png)


 Ethical API querying practices are crucial for ensuring fair and responsible use of application programming interfaces (APIs) while respecting the rights and resources of API providers, as well as the privacy and security of users' data. Here's a brief exploration of some key ethical considerations:

Respect API Usage Policies: Every API provider typically has usage policies outlined in their terms of service or documentation. It's essential to review and adhere to these policies, including rate limits, usage quotas, and acceptable use cases. Exceeding these limits or using the API for prohibited activities can lead to suspension of access or legal consequences.

Minimize Unnecessary Queries: Avoid making excessive or unnecessary API queries, as this can strain the API provider's infrastructure and may result in degraded service for other users. Optimize your queries to retrieve only the data you need, and cache responses whenever possible to reduce redundant requests.

Use Backoff Strategies: Implement backoff strategies to handle rate limits and server errors gracefully. When an API responds with rate limit exceeded or server errors, back off and retry requests after a reasonable delay rather than continuously bombarding the API with retries.

Respect Privacy and Security: When working with APIs that handle sensitive or personal data, ensure that you handle this data responsibly and in compliance with relevant privacy regulations such as GDPR or CCPA. Avoid storing sensitive data longer than necessary and use encryption and other security measures to protect data in transit and at rest.

Obtain User Consent: If your application collects user data or interacts with APIs on behalf of users, obtain clear and informed consent from users regarding how their data will be used and shared. Be transparent about the types of data you collect, how it will be processed, and any third-party APIs or services involved.

Monitor API Usage: Regularly monitor your API usage and performance metrics to identify any abnormal patterns or excessive usage that may indicate misuse or abuse. Address any issues promptly to prevent disruptions to your own application and to avoid violating API provider policies.

Contribute to API Ecosystem: Whenever possible, contribute positively to the API ecosystem by providing feedback to API providers, reporting bugs or vulnerabilities responsibly, and sharing knowledge and best practices with other developers. Collaboration and communication within the developer community can help improve APIs and foster a more ethical and sustainable ecosystem.