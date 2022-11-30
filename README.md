# Send emails on Azure With GraphAPI

Sample scripts for sending emails using Azure. Utilizes the Microsoft Authentication Library(MSAL) that allows signing into Azure AD, registering an app, and obtaining tokens to call Microsoft Graph API to allow sending emails with attachments. 


### Step 1:  Clone or download this repository

From your shell or command line:

```Shell
git clone https://github.com/AgnesMuita/emails-with-graph-api-on-azure.git
```

### Step 2:  Register the sample with your Azure Active Directory tenant

Some registration is required for Microsoft to act as an authority for your application.

#### Choose the Azure AD tenant where you want to create your applications

1. Sign in to the [Azure portal](https://portal.azure.com).
> If your account is present in more than one Azure AD tenant, select `Directory + Subscription`, which is an icon of a notebook with a filter next to the alert icon, and switch your portal session to the desired Azure AD tenant.
2. Select **Azure Active Directory** from the left nav.
3. Select **App registrations** from the new nav blade.

#### Register the client app

1. In **App registrations** page, select **New registration**.
1. When the **Register an application page** appears, enter your application's registration information:
   - In the **Name** section, enter a meaningful application name that will be displayed to users of the app, for example `device-code-sample`.
   - In the **Supported account types** section, select the last option **Accounts in any organizational directory and personal Microsoft accounts**.
   - Device Code Flow disables the need for a redirect URI. Leave it blank.
1. Select **Register** to create the application.
1. On the app **Overview** page, find the **Application (client) ID** value and copy it to your *parameters.json* file's *client_id* entry.
1. In **Authentication* select the recommended Redirect URIs for public clients.
1. Then set the Default Client Type to `Yes` and Save.

1. In the list of pages for the app, select **API permissions**
   - Click the **Add a permission** button and then,
   - Ensure that the **Microsoft APIs** tab is selected
   - In the *Commonly used Microsoft APIs* section, click on **Microsoft Graph**
   - In the **Delegated permissions** section, ensure that the right permissions are checked: **User.Read**. Use the search box if necessary.
   - Select the **Add permissions** button


### Step 3: Run the sample

You'll need to install the dependencies using pip as follows:

```Shell
pip install msal requests
```
To utilize MSAL's ConfidentialClientApplication approach, run
```Shell
python index.py
```
This will open a browser tab. Use the code printed on the terminal for authentication. 
<img width="616" alt="image" src="https://user-images.githubusercontent.com/67423874/204729146-b5973c57-2970-4af4-991d-77955cbb71c0.png">


On authentication, it will be possible to the email. 
