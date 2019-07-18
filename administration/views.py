from datatableview.views import XEditableDatatableView
from customer.models import UserOrder
from datatableview.helpers import make_xeditable


class AdminView(XEditableDatatableView):
    model = UserOrder
    datatable_options = {
        'columns': [
            'id',
            'name',
            'sum_paid',
            ("Order", 'order', make_xeditable),
        ]
}



