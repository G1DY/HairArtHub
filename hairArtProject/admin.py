from flask_admin.contrib.sqla import ModelView

from hairArtProject import db

from .models import Services


class ServicesAdminView(ModelView):
    column_list = ['service_name', 'description', 'duration', 'price'] 
    form_columns = ['service_name', 'description', 'duration', 'price'] 
    column_searchable_list = ['service_name'] 
    column_filters = ['duration'] 
    edit_modal = True  
    create_modal = True 
    can_export = True 


admin.add_view(ServicesAdminView(Services, db.session))