# [Authentication](/docs/api-reference/authentication)
## [API keys](/docs/api-reference/api-keys)
The OpenAI API uses API keys for authentication. You can create API keys
        at a user or service account level. Service accounts are tied to a "bot"
        individual and should be used to provision access for production
        systems. Each API key can be scoped to one of the following, 
- **Project keys** - Provides access to a single project
          (**preferred option**); access
          [Project API keys](/settings/organization/general) by
          selecting the specific project you wish to generate keys against.  

- **User keys** - Our legacy keys. Provides access to all
          organizations and all projects that user has been added to; access
          [API Keys](/account/api-keys) to view your available keys.
          We highly advise transitioning to project keys for best security
          practices, although access via this method is currently still
          supported.  

**Remember that your API key is a secret!** Do not share it
        with others or expose it in any client-side code (browsers, apps).
        Production requests must be routed through your own backend server where
        your API key can be securely loaded from an environment variable or key
        management service. 
All API requests should include your API key in an
        Authorization HTTP header as follows: 

```python
Authorization: Bearer OPENAI_API_KEY
```
## [Organizations and projects (optional)](/docs/api-reference/organizations-and-projects-optional)
For users who belong to multiple organizations or are accessing their
        projects through their legacy user API key, you can pass a header to
        specify which organization and project is used for an API request. Usage
        from these API requests will count as usage for the specified
        organization and project. 
To access the Default project in an organization, leave out
        the OpenAI-Project header 
Example curl command: 

```python
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "OpenAI-Organization: YOUR_ORG_ID" \
  -H "OpenAI-Project: $PROJECT_ID"
```
Example with the openai Python package: 

```python
from openai import OpenAI
client = OpenAI(
  organization='YOUR_ORG_ID',
  project='$PROJECT_ID',
)
```
Example with the openai Node.js package: 

```python
import OpenAI from "openai";
const openai = new OpenAI({
    organization: "YOUR_ORG_ID",
    project: "$PROJECT_ID",
});
```
Organization IDs can be found on your
        [Organization settings](/account/organization) page. Project
        IDs can be found on your [General settings](/settings) page
        by selecting the specific project. 
