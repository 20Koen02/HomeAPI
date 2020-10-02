###########
# GENERAL #
###########

app_title = "HomeAPI"
app_description = "HomeAPI by Koen02. It connects local machines & smart devices to the internet"
app_version = "0.1.0"
import os
# Categories Descriptions
tags_metadata = [
    {
        "name": "machines",
        "description": "Manage HomeAPI enabled machines",
    },
    {
        "name": "lights",
        "description": "Manage Lights",
    },
    {
        "name": "auth",
        "description": "Authentication",
    }
]

############
# DATABASE #
############

database_url = f'postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("POSTGRES_HOST")}/{os.getenv("POSTGRES_DB")}'

########
# AUTH #
########

token_expires_in_minutes = 60
jwt_algorithm = "HS256"
