$(document).ready(function () {
    var grid;
    grid = $('#grid').grid({
        dataSource: ORDERS_LIST_JSON_URL,
        uiLibrary: 'bootstrap4',
        primaryKey: 'id',
        inlineEditing: { mode: 'command' },
        columns: [
            { field: 'id', width: 44 },
            { field: 'name', type:'text', editor: true },
            { field: 'order', type:'text', editor: true },
            { field: 'comment', type:'text', editor: true },
            { field: 'sum_paid', editor: true }
        ],
        pager: { limit: 5 }
    });
    grid.on('rowDataChanged', function (e, id, record) {
        // Clone the record in new object where you can format the data to format that is supported by the backend.
        var data = $.extend(true, {}, record);
        // Post the data to the server
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
       var csrftoken = getCookie('csrftoken');
        console.log(data);
        $.ajax({method: 'PUT', contentType: 'application/json' , url: ORDERS_LIST_JSON_UPDATE, data: JSON.stringify(data), headers:{"X-CSRFToken": csrftoken}})
            .fail(function () {
                alert('Failed to save.');
            });
    });
    grid.on('rowRemoving', function (e, $row, id, record) {
        if (confirm('Are you sure?')) {
            function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
       var csrftoken = getCookie('csrftoken');
        $.ajax({ method: 'DELETE', url: ORDERS_LIST_JSON_DELETE, data: {id : id}, headers:{"X-CSRFToken": csrftoken}})
            .done(function () {
                grid.reload();
            })
            .fail(function () {
                alert('Failed to delete.');
            });
        }
    });
});

