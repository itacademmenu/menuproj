datatableview.auto_initialize = false;
$(function(){
    var xeditable_options = {};
    datatableview.initialize($('.datatable'), {
        fnRowCallback: datatableview.make_xeditable(xeditable_options),
    });
})