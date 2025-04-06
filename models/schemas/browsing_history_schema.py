from models import ma
from models.browsing_history import BrowsingHistory

class BrowsingHistorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'site_nm', 'site_url', 'createdAt', 'chrome_extention_uuid', 'user_id')
        model = BrowsingHistory

browsing_history_schema = BrowsingHistorySchema()
browsing_histories_schema = BrowsingHistorySchema(many=True) 