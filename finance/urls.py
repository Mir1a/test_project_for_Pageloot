# region				-----External Imports-----
# endregion

# region				-----Internal Imports-----
from .api import urls as urls

# endregion

# region			  -----Supporting Variables-----
# endregion

urlpatterns = urls.finance_router.urls
