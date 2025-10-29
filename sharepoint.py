from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential

password = "Toyoda@0997"
sharepoint_url = "https://toyotabrasil.sharepoint.com/sites/memorial_dwg_materiais_gps"
username = "aaloliveira@toyota.com.br"


# Folder path within SharePoint (e.g., "Shared Documents/MyFolder")
folder_server_relative_url = "/sites/memorial_dwg_materiais_gps/Documentos%20Compartilhados/Memorial%20%26%20DWG_YG%27s%20TDB" 

# Authenticate with SharePoint
ctx = ClientContext(sharepoint_url).with_credentials(UserCredential(username, password))

# Get the target folder
target_folder = ctx.web.get_folder_by_server_relative_url(folder_server_relative_url)

# Load the files within the folder
target_folder.files.expand(["ListItemAllFields"]).get().execute_query()

# Iterate and print file names
for file in target_folder.files:
    print(file.name)